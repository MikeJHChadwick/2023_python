import random

print("Hello World")

x= 1
y= 3

print(x+y)

if (x > y):
    print('Y is greater than X.')
else:
    print('X is greater than Y.')


friends= ['sam', 'kevin']
for friend in friends:
    print("outer loop")
    print(friend)
    for letter in friend:
        print("inner loop")
        print(letter)


friends= [['cat', 'dog', 'hippo'], 'kevin']
for friend in friends:
    print("outer loop")
    print(friend)
    for letter in friend:
        print("inner loop")
        print(letter)

# print(x==y)
# print(x<y)
# print(x>y)
# print(x<=y)
# print(id(friends))



# def convert_seconds(seconds):
#     hours= seconds // 3600
#     minutes= (seconds - hours * 3600) // 60
#     remaining_seconds= seconds - hours * 3600 - minutes * 60
#     #print(hours, minutes, remaining_seconds)
#     return(hours, minutes, remaining_seconds)

# return_statement= convert_seconds(5000)
# #print(return_statement)
# hours, minutes, remaining_seconds= convert_seconds(5000)
# print(return_statement)
# print(type(return_statement))

# favorite_number= 9

# print(globals())

# def testing_scope():
#     x= 'cat'
#     y= 'dog'
#     print("My favorite number is "+ str(favorite_number))
#     print(locals())
#     def new_local_scope():
#         z="elephant"
#         print("We are in the new_local_scope")
#         x=150
#         print(x, y, z, favorite_number)
#     new_local_scope()

    
# testing_scope()

def new_func():
    print("new function")