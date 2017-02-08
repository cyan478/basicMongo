import csv, pprint
from pymongo import MongoClient

#server = MongoClient('127.0.0.1')
server = MongoClient('149.89.150.100')

db = server.celharry

db.students.drop()
db.teachers.drop()

students = db.students
teachers = db.teachers


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
#============================================= TEACHERS
teach = open("teachers.csv")
teachdict = csv.DictReader(teach)

for t in teachdict:
	info = {}
	info['teacher'] = t['teacher']
	info['period'] = t['period']
	info['code'] = t['code']

	stu = []
	code = t['code']
	for s in students.find({'courses.code':code}):
		stu.append(s['id'])

	info['students'] = stu

	teachers.insert_one(info)
'''
for teacher in teachers.find():
    pprint.pprint(teacher)
'''


 

