#String Practice
import random

name = "Jaylen"
print(name[1])

print(name[0])

text = "Random string with a lot of characters"
print()

#can access a slice of a string

color ="Orange"
print(color[1:4])


#python understands -1 , in relation to indexing, means to iterate until the last character which is ommited.
#using slicing and [:-1] means to just iterate the last character
#
fruits="Apple"
print(fruits[1:])
print(fruits[2:4]) #the last index is where it stops so this prints pl
fruits2="Orange"
print(fruits2[2:-1])


#string in python are immuttatble
message="A kong string with a silly typo"

new_message=message[0:2]+"l"+message[3:]
print(new_message)

pets="Cats & Dogs"
print(pets.index("&"))
print(pets.index("s"))


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_domain("mjh.chadwick@gmail.com", "gmail.com", "aol.com"))


word="Apple Orange & Others"
print(word.index("Others"))

word2="mountains"
print(word2.upper())

print("legos".upper())

print(word.replace("Apple", "Watermelon"))


name3 = "Manny"
number=len(name3)*3
print("Hello {}, your lucky number is {}".format(name3, number))
#print("your lucky number is {number} Hello {name3}, ".format())


price = 7.5
with_tax = price * 1.89
print("Price: ${:.2f},  With Tax: ${:.2f}".format(price, with_tax))

name2="John"
print("{:^15s} is the ".format(name2))


'''
a built in function is not associated with a class object (print)
funcions that we define that dont rely on a specific object(standalone)
methods, the only thing that makes it a method instead of a function is that its associated with a class (ie .format)
methods belong to class and functions are independent.
'''

