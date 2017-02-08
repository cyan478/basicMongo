from pymongo import MongoClient

#server = MongoClient('127.0.0.1')
server = MongoClient('149.89.150.100')

db = server.celharry

db.teachers.drop()

students = db.students
teachers = db.teachers

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