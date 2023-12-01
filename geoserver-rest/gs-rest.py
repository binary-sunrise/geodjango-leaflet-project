# Import the library
from geo.Geoserver import Geoserver
# Initialize the library
geo = Geoserver('http://127.0.0.1:8000/geoserver', username='admin', password='geoserver')
# # For creating workspace
# geo.create_workspace(workspace='demo')
# # For uploading raster data to the geoserver
# geo.create_coveragestore(layer_name='layer1', path=r'C:\Users\times_sxzwm75\OneDrive - TIMESWORLD MEDIA AND TECHNOLOGY SOLUTIONS PVT. LTD\Projects\My projects\geoserver-rest\data\Landsat_ETM_2001-08-26_multispectral.tif', workspace='demo')
# # For creating postGIS connection and publish postGIS table
# geo.create_featurestore(store_name='geo_data', workspace='demo', db='project_1', host='127.0.0.1', pg_user='postgres',
#                         pg_password='Unni@2885')
# geo.publish_featurestore(workspace='demo', store_name='geo_data', pg_table='district')
# For uploading SLD file and connect it with layer
geo.upload_style(path=r'C:\Users\times_sxzwm75\OneDrive - TIMESWORLD MEDIA AND TECHNOLOGY SOLUTIONS PVT. LTD\Projects\My projects\geoserver-rest\style\districts2.sld', workspace='demo')
geo.publish_style(layer_name='district', style_name='districts2', workspace='demo')