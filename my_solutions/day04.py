text="Coding For All"
split_word=text.split()
print(split_word)


print(text[-3:])

print(text.replace("Coding", "Python"))
print(text)

print(text.startswith("Python"))
print(text)


print(text.endswith("All"))
print(text)

sentence = "You cannot end a sentence with because because because is a conjunction"

print(sentence.find("because"))
print(sentence)

print(sentence.rfind("because"))
print(sentence)


radius=10
pi=3.14
area=pi*radius**2
print(f"The area of a circle with radius {radius} is {area:.2f}")