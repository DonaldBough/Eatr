import json
import http.client, urllib

# reading config file
parser = ConfigParser()
parser.read('configs/config.ini')

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": parser.get('pushover', 'token'),
    "user": parser.get('pushover', 'user'),
    "message": "Eat some protein yo",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()