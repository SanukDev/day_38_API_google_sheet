import requests
import datetime
ID_API = "0f335044"
API_KEY = "d377bd281e0dd11434262b1becada91d"
USER_NAME = "samuka"
GENDER = "Male"
AGE = "22"
WEIGHT_KG = "70"
HEIGHT_CM = "1.76"

HOST_DOMAIN = "https://trackapi.nutritionix.com"
API_ENDPOINT_NU = "/v2/natural/nutrients"
API_ENDPOINT_EX = "/v2/natural/exercise"

date = datetime.datetime.now()
now = date.strftime("%d/%m/%Y")
print(now)
exercise_text = input("Tell me which exercises you did")
header = {
    "x-app-id": ID_API,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=f"{HOST_DOMAIN}{API_ENDPOINT_EX}", json=parameters, headers=header)
result = response.json()
print(result)
# Add in Google Sheet
API_ENDPOINT_GOO = "https://api.sheety.co/2dca21823908887c01943074c5fd238c/myWorkout/workout"

header_google = {
    'Authorization': "Basic c2FtdWthOkFhMTIzYWJjZGVA"
}
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(API_ENDPOINT_GOO, json=sheet_inputs, headers=header_google)

    print(sheet_response.text)
