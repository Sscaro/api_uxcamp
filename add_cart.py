from decouple import config
import json
import pprint
from api_conexion import api_connect

def addToCart():

    url = 'https://api.uxcam.com/v2/event/analytics?'  #
    conexion = api_connect(url)       

    appid = config('APPID')
    apikey = config('APIKEY')
    lower = '2025-07-01T05:00:00Z'
    upper = '2025-08-01T08:00:00Z'
    
    #headers = {
    #'apikey': apikey, 
    #'Content-Type': 'application/json' 
    #}
   # url = 'https://api.uxcam.com/v2/user/analytics'
   # end point para addTo cart y confirmOrder
    event_filters = [
        {'attribute': 'event_name',
        'operator': 'equal',
         'value': 'addToCart' # Lista de nombres de eventos que quieres filtrar
        },
        {  'attribute': 'date_range',
            'operator': 'between_dates',
            'value': {
            'lower': lower,
            'upper': upper
        }
        }
    ]
    params_event = {
    'appid': appid,
    'page': 1,
    'page_size': 500,
    'filters': json.dumps(event_filters)
    }

    response = conexion.metodo_get(params_event)
    #response = requests.get(url=url, headers=headers, params=params_event)

    print('Add to cart')
    pprint.pprint(response.keys())
    pprint.pprint(response['data'])


def complete_purshase():

    url = 'https://api.uxcam.com/v2/event/analytics?'  #
    conexion = api_connect(url)       

    appid = config('APPID')
    apikey = config('APIKEY')
    lower = '2025-07-01T05:00:00Z'
    upper = '2025-08-01T08:00:00Z'
    
    #headers = {
    #'apikey': apikey, 
    #'Content-Type': 'application/json' 
    #}
   # url = 'https://api.uxcam.com/v2/user/analytics'
   # end point para addTo cart y confirmOrder
    event_filters = [
        {'attribute': 'event_name',
        'operator': 'equal',
         'value': 'confirmOrder' # Lista de nombres de eventos que quieres filtrar
        },
        {  'attribute': 'date_range',
            'operator': 'between_dates',
            'value': {
            'lower': lower,
            'upper': upper
        }
        }
    ]
    params_event = {
    'appid': appid,
    'page': 1,
    'page_size': 500,
    'filters': json.dumps(event_filters)
    }

    response = conexion.metodo_get(params_event)
    #response = requests.get(url=url, headers=headers, params=params_event)

    print('complete purshase')
    pprint.pprint(response.keys())
    pprint.pprint(response['data'])

def new_user_by_region():

    url = 'https://api.uxcam.com/v2/user/analytics?'  #
    conexion = api_connect(url)       

    appid = config('APPID')
    lower = '2025-09-01T05:00:00Z'
    upper = '2025-09-30T08:00:00Z'
    
    #headers = {
    #'apikey': apikey, 
    #'Content-Type': 'application/json' 
    #}
   # url = 'https://api.uxcam.com/v2/user/analytics'
   # end point para addTo cart y confirmOrder
    event_filters = [
        {'attribute': 'user_first_seen_on',
        'operator': 'between_dates',
         'value': {
            'lower': lower,
            'upper': upper
        }  # Lista de nombres de eventos que quieres filtrar
        }]
    aggregations =  [ {"atributte":"user_count",
                         "operator":""}]
    group_by_data =[{'attribute': 'region'
    }]                    
    params_event = {
    'appid': appid,
    'page': 1,
    'page_size': 500,
    'filters': json.dumps(event_filters),
    'aggreation': json.dumps(aggregations)}
    response = conexion.metodo_get(params_event)
    #response = requests.get(url=url, headers=headers, params=params_event)

    print('new user by region')
    pprint.pprint(response.keys())
    pprint.pprint(response['data'])

def session_average_duration():

    url = 'https://api.uxcam.com/v2/session/analytics'  #
    conexion = api_connect(url)
    appid = config('APPID')
    lower = '2025-08-01T05:00:00Z'
    upper = '2025-08-31T08:00:00Z'
    
    #headers = {
    #'apikey': apikey, 
    #'Content-Type': 'application/json' 
    #}
   # url = 'https://api.uxcam.com/v2/user/analytics'
   # end point para addTo cart y confirmOrder
    event_filters = [
        {'attribute': 'session_uploadedon',
        'operator': 'between_dates',
         'value': {
            'lower': lower,
            'upper': upper
        }  # Lista de nombres de eventos que quieres filtrar
        }]
    aggregations =  [ {"atributte":"session_duration",
                         "operator":"avg"}]
    params_event = {
    'appid': appid,
    'page': 1,
    'page_size': 500,
    'filters': json.dumps(event_filters),
    'aggreation': json.dumps(aggregations)    }
    response = conexion.metodo_get(params_event)
    #response = requests.get(url=url, headers=headers, params=params_event)

    print('Avg Session Duration')
    pprint.pprint(response.keys())
    pprint.pprint(response['data'])

