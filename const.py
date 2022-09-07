TOKEN = '5686445425:AAESKAv8b9gS6kjGwsn3n87yotc262anOhk'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'

SEND_METH = 'sendMessage'

MY_ID = 5258094888

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    UPDATE_ID = file.readline()

WEATHER_TOKEN = '5e0d8e38a0c8e2491f54774b16f3db1c'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'