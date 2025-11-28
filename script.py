from decouple import config
import requests
import json
import pprint
import os

appid = config('APPID')
apikey = config('APIKEY')
lower = '2025-07-01T05:00:00Z'
upper = '2025-08-01T08:00:00Z'

headers = {
   'apikey': apikey
}

url = 'https://api.uxcam.com/v2/user/analytics'

# Tasa de abandono del carrito de compras add To Cart
params = {
   'appid': appid,
   'page': 1,
   'page_size': 500,
   'filters': json.dumps([
       {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       },
       {
            'attribute': 'event_count_per_user',
            'operator': 'greater',
            'value': {'count': 0, 'event_names': [' ']}
       }
    ])
}

response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
print('Add to cart')
pprint.pprint(json_response['data'])

## prueba
params = {
    "appid": "TU_APP_ID",
    "page": 1,
    "page_size": 500,
    "filters": [
        {
            "attribute": "event_name",
            "operator": "in",
            "value": ["addToCart"]
        },
        {
            "attribute": "event_uploadedon",
            "operator": "between_dates",
            "value": {
                "lower": "2025-07-01T05:00:00Z",
                "upper": "2025-08-01T08:00:00Z"
            }
        }
    ]
}

### fin prueba
response = requests.get(url=url, headers=headers, params=params)
print(response.url)      # muestra la URL final con filtros codificados
print(response.status_code)
print(response.json())
json_response = response.json()
print('Add to cart')
pprint.pprint(json_response['data'])

#  Orden confirmada confirmOrder
params = {
   'appid': appid,
   'page': 1,
   'page_size': 500,
   'filters': json.dumps([
       {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       },
       {
            'attribute': 'event_count_per_user',
            'operator': 'greater',
            'value': {'count': 0, 'event_names': ['confirmOrder']}
       }
    ])
}
response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
print('Orden confirmada')
pprint.pprint(json_response['data'])

## Eventos y analiticas
url = 'https://api.uxcam.com/v2/event/analytics'
params = {
   'appid': appid,
   'page': 1,
   'page_size': 500,
   'filters': json.dumps([
       {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': upper,
               'upper': lower
           }
       },
       {
            'attribute': 'event_name',
            'operator': 'in',
            'value': ['confirmOrder', 'addToCart']
        },
    ]),
    'group_by': json.dumps([
        {'attribute': 'event_name'}
    ])
}

response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
pprint.pprint(json_response['data'])

## eventos
url = 'https://api.uxcam.com/v2/event'

params = {
   'appid': appid,
   'page_size': 500,
   'page': 1,
   'filters': json.dumps([
        {
            'attribute':'event_custom_property',
            'operator':'equal',
            'property_name':'Regional',
            'value':'BOGOTA'
        },
        {
            'attribute': 'event_name',
            'operator': 'equal',
            'value': 'confirmOrder'
        },
        {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       },
    ])
}

response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
print('regional')
pprint.pprint(json_response['data'][0])

# duración promedio de la sesion
url = 'https://api.uxcam.com/v2/session/analytics'

params = {
   'appid': appid,
   'page_size': 500,
   'page': 1,
   'filters': json.dumps([
        {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       },
    ])
}

response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
print('promedio sesion')
pprint.pprint(json_response['data'])

#usuarios nuevos por regional

url = 'https://api.uxcam.com/v2/user/analytics'

params = {
   'appid': appid,
   'page': 1,
   'page_size': 500,
   'filters': json.dumps([
       {
           'attribute': 'user_first_seen_on',
           'operator': 'after',
           'value': '2024-12-01',
        #    'property':{
        #        'name':'Regional',
        #        'operator':'equal',
        #        'value':'ANTIOQUIA'
        #    }
       },
       {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       },
    #    {
    #         'attribute':'user_custom_property',
    #         'operator':'equal',
    #         'property_name':'Regional',
    #         'value':'BOGOTA'
    #     },
    ]),
    'group_by': json.dumps([
        {'attribute': 'user_custom_property', 'property_name': 'Regional'}
    ])
}
response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
print('nuevos usuarios por regional')
pprint.pprint(json_response['data'])
pprint.pprint(json_response['data'][0])

#sesiones por dia
url = 'https://api.uxcam.com/v2/session/analytics'

params = {
   'appid': appid,
   'page': 1,
   'page_size': 500,
   'filters': json.dumps([
       {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       }
    ]),
    'group_by': json.dumps([
        {'attribute': 'session_uploadedon_day'}
    ])
}

response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
pprint.pprint(json_response['data'])

#Productos mas vistos vs productos mas comprados
url = 'https://api.uxcam.com/v2/event/analytics'

params = {
   'appid': appid,
   'page': 1,
   'page_size': 500,
   'filters': json.dumps([
       {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       },
       {
            'attribute': 'event_name',
            'operator': 'equal',
            'value': 'seeDetailProduct'
        },
    ]),
    'group_by': json.dumps([
        {'attribute': 'event_custom_property', 'property_name': 'name', 'max_group_number': 1000}
    ])
}

response_detail = requests.get(url=url, headers=headers, params=params)
json_response_detail = response_detail.json()
pprint.pprint(json_response_detail)

for event in json_response_detail['data']:
    if 'aloha' in event['event_custom_property_name'].lower():
        pprint.pprint(event)
params = {
   'appid': appid,
   'page': 1,
   
   'page_size': 500,
   'filters': json.dumps([
       {
           'attribute': 'date_range',
           'operator': 'between_dates',
           'value': {
               'lower': lower,
               'upper': upper
           }
       },
       {
            'attribute': 'event_name',
            'operator': 'equal',
            'value': 'clickPlaceIndividualOrder'
        },
    ]),
    'group_by': json.dumps([
        {'attribute': 'event_custom_property', 'property_name': 'product', 'max_group_number': 1000}
    ])
}

response = requests.get(url=url, headers=headers, params=params)
json_response = response.json()
pprint.pprint(json_response)

for event in json_response['data']:
    if 'aloha' in event['event_custom_property_product'].lower():
        pprint.pprint(event)