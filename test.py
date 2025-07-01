import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_ACCESS")
url = "http://api.marketstack.com/v1/eod"
params = {
        'access_key' : api_key,
        'symbols' : 'AAPL',
        }

r = requests.get(url, params=params)
if r.status_code == 200:
    data = r.json()
    print(data)
else:
    print("failed")
