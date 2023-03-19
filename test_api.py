import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

apikey = config['DEFAULT']['apikey']

resp = requests.get('http://opendata.translinkniplanner.co.uk/Ext_API/XML_TRIP_REQUEST2?ext_macro=trip&type_origin=any&name_origin=10000566&type_destination=1&name_destination=10000011&itdDate=20230319', headers={'X-API-TOKEN': apikey})

print(resp.text)
