import json
# with open(r'C:\Users\RaghulRamesh\OneDrive\Documents\data\sample.json','r') as jf:
#     data=json.load(jf)
# for x in data['people'][0].keys():
#     print(x + " ===> "+ str(data['people'][0][x] ))

info={
    'Name':'Raghul Ramesh',
    'City':'Chennai',
    'Tech':['Python','AIML','AWS'],
    'Manager': False,
    'Salary':None
}

with open('trainer_info.json','w') as wjf:
    json.dump(info,wjf)