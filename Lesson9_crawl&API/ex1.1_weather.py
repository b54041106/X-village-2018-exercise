# import json
# import requests
# api_key = 'bc47e078d2864ef184fd595eb35f1675'
# url = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=' + api_key
# r = requests.get(url)

# r.encoding = 'utf-8' 
# #print(r.text)
# data = json.loads(r.text)
# print(data['num_results'])

import json
import requests
url = 'https://www.metaweather.com/api/location/2306179/2018/7/18/'
data = requests.get(url)
#print(data.text)
weather = json.loads(data.text)
print(type(weather))


with open('weather.txt', 'w+', encoding='utf-8-sig') as g:
    for i in range(len(weather)):
        a=[weather[i]['weather_state_name']]
        b=str(a)
        g.write(b+'\n')
