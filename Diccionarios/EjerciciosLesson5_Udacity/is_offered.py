#Autor: guilleCM
#coding=utf-8

#from Udacity: Lesson 5
#Enunciado:
# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                		  {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                		  {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# Define a procedure, is_offered(courses, course, hexamester), that returns 
# True if the input course is offered in the input hexamester, and returns 
# False otherwise.

def is_offered(courses, course, hexamester):
	'''coge el hexamester. busca en los valores si aparece el curso.
	Si aparece devuelve True. Sino False.'''
	cursosOfrecidosHexamester=courses[hexamester]
	if course in cursosOfrecidosHexamester.keys():
		return True
	else:
		return False

#CASOS TEST#
print (is_offered(courses, 'cs101', 'apr2012'))
#>>> True

print (is_offered(courses, 'cs003', 'apr2012'))
#>>> False

print (is_offered(courses, 'cs001', 'jan2044'))
#>>> True

print (is_offered(courses, 'cs253', 'feb2012'))
#>>> False