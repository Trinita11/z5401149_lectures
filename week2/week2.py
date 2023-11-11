print("John said \"Let's go to a cafe\"")

a = 8.2+0.2+0.2
print(a)

6/2

1 == 2

a="trinita"
x = str.upper(a)
print(x)

x=a.upper()

print(x)


a = True
b = 5

print("The value of a is a and the value of b is b")

a = True
b = 5

print(f"The value of a is {a} and the value of b is {b}")
print("The value of a is {} and the value of b is {}".format(a,b))




l = 56
w = 33
h = 30.5
volume = l*w*h
print(f"the volume of this box is {volume}")

lst = []
lst=["Second", 1, "Third"]
print(lst[2])  #indexing
print(lst[0:2])  #slicing


lst.append(2)
print(lst)


line = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)


a = 1 + 2 # Addition
# Division follows
b = 3 / 5
# c = 2**5 # Exponentiation



x = 1.0
print(x)

#assignment
x="2023-02-06"
y=36.8
print("the exam date is{} and you'll have {} minutes".format(x,y))

w = "What"
i = "IS"
c = "CamelCase?"

print(f'{w} {i} {c}')
print('{} {} {}'.format(w, i, c).lower())

print('{} {} {}'.format(w, i.lower, c))

import yfinance as yf





dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic1)
print(dic0['a'])




dic = { ('a', 'b'): 1, 'c': 2, }
print(dic)


l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
m = l[2:10]
print(m)

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[-7:12])

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(l[1:4])
print(l[-8:-6])

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[:-5])

(b,s,i )= (True, 'string', 1)
print(b,s,i)

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
print(sol)

sol.remove('bad')
print(sol)

sol.append("including")
print(sol)

sol.insert(2, 'good')
print(sol)

sol.extend(list_b)
print(sol)