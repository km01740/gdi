import urllib.request
import socket
import urllib.request
import json

RECIPE_URL = "https://api.edamam.com/search?q=chicken&app_id=ab31695f&app_key=820cb037f347b158261c248745abc0f4" \
             "&from=0&to=3&calories=500-700"

timeout = 10
socket.setdefaulttimeout(timeout)
req = urllib.request.Request(RECIPE_URL)
response = urllib.request.urlopen(req)
response_body = response.read().decode("utf-8")
response_body = response_body.replace('\n', ' ').replace('\r', '')
parsed_json = json.loads(response_body)
for recipe in parsed_json['hits']:
    print ("Recipe Name: " + recipe['recipe']['label'])
    print()
    print ("Calories: {}".format(recipe['recipe']['calories']))
    print()
    print()
    
