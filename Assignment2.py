#Question 1
stg = "Python is a case sensitive language"
print(len(stg))
print(stg[::-1])
print(stg[10:26])
print(stg.replace("a case sensitive","object oriented"))
print(stg.find("a"))
print(stg.replace(" ",""))

#Question 2
name = "ABC"
sid = "2110XXXX"
dep_name = "XYZ"
cg = 9.9
print(f"Hey, {name} here!\n My SID is {sid}\n I am from {dep_name} department and my CGPA is {cg}")

#Question 3
a = 56
b = 10
print(a&b)
print(a|b)
print(a^b)
print(a<<2,b<<2)
print(a>>2,b>>4)

#Question 4
nam = input("Enter ")
x = int(nam.find("name"))
if x>=0:
    print("Yes")

else:
    print("No")

#Question 5
l = int(input("First side = "))
h = int(input("Second side = "))
y = int(input("Third side = "))
t1 = l+h
t2 = l+y
t3 = y+h
xyz = t1>y and t2>h and t3>l
match xyz:
    case True:
        print("Yes")
        exit()
    case False:
        print("No")

#Question 6
o = int(input(" Enter first no = "))
n = int(input(" Enter second no = "))
k = bin(x^n)
q = k.count('1')
print(q)
