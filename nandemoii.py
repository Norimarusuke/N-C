import requests
API_KEY = "0ea8fd21d3e847189e5b6a088b5f248f"
url = f"https://api.weatherbit.io/v2.0/current?lat=39.68809830869338&lon=141.16449176101054&lang=ja&units=M&key={API_KEY}"
response = requests.get(url)
data = response.json()
print(data)
