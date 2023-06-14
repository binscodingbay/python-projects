import requests
from datetime import datetime
import os
API_KEY=os.environ.get('ENV_NIX_API_KEY')
API_ID=os.environ.get('ENV_NIX_API_ID')
exercise_endpoint=os.environ.get('ENV_exercise_endpoint')
sheet_endpoint=os.environ.get('ENV_sheet_endpoint')
USER=os.environ.get('ENV_USER')
PASSWORD=os.environ.get('ENV_PASSWORD')
print(API_ID,API_KEY,exercise_endpoint,sheet_endpoint,USER,PASSWORD)

headers = {
    'x-app-id':API_ID.replace('"', '').strip(),
    'x-app-key':API_KEY.replace('"', '').strip(),
}
print(headers)

user_query = input("Tell me which exercises you did? ")
user_params = {
    "query": user_query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=exercise_endpoint.replace('"', ''), json=user_params, headers=headers)
response.raise_for_status()
results = response.json()
print(results)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint.replace('"', ''), json=sheet_inputs, auth=(USER.replace('"', '').strip(),PASSWORD.replace('"', '').strip()))

    print(sheet_response.text)

