students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},    #[0]
         {'first_name' : 'John', 'last_name' : 'Rosales'},      #[1]
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},      #[2]
         {'first_name' : 'KB', 'last_name' : 'Tonel'}           #[3]
    ]


#2
def iterateDictionary(students):
    for index in range (len(students)):
        print(students[index])
print(iterateDictionary(students))


#bonus
def bonus(students):
    for index in range(len(students)):
        print('first_name -', students[index]['first_name'], ',', 'last_name -', students[index]['last_name'])
bonus(students)


#3
def iterateDictionary2(students):
    for index in range(len(students)):
        print(students[index]['first_name'])
print(iterateDictionary2(students))


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


#4
def printInfo(dojo):
    print(len(dojo['locations']), 'LOCATIONS')
    for location in dojo['locations']:
        print(location)
    print()
    print(len(dojo['instructors']), 'INSTRUCTORS')
    for instructor in dojo['instructors']:
        print(instructor)
printInfo(dojo)