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

# [Double Gold Star] Define a procedure, involved(courses, person), that takes 
# as input a courses structure and a person and returns a Dictionary that 
# describes all the courses the person is involved in.  A person is involved 
# in a course if they are a value for any property for the course.  The output 
# Dictionary should have hexamesters as its keys, and each value should be a 
# list of courses that are offered that hexamester (the courses in the list 
# can be in any order).

def involved(courses, person):
    '''miro cada semestre, miro cada curso, miro el teacher del curso.
    Si el teacher corresponde a la persona, añado el curso a la lista.
    Una vez finalizo el semestre, si la lista no esta vacia se añade al 
    diccionario el semestre como key y la lista como value.
    '''
    resultado={}
    for hexamester in courses:
        cursosOfrecidos=[]
        for curso in courses[hexamester]:
            for detallesCurso in courses[hexamester][curso]:
                if courses[hexamester][curso][detallesCurso]==person:
                    if hexamester in resultado:
                        resultado[hexamester].append(curso)
                    else:
                        resultado[hexamester] = [curso]
    return resultado
    



#CASOS TEST#
print involved(courses, 'Dorina')
#>>> {'jan2044': ['cs001']}

print involved(courses, 'Dave')
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print involved(courses, 'Peter C.')
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

print involved(courses,'Peter')
#>>> {}

print involved(courses, '')
#>>> {}