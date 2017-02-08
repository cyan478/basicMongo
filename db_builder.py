import csv, pprint
from pymongo import MongoClient

#server = MongoClient('127.0.0.1')
server = MongoClient('149.89.150.100')

db = server.celharry

db.students.drop()


students = db.students

#============================================= STUDENTS
peeps = open("peeps.csv") 
peepdict = csv.DictReader(peeps)

for student in peepdict:
    info = {}
    info['name'] = student['name']
    info['id'] = student['id']
    info['age'] = student['age']
    courses = []

    cours = open("courses.csv") 
    
    coursedict = csv.DictReader(cours)    

    for key in coursedict:
        x = {}
        #print(student['id'])

        #print(key['id'])
        if student['id'] == key['id']:
            x['code'] = key['code']
            x['mark'] = key['mark']
        courses.append(x)
            
    info['courses'] = courses
    
    students.insert_one(info)
'''
for student in students.find():
    pprint.pprint(student)
'''



 

