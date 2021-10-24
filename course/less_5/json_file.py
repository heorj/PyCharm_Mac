import json
# data = {
#     'number': 0,
#     'boolean' : True,
#     'string': 'string',
#     'none': None,
#     'float': 3.14,
#     'dictionary' : {
#         'key':'value',
#     }
# }
# with open ('dumpk.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

with open ('dump.json') as json_file:
    data = json.load(json_file)
    print(data)

