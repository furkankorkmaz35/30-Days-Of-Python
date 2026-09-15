"""
first_name="Furkan"
last_name="Korkmaz"
country="Turkey"
city="Izmir"
age=20
is_married=False
skills=["Python","HTML","C"]
person_info={
    "first_name":"Furkan",
    "last_name":"Korkmaz",
    "country":"Turkey",
    "city":"Izmir"
}

print("First name:",first_name)
print("First name length:",len(first_name))
print("Last name:",last_name)
print("Last name length:",len(last_name))
print("Country:",country)
print("City:",city)
print("Age:",age)
print("Married:",is_married)
print("Skills:",skills)
print("Person information:",person_info)

first_name,last_name,country,age,is_married="Faruk","Korkmaz","Izmir",20,False

print(first_name,last_name,country,age,is_married)


radius=30
pi=3.14
area=pi*radius**2
circumference=2*pi*radius

print("Area of circle:",area)
print("Circumference of circle:",circumference)

from numpy import pi


radius=float(input("Enter the radius of the circle: "))

area=pi*radius**2
circumference=2*pi*radius
print("Area of circle:",area)
print("Circumference of circle:",circumference)"""

num1=5
num2=4
total=num1+num2
print("Total:",total)
diff=num1-num2
print("Difference:",diff)
product=num1*num2
print("Product:",product)
exp=num1**num2
list=[5, 4, 12, 3, 9]
print("Minimum value in the list:", min(list))
print("Maximum value in the list:", max(list))
print("Sum of the list:", sum(list))