#input number
# x = input("Enter the number")
# print(x)


#input string
# x = input("Enter the string: ")
# print(x)

#multiple input at a time
# x,y = input("Enter two Number: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)


# # output formattting
# amount = 10.3423
# print('Amount: ${:.2f}'.format(amount))

''' sep and end operator'''
# end 
# print("hello",end='@')
# print('joshi')

# sep operator
# print("umesh","joshi", 'A',sep='')
# print("umesh","joshi", 'A',sep='-')
# print(10,20,30,sep='/')

'''using f'''
# name = 'umesh'
# age = 20
# print(f"hello i am {name} and i am {age} year old")


'''using % opearor'''
# add = 5+1
# print("Sum: %d"%add)
# print("Sum: %x"%add)

'''input in the list'''
x = input("Enter the numbers seperate by space: ").split()
print(x)

# getting input lin list by using loop

# a = []
# n = int(input("Enter the number want to stroew in the list: "))
# for i in range (n):
#     b = int(input(f'Enter the number {i+1}'))
#     a.append(b)
# print(a)

# geting input in the list using map 
# a = list(map(int,input("Enter the number by using space: ").split()))
# print(a)

'''get input in nested list'''
user_input = [x.split(',') for x in input("Enter nest list seperate by ;: ").split(';')]
print(user_input)
# user_input = [input("Enter the list sperate by coma,: ").split(',')]



