import requests, folium

class Addresses:
    def __init__(self, node,way,relation,tag):
        self.node = node
        self.way = way
        self.relation = relation
        self.tag = tag

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

    def LoadMap(self):
        map = folium.Map()
        return map