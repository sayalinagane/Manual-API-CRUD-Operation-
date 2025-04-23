import requests
import json
URL='http://127.0.0.1:4567/api/students'
URL2='http://127.0.0.1:4567/api/students/2'

# read
# data=requests.get(url=URL)
# print(data.json())

# #create

# py_data={
#     'sname':'adi',
#     'rollno':'67',
#     'course':'mech'
# }

# req=requests.post(url=URL,data=json.dumps(py_data))
# print(req.json())

#update put
# py_data={
#     'sname':'sameer',
#     'rollno':'27',
#     'course':'IT'
# }
# req=requests.put(url=URL2,data=json.dumps(py_data))
# print(req.json())

#patch same method put use
# py_data={
#     'sname':'pranay',
   
# }
# req=requests.put(url=URL2,data=json.dumps(py_data))
# print(req.json())

#delete
# res=requests.delete(url=URL2)
# print(res.json())
