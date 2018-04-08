import requests, json

wu_api_key = "f357186b72c393f0"
wu_api_url = "https://api.wunderground.com/api/{0}/conditions/q/CO/Denver.json".format(wu_api_key)

response = requests.get(wu_api_url)

weatherDict = json.loads(response.text)

print(weatherDict['current_observation']['display_location']['full'])
print("Current Temp: {0} F".format(weatherDict['current_observation']['temp_f']))

