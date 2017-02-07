'''
Using python and the database from the previous assignment write a program to do the following:
Compute the average for each student.
Display each students name, id and average.
The points above are not specific steps you need to take in a particular order. You should organize 
the code however you feel will accomplish the task best.

Work with the same people with whom you did Friday's assignment in the same repository.

Do this work in a separate python file
'''

from pymongo import MongoClient

server = MongoClient('127.0.0.1')
#server = MongoClient('149.89.150.100')

db = server.celharry

avg = 0
counter = 0

for student in db.students.find():
	for course in student['courses'].keys():
		grade = student['courses'][course]
		avg += grade
		counter += 1
	avg = avg / counter
	print "Student: " + student['name'] + "\n ID: " + student['id'] + "\n Average: " + avg + "\n"








		