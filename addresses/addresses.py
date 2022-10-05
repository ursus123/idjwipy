import requests, json, overpy, overpy.helper, json,pprint, folium, pyspark, os, sys,pandas as pd, pyspark.pandas as ps
from collections import defaultdict
os.environ['PYSPARK_DRIVER_PYTHON_OPTS']= "notebook"
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['PYSPARK_PYTHON'] = sys.executable

class GetInfo:
    def __init__(self,func):
        self.func = func
    def Fields(func):
         def GetFields(*args):
            data = func(*args).json()
            addresses = defaultdict(list)

            for i in data['elements']:
                addresses['id'].append(i['id'])
                addresses['type'].append(i['type'])
                try:
                    addresses['street_number'].append(i['tags']['addr:housenumber'])
                except KeyError as e:
                    addresses['street_number'].append(None)
                try:
                    addresses['street_name'].append(i['tags']['addr:street'])
                except KeyError as e:
                    addresses['street_name'].append(None)

                try:
                    addresses['city'].append(i['tags']['addr:city'])
                except KeyError as e:
                    addresses['city'].append(None)

                try:
                    addresses['state'].append(i['tags']['addr:state'])
                except KeyError as e:
                    addresses['state'].append(None)

                try:
                    addresses['country'].append(i['tags']['addr:country'])
                except KeyError as e:
                    addresses['country'].append(None)

                try:
                    addresses['zipcode'].append(i['tags']['addr:postcode'])
                except KeyError as e:
                    addresses['zipcode'].append(None)
                dataframe = pd.DataFrame(addresses)
                return dataframe
            return GetFields



class Addresses:
    def __init__(self, query_string):
        self.query_string = query_string

    def LoadMap():
        map = folium.Map()
        return map

    def AmenityList():
        '''This is used to map facilities used by visitors and residents
        for example toilets, banks,pharmacies,...'''
        url = "http://wiki.openstreetmap.org/wiki/Key:amenity"
        df = pd.read_html(io = url)
        df = dict(df[1])[('Value', 'Sustenance')]
        AmenityList = list(df)
        return AmenityList

    def BarrierList():
        '''Barrier covers barriers or obstacles, that are usually used in travelling '''
        url = 'https://wiki.openstreetmap.org/wiki/Key:barrier'
        df = pd.read_html(io = url)
        df = dict(df[3])[('Value', 'Linear barriers (e.g. along a path or road)')]
        BarrierList = list(df)
        return BarrierList

    def BoundaryList(self):
        '''Boundaries Marks borders of areas, mostly political but also other administrative areas'''
        url = 'https://wiki.openstreetmap.org/wiki/Key:boundary'
        df = pd.read_html(io = url)
        df = dict(df[1])[('Value', 'Boundary types')]
        BoundaryList = list(df)
        return BoundaryList

    def OSMEndPoints():
        'This function returns APIs for Open Street Map'
        return '{0}'.format('https://lz4.overpass-api.de/api/interpreter')
    #@GetInfo.Fields
    def Query(query_string):
        api = overpy.Overpass()
        results = api.query(query_string)
        return results


