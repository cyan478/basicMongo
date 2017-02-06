import csv, pprint
from pymongo import MongoClient

server = MongoClient('149.89.150.100')

db = server.celharry

db.students.drop()

students = db.students


peeps = open("peeps.csv") 
peepdict = csv.DictReader(peeps)

for student in peepdict:
    info = {}
    info['name'] = student['name']
    info['id'] = student['id']
    info['age'] = student['age']
    courses = {}

    cours = open("courses.csv") 
    
    coursedict = csv.DictReader(cours)    

    for key in coursedict:
        print(student['id'])

        print(key['id'])
        if student['id'] == key['id']:
            courses[key['code']] = key['mark']
            
    info['courses'] = courses
    
    students.insert_one(info)

for student in students.find():
    pprint.pprint(student)
