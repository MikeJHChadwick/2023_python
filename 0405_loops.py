def create_user_name(username):
    if len(username) < 5:
        print("Invalid username. Username must be at least 5 chracters long")
    elif len(username) > 15:             
        print("Invalid username. Username must be at least 15 chracters long")
    else:
        print("You have created a valid username")

create_user_name("sammi")


def check_nums(num1, num2):
    if num1 > num2:
        return True
    return False

result= check_nums(10, 3)
print(result)

print(check_nums(3, 10))

def true_or_false(result):
    if result == True:
        print("The result is True")
    if result == False:
        print("The result if False")

true_or_false(result)

return_test= true_or_false(result)
#print(return_test)

if return_test == None:
    print("False statement")
else:
    print("True statement")


#x = 5
# def greater_than_0(num):
#     while num > 0:
#         num -= 1
#         if num == 2:
#             continue
#         print("Not there yet, num=" + str(num)) 
#     print("num=" + str(num))

# greater_than_0(5)


# def to_celcius(x):
#     return(x-32)*5/9

# for x in range(0,101,10):
#     print(x, to_celcius(x))

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

#teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

a = [1, 2]
b = [4,5]

for i in a:
    for j in b:
        print(i, j)

print("Testing 123")

print("Making a change")