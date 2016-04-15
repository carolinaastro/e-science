#programa 2 do software carpentry

#From 1 to N: Using range, write a loop that uses range to print the first 3 natural numbers: 1,2,3

for a in range(1, 4):
    print(a)	

#Computing powers with loops
#Write a loop that calculates the same result as 5 ** 3 using multiplication (and without exponentiation).

b= 5*5*5
print b

#Reverse a string
#Write a loop that takes a string, and produces a new string with the characters in reverse order, so 'Newton' becomes 'notweN

c = 'Newton'
print c[::-1] #printa tudo na ordem inversa
