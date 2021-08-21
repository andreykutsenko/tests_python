import json
from pprint import pprint

try:
    my_json = json.loads(input())
    pprint(my_json)
except Exception as e:
    print("Некорректный JSON")