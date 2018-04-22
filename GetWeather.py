import requests, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('api_key')
parser.add_argument('city')
parser.add_argument('state')
args = parser.parse_args()


wu_api_key = args.api_key
wu_city = args.city
wu_state = args.state
print(wu_api_key, wu_city, wu_state)
wu_api_url = "https://api.wunderground.com/api/{0}/conditions/q/{2}/{1}.json".format(wu_api_key,
                                                                                    wu_city, wu_state)

response = requests.get(wu_api_url)

weatherDict = json.loads(response.text)

print(weatherDict['current_observation']['display_location']['full'])
print("Current Temp: {0} F".format(weatherDict['current_observation']['temp_f']))

print("Windstring: {0} ".format(weatherDict['current_observation']['wind_string']))
