import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'vol_acidity':2, 'alco':9, 'den':6, 'wtype':1, 'chlo':3})

print(r.json())
