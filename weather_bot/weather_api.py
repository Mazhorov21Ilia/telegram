import weatherapi

configuration = weatherapi.Configuration()
configuration.api_key['key'] = 'your_key'
api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))



def get_forecast(date):
    q = 'Moscow'
    days = 1
    dt = date
    lang = 'ru'
    api_response = api_instance.forecast_weather(q, lang=lang, dt=date, days=days, aqi='no')
    return api_response

