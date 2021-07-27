import json
with open("./train-v2.0.json", "r", encoding="utf-8") as file:
    jasonobj = file.read()
    jasonobj = json.loads(jasonobj)
    print(jasonobj.keys())