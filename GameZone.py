import json

with open('Project_x.json', 'r') as f:
    data = f.read()
    json_data = json.loads(data)
print(type(json_data))

jsonStr = '[{"a":1, "b":2}, {"c":3, "d":4}]'
aList = json.loads(jsonStr)
print(aList[0]['b'])
