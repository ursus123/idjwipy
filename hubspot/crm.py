import requests, json, os, sys, pandas as pd,urllib.parse
from collections import defaultdict

def HubSpotGetProps(object,OAuth):
    try:
        url = 'https://api.hubapi.com/crm/v3/properties/{0}'.format(object)
        headers = {'content-type': 'application/json',
                    'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
        response = requests.get(url, headers = headers)
        resp = response.json()['results']
        properties = defaultdict(list)
        for i in resp:
            properties['name'].append(i['name'])
            properties['label'].append(i['label'])
            properties['fieldType'].append(i['fieldType'])
            properties['groupName'].append(i['groupName'])
            properties['type'].append(i['type'])
            properties['hidden'].append(i['hidden'])
            properties['displayOrder'].append(i['displayOrder'])
            properties['options'].append(i['options'])
            properties['hasUniqueValue'].append(i['hasUniqueValue'])
            properties['formField'].append(i['formField'])
        data = pd.DataFrame(properties)
        return data
    except KeyError as e:
        return 'Try Hubspot Objects for example: [contacts,companies,deals..]'

def HubSpotGetRecords (object, OAuth, properties,limit=100):
    propsSetup = {'properties': properties}
    property = urllib.parse.urlencode(propsSetup, doseq=True)
    url = 'https://api.hubapi.com/crm/v3/objects/{0}?limit={1}&{2}&archived=false'.format(object, limit, property)
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
    if limit <= 100:
        try:
            response = []
            resp = requests.get(url=url, headers=headers).json()
            while 'paging' in requests.get(url=url, headers=headers).json().keys():
                resp = requests.get(url=resp['paging']['next']['link'], headers=headers).json()
                response.append(resp)
                if len(response) == 100:
                    break
        except KeyError:
            pass
    else:
        return 'The Limit cannot exceed 100'
    records = defaultdict(list)

    for lists in response:
        for i in lists['results']:
            records['hs_object_id'].append(i['properties']['hs_object_id'])
            for j in properties:
                records[str(j)].append(i['properties'][str(j)])
    data = pd.DataFrame(records)
    return data

def HubSpotGetAssociations (from_object,object_id,to_object,OAuth):
    headers = {'content-type': 'application/json',
               'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
    records =defaultdict(list)
    for j in object_id:
        url = 'https://api.hubapi.com/crm/v4/objects/{0}/{1}/associations/{2}'.format(from_object,j,to_object)
        response = requests.get(url, headers=headers)
        resp = response.json()
        for i in resp['results']:
            records['fromObjectId'].append(j)
            records['toObjectId'].append(i['toObjectId'])
    data = pd.DataFrame(records)
    return data

def HubSpotGetCustomObj(OAuth):
    url = 'https://api.hubapi.com/crm/v3/schemas'
    headers = {'content-type': 'application/json',
               'properties': 'domain',
               'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
    response = requests.get(url, headers=headers)
    resp = response.json()
    custom_objects = defaultdict(list)
    for i in resp['results']:
        custom_objects['name'].append(i['primaryDisplayProperty'])
        custom_objects['objectTypeId'].append(i['objectTypeId'])
    return custom_objects

def HubSpotPutData(object,OAuth,data):
    data_dict = defaultdict(dict)
    for i in range(len(data)):
        data_dict[i] = defaultdict()
        if 'hs_object_id' in data.columns:
            data_dict[i]['hs_object_id'] = data.loc[i, 'hs_object_id']
        else:
            pass
        data_dict[i]['data'] = defaultdict()
        data_dict[i]['data']['properties'] = dict(data.iloc[i, 1:])

    headers = {'content-type': 'application/json',
               'properties': 'domain',
               'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
    for j in data_dict:
        url = 'https://api.hubapi.com/crm/v3/objects/{0}'.format(object)
        resp = requests.post(url, headers=headers, data=json.dumps(data_dict[j]['data']))
    return resp.json()

def HubSpotUpdateData(object,OAuth,data):
    data_dict = defaultdict(dict)
    for i in range(len(data)):
        data_dict[i] = defaultdict()
        if 'hs_object_id' in data.columns:
            data_dict[i]['hs_object_id'] = data.loc[i, 'hs_object_id']
        else:
            pass
        data_dict[i]['data'] = defaultdict()
        data_dict[i]['data']['properties'] = dict(data.iloc[i, 1:])

    headers = {'content-type': 'application/json',
               'properties': 'domain',
               'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
    for j in data_dict:
        url = 'https://api.hubapi.com/crm/v3/objects/{0}/{1}'.format(object,data_dict[i]['hs_object_id'])
        resp = requests.patch(url, headers=headers, data=json.dumps(data_dict[j]['data']))
    return resp.json()

def HubSpotCreateProps(object,OAuth,name,label,type,fieldType,groupName):
    url = 'https://api.hubapi.com/crm/v3/properties/{0}'.format(object)
    headers = {'content-type': 'application/json',
               'properties': 'domain',
               'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
    fieldType_list = list(HubSpotGetProps(object,OAuth=OAuth)['fieldType'].values.tolist())
    type_list = list(HubSpotGetProps(object,OAuth=OAuth)['type'])
    groupName_list = list(HubSpotGetProps(object,OAuth=OAuth)['groupName'])
    if fieldType not in fieldType_list:
        return 'This FieldType {0} is not right Try these: {1}'.format(fieldType,fieldType_list)
    elif type not in type_list:
        return 'This type {0} is not right Try these: {1}'.format(type,type_list)
    elif groupName not in groupName_list:
        return 'This groupName {0} is not right Try these: {1}'.format(groupName,groupName_list)
    else:
        data = {
            'name':name,
            'label':label,
            'type':type,
            'fieldType':fieldType,
            'groupName':groupName
        }
    response = requests.post(url=url, headers=headers,data=json.dumps(data))
    resp = response.json()
    return resp

def HubSpotDeleteProps(object,OAuth,name):
    url = 'https://api.hubapi.com/crm/v3/properties/{0}/{1}'.format(object,name)
    headers = {'content-type': 'application/json',
               'properties': 'domain',
               'authorization': 'Bearer %s' % '{0}'.format(OAuth)}
    requests.delete(url=url, headers=headers)
    return 'Deleting {0} Done'.format(name)
