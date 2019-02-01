import json
import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "a6wz72iuhi513rs66muxezw7xow56p",
    "user": "gig7rn39w69sf5ahk5uucvc3814m4c",
    "message": "Eat some protein yo",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()