import csv, pprint
from pymongo import MongoClient

server = MongoClient('149.89.150.100')

db = server.celharry

students = db.students

peeps = open("peeps.csv") 
peepdict = csv.DictReader(peeps)

courses = open("courses.csv") 
coursedict = csv.DictReader(courses)


for student in peepdict:
    info = {}
    info['name'] = student['name']
    info['id'] = student['id']
    info['age'] = student['age']
    courses = {}
    
    for item in coursedict:
        print(student['id'])
        print(item['id'])
        if student['id'] == item['id']:
            courses[item['code']] = item['mark']
            
    info['courses'] = courses
    
    students.insert_one(info)

for student in students.find():
    pprint.pprint(student)
