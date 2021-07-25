# l = [1,2,3,4]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

# import json
# p = '{"name": "Bob", "languages": ["Python", "Java"]}'
#
# d=json.loads(p)
#
# j=json.dumps(d,indent=4)
#
# print(j)
#
# print(type(j))


#C:/my_folder/practice_codes/python/sample.json

import json

with open('/mnt/c/my_folder/practice_codes/python/sample.json') as f:
    data=json.load(f)
print(type(data))
print(data)

# import json
#
# person_dict={"name":"Ian",
# "languages": ["English","Spanish"],
#  "country": "Argentina"
# }
#
# with open('person.txt','w') as json_file:
#     json.dump(person_dict,json_file)



