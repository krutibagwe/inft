for i in range(5):
    print (i)
    
for i in range(1,5):
    print(i)
    
for i in range(1,6):
    print(i)

for i in range(1,10,2):
    print(i)

num = [1,2,3,4,5,6,7]
for i in num:
    if i%2==0:
        print(i)

colour=['red', 'green', 'blue']
for index, i in enumerate(colour):
    print(index,i)

name= ['raj', 'suraj', 'deepak']
for index,i in enumerate(name):
    print("The name {} is at location {}.".format(i,index))

name= "kruti"
for index,i in enumerate(name):
    print("The character {} is at location {}.".format(i,index))

countries = {'USA', 'China', 'Turkey'}
for i in countries:
    print(i)
   
countries = {'USA', 'China', 'Turkey'}
for i in countries:
    print(countries[i]) #subscripting not allowed 

countries = ('USA', 'China', 'Turkey')
for i in countries:
    print(i)

countries = ('USA', 'China', 'Turkey')
for index,i in enumerate(countries):
    print("The country {} is at location {}.".format(i,index))

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for i in a_dict:
    print(a_dict[i])

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for items in a_dict.items():
    print(items)
