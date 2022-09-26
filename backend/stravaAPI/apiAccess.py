import requests

statsUrl = "https://www.strava.com/api/v3/athletes/53662785/stats"

header = {'Authorization': 'Bearer ' + "3c6a91ad79c96c6e514baa64e4b209156f23ed63"}
param = {'per_page': 200, 'page': 1}
myDataset = requests.get(statsUrl, headers=header, params=param).json()
print(myDataset)
