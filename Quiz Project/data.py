import requests


response = requests.get("https://opentdb.com/api.php?amount=20&category=22&type=boolean")
data = response.json()