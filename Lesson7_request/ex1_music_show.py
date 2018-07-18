import requests
url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
music_show = requests.get(url)
print(music_show.text)
with open('music_show.json', 'w+', encoding='utf-8-sig') as f:
    f.write(music_show.text)


import json
with open('music_show.json','r',encoding='utf-8-sig') as f:
    detail = json.load(f)
    #print(json.dumps(detail,ensure_ascii=False,indent=4))

with open('music.txt', 'w+', encoding='utf-8-sig') as g:
    for i in range(len(detail)):
        a=detail[i]['title']+':'+detail[i]['startDate']+'~'+detail[i]['endDate']+'\n'
        g.write(a)
    