
import fastjsonschema
import json
import os

filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)

with open("D:\\50_Forschung\\01_Aimfree\\8_Code\\Beschreibungsmodell\\Part_type.json", "r") as moschema:
    schema = json.load(moschema)
with open("D:\\50_Forschung\\01_Aimfree\\8_Code\\Beschreibungsmodell\\validation_json.json", "r") as morojson:
    json = json.load(morojson)


fastjsonschema.validate(schema,json)