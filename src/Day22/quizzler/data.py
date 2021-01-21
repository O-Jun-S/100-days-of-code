import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

URL = "https://opentdb.com/api.php"
response = requests.get(URL, params=parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]