def num_session_by_day_week():

    url = 'https://api.uxcam.com/v2/session/analytics'  #
    conexion = api_connect(url)      
    appid = config('APPID')
    lower = '2025-09-01T05:00:00Z'
    upper = '2025-09-30T08:00:00Z'
    
    #headers = {
    #'apikey': apikey, 
    #'Content-Type': 'application/json' 
    #}
   # url = 'https://api.uxcam.com/v2/user/analytics'
   # end point para addTo cart y confirmOrder
    event_filters = [
        {'attribute': 'session_uploadedon',
        'operator': 'between_dates',
         'value': {
            'lower': lower,
            'upper': upper
        }  # Lista de nombres de eventos que quieres filtrar
        }]
    aggregations =  [ {"attribute":"session_count",
                         'operator':''}]
    group_by_data =[{'attribute': 'session_user_weekday'
    }]
    params_event = {
    'appid': appid,
    'page': 1,
    'page_size': 500,
    'filters': json.dumps(event_filters),
    'aggregation': json.dumps(aggregations),
    'group_by': json.dumps(group_by_data)}

    response = conexion.metodo_get(params_event)
    #response = requests.get(url=url, headers=headers, params=params_event)

    print('Num session per day week')
    pprint.pprint(response.keys())
    pprint.pprint(response['data'])

def num_session_by_hour_of_day():

    url = 'https://api.uxcam.com/v2/session/analytics'
    conexion = api_connect(url)
    appid = config('APPID')
    lower = '2025-09-01T05:00:00Z'
    upper = '2025-09-30T08:00:00Z'
    
    #headers = {
    #'apikey': apikey, 
    #'Content-Type': 'application/json' 
    #}
   # url = 'https://api.uxcam.com/v2/user/analytics'
   # end point para addTo cart y confirmOrder
    event_filters = [
        {'attribute': 'session_uploadedon',
        'operator': 'between_dates',
         'value': {
            'lower': lower,
            'upper': upper
        }  # Lista de nombres de eventos que quieres filtrar
        }]
    aggregations =  [ {"attribute":"session_count",
                         'operator':''}]
    group_by_data =[{'attribute': 'session_hour_of_day_user'
    }]
    params_event = {
    'appid': appid,
    'page': 1,
    'page_size': 500,
    'filters': json.dumps(event_filters),
    'aggregation': json.dumps(aggregations),
    'group_by': json.dumps(group_by_data)}

    response = conexion.metodo_get(params_event)
    #response = requests.get(url=url, headers=headers, params=params_event)

    print('Num session per day week')
    pprint.pprint(response.keys())
    pprint.pprint(response['data'])


def select_product():

    url = 'https://api.uxcam.com/v2/event/analytics'  #
    conexion = api_connect(url)
    appid = config('APPID')
    lower = '2025-07-01T05:00:00Z'
    upper = '2025-08-01T08:00:00Z'    
    #headers = {
    #'apikey': apikey, 
    #'Content-Type': 'application/json' 
    #}
    # url = 'https://api.uxcam.com/v2/user/analytics'
    # end point para addTo cart y confirmOrder

    event_filters=[{"attribute":"event_name",
            "operator":"in",
            "value":["seeDetailProduct"]},

            {"attribute":"event_uploadedon",
            "operator":"between_dates",
            "value":{"lower": lower,
             "upper":upper}}]
    
    aggregations=[{"attribute":
    "event_count","operator":""}]
    group_by_data=[{"attribute":"event_custom_property",
    "property_name":"name"}]
  
    params_event = {
    'appid': appid,
    'page': 1,
    'page_size': 500,
    'filters': json.dumps(event_filters),
    'aggregation': json.dumps(aggregations),
    'group_by': json.dumps(group_by_data)}

    response = conexion.metodo_get(params_event)
    #response = requests.get(url=url, headers=headers, params=params_event)

    print('Num session per day week')
    pprint.pprint(response.keys())
    pprint.pprint(response['data'])

if __name__ == "__main__":

    #addToCart()
    #complete_purshase()
    #new_user_by_region()
    # print(1)
    #session_average_duration()
    #num_session_by_day_week()
    #num_session_by_hour_of_day()
    select_product()
