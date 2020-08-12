
import fastjsonschema
import json
import os

filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)

with open("D:\\20_Forschung\\20_AIMFREE\\10_MQTT\\aimfree_models\\workshop\\product_schema.json", "r") as moschema:
    schema = json.load(moschema)
with open("D:\\20_Forschung\\20_AIMFREE\\10_MQTT\\aimfree_models\\workshop\\validation_json.json", "r") as morojson:
    json = json.load(morojson)


fastjsonschema.validate(schema,json)