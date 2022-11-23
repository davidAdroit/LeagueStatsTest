"""
Class: CS230
Name: Anqi
Description: Strings
"""
'''
print(s[8])
print(s[-4])
print(s[-2])
s = "Hello World!"




# 1. Print every character in “Hello World!” using for loop – with their positions
count = 0
for i in range(0,12):

   # print(s[i])
    count += 1

# 2. Get the third character in “Hello World!”
s[2]
print(s[6:11])
print(s[-9:9])
print(s[2:-9])


# 3. How to get “World” from “Hello World!”?
print(s[6:len(s)])
# 4. How to get “World!” from “Hello World!”?

# 5. How to get “Hello” from “Hello World!”?
print(s[:5])
print(s[:])
# 6. Is “python” in s?
print("python" in s)


'''

'''
Exercise:
Write a Python program to 
1. Ask the user to input a string 
2. Create a new string made of the first two and the last two chars from a given a string. 
3. If the string length is less than two, ask the user to input again until the string length is greater than two.
4. Show the new string.

'''

'''
string = input("Please enter a string : "))
while len(string) <=2:
    string = input("Enter a new string: "))
else:
    newString = string[:2] + string[len(string)-2:]
    print(newString)
'''









# 7. How to print “hello world!” using s?
s = "Hello World"
print(s.upper())


# 8. How to split s?
print(s.split("o"))
file_name = "text.txt"

print(file_name.split(".")[-1])
# 9. How to get “Hi World!” from s?
print(s.replace("Hello", "Hi"))
print(s.replace("o", ""))
print(s.replace(" ", " , "))

s_dul = "!!!! HELLO WORLD !!!!"


# 10. How to get “Hello,World!” from s?


# 11. How to get “Hello World” from s?
s2 = "!!!! HELLO WORLD !!!!"
print(s2.strip("!"))
s1 = "           I love python !          "
print(s1.lstrip("!"))
print(s2 ==s_dul)
# 12. What is s now? Print "The string is changed" is s is change.




"""
Exercise:
Write a program for the computer selection, 
enter the word "mac" for Mac, 
and enter "windows" for Windows.
The input can be upper or lower cases, e.g. "mAc" or "WinDows" both works.
It should able to handle simple input errors, such as spaces before, after or inside the input
e.g., "  M ac" is for Mac.
Ask to re-enter if the input is not mac or windows

Sample output 1:
Please enter your choice, Mac or Windows? hgra
Please enter your choice, Mac or Windows? asda
Please enter your choice, Mac or Windows? we
Please enter your choice, Mac or Windows?     winDows
You choose a Windows!

Sample output 2:
Please enter your choice, Mac or Windows? ioqt
Please enter your choice, Mac or Windows? kag
Please enter your choice, Mac or Windows? MAC
You choose a Mac!

"""

