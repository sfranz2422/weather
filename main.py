import requests
from twilio.rest import Client
import os

account_sid = os.environ.get('ACCOUNT_SSID')
auth_token = os.environ.get('AUTH_TOKEN')
api_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get("OWM_API_KEY")
to_phone = os.environ.get("TO_PHONE")
from_phone = os.environ.get("FROM_PHONE")


def send_message():
    weather_message = f"{data['daily'][1]['weather'][0]['description']}." \
                      f"High: {data['daily'][0]['temp']['max']},Low: " \
                      f"{data['daily'][0]['temp']['min']} "

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to_phone,
        from_=from_phone,
        body=weather_message
    )

    print(message.sid)


weather_params = {
    'lat': os.environ.get("LAT"),
    'lon': os.environ.get("LON"),
    'appid': api_key,
    'units': 'imperial',
    'exclude': "current,minutely,hourly"
}

response = requests.get(url=api_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
send_message()
