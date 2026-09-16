base=float(input("Enter the base: "))
height=float(input("Enter the height: "))

area=0.5*base*height
print("Area of the triangle is: ", area)


word1="python"
word2="dragon"

print(len(word1) != len(word2))
print('on' in word1 and 'on' in word2)

number1=int(input("Enter the first number: "))

if number1 % 2 == 0:
    print(number1, "is an even number.")
else:
    print(number1, "is an odd number.")
