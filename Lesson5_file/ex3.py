import json
with open('band.json','r',encoding='utf-8-sig') as f:
    detail = json.load(f)
    print(json.dumps(detail,ensure_ascii=False,indent=4))
    
# #Method_2:loads&pprint
# from urllib.request import urlopen
# import json
# u = urlopen('http://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5')
# resp = json.loads(u.read().decode('utf-8'))
# from pprint import pprint
# pprint(resp)