from sqlalchemy import create_engine
from geoalchemy2 import Table as GEOTable
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData
from django.utils.translation import ugettext_lazy as _
import os
try:
    from osgeo import ogr
except ImportError:
    pass

from qdjango.models import Layer
from core.utils.projects import CoreMetaLayer


class QdjangoMetaLayer(CoreMetaLayer):

    layerTypesSingleLayer = (
        'wms',
    )

    def getCurrentByLayer(self, layer):
        """
        Get current metalayer value by qdjango layer type
        """

        self.countLayer += 1
        if isinstance(layer, dict):
            layerType = layer['layer_type']
            options = layer['options']
        else:

            # todo: manage options for layer object model
            layerType = layer.layer_type

        if layerType in self.layerTypesSingleLayer and options is not None:
            if self.countLayer > 1:
                self.increment()
            self.toIncrement = True
        elif self.toIncrement:
            self.increment()
            self.toIncrement = False

        return self.current


class QgisLayerStructure(object):

    def __init__(self, layer, **kwargs):
        self.layer = layer
        self.datasource = layer.datasource
        self.layerType = layer.layerType
        self.datasourceDict = {}
        self.columns = []

        self._errDatasourceNotFound = _('Missing data file for layer') + ' "{}"'
        self._errDatasourceNotFound += _('which should be located at') + ' "{}"'

    def getTableColumns(self):
        pass


class QgisOGRLayerStructure(QgisLayerStructure):

    def __init__(self, layer, **kwargs):
        super(QgisOGRLayerStructure, self).__init__(layer,**kwargs)

        # check datasource
        self._cleanDataSource()

        # get table columns
        self.getTableColumns()

    def _cleanDataSource(self):
        """
        Check if ogr data layer exisists
        """
        if not os.path.exists(self.datasource.split('|')[0]):
            raise Exception(self._errDatasourceNotFound.format(self.layer.name,self.datasource))

    def getTableColumns(self):
        """
        Get table column info from ogr layer by gdal python lib
        """
        dataSourceOgr = ogr.Open(self.datasource)
        daLayer = dataSourceOgr.GetLayer(0)
        layerDefinition = daLayer.GetLayerDefn()

        for i in range(layerDefinition.GetFieldCount()):
            self.columns.append({
                'name':layerDefinition.GetFieldDefn(i).GetName(),
                'type':layerDefinition.GetFieldDefn(i).GetFieldTypeName(layerDefinition.GetFieldDefn(i).GetType()).upper(),
                'label': layerDefinition.GetFieldDefn(i).GetName()
            })

        dataSourceOgr.Destroy()

class QgisDBLayerStructure(QgisLayerStructure):

    _dbTypes = {
        Layer.TYPES.postgres: 'postgresql+psycopg2',
        Layer.TYPES.spatialite: 'sqlite'
    }

    def __init__(self, layer, **kwargs):
        super(QgisDBLayerStructure, self).__init__(layer,**kwargs)

        if not self.layerType in self._dbTypes.keys():
            raise Exception('Database Layer Type not available in qdjango module: {}'.format(self.layerType))

        self.datasource2dict()

        # check datasource
        self._cleanDataSource()

        # get driver for geoalchemy
        getattr(self, 'getDriver_{}'.format(self.layerType))()

        # get table columns
        self.getTableColumns()

    def _cleanDataSource(self):
        """
        Chheck il spatilite fiel exists
        """
        if self.layerType ==  Layer.TYPES.spatialite:
            if not os.path.exists(self.datasourceDict['dbname']):
                raise Exception(self._errDatasourceNotFound.format(self.layer.name,self.datasource))


    def datasource2dict(self):
        """
        Read datasource string e put data in a python dict
        """

        datalist = self.datasource.split(' ')
        for item in datalist:
            try:
                key, value = item.split('=')
                self.datasourceDict[key] = value.strip('\'')
            except ValueError:
                pass

    def getSchemaTable(self):
        """
        Get and set in self sttributes value of table and schema
        """
        if self.datasourceDict['table'].find('.')!=-1:
            self.schema, self.table = self.datasourceDict['table'].split('.')
        else:
            self.schema = 'public'
            self.table = self.datasourceDict['table']

        self.table = self.table.strip('"')
        self.schema = self.schema.strip('"')

    def getDriver_postgres(self):
        """
        Get URL connection for sqlite postgresql+postgis2
        """

        self.getSchemaTable()
        # Connection url
        self.urlDB = URL(
            self._dbTypes[self.layerType],
            self.datasourceDict['user'],
            self.datasourceDict['password'],
            self.datasourceDict['host'],
            self.datasourceDict['port'],
            self.datasourceDict['dbname']
        )

    def getDriver_spatialite(self):
        """
        Get URL connection for sqlite geoalchemy
        """

        self.urlDB = URL(self._dbTypes[self.layerType], database = self.datasourceDict['dbname'])
        self.table = self.datasourceDict['table'].strip('"')
        self.schema = None

    def getTableColumns(self):

        # Some SQLAlchemy magic
        Base = declarative_base()
        engine = create_engine(self.urlDB, echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        meta = MetaData(bind=engine)
        messages = GEOTable(
            self.table, meta, autoload=True, autoload_with=engine, schema=self.schema
            )

        for c in messages.columns:
            try:
                self.columns.append({'name': c.name, 'type': str(c.type), 'label': c.name})
            except NotImplementedError:
                pass
