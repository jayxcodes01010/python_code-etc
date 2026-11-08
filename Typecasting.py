#Typecasting is the process of converting a variable from one data type to another
# str(), float(), int(), bool()

name = "Jayanshu"
age = 24
gpa = 4.6
is_student = True

print(type(name))#To identify and print the type of data stored in variable (bool, int, etc)

gpa = int(gpa)# for converting float to whole number or integer (int)
print(gpa)

age = float(age)# for converting whole number to decimal point
print(age)

name = bool(name)# for converting string to boolean (interesting result when ran), and if strings are wmpty it returns the value of false
print(name)