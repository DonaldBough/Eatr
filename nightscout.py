import datetime
import requests

def postCarbsToNightscout(carbs, url, api_secret_hashed):
	now = datetime.datetime.now()
	nowInExpectedTimeZone = now + datetime.timedelta(hours=5)
	nowDate = str(nowInExpectedTimeZone).split(' ')[0]
	nowTime = str(nowInExpectedTimeZone).split(' ')[1]

	querystring = {"token":token,"API-SECRET":api_secret_hashed}

	payload = "[{\r\n\t\"carbs\": " + carbs + ",\r\n\t\"created_at\": \"" + nowDate + "T" + nowTime + "Z\",\r\n\t\"duration\": 0,\r\n\t\"enteredBy\": \"\",\r\n\t\"eventType\": \"Carb Correction\",\r\n\t\"reason\": \"\"\r\n}]"
	print('Payload: ' + payload)
	headers = {
	    'Content-Type': "application/json",
	    'cache-control': "no-cache",
	    'Postman-Token': "8d3ce8d7-5551-4392-8904-a975b16d4433"
	    }

	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
	print(response.text)

url = "https://donaldcgm.herokuapp.com/api/v1/treatments"
token = "python_api-63f7b17540f3f091"
api_secret_hashed = "01964733944759139eab117430f96a5ea6727138"
postCarbsToNightscout("14", url, api_secret_hashed)