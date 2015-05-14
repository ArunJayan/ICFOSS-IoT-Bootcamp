#strings and texts
#strings : actually string is a group of characters like our name etc.

str1 = "Python"	#string 1
str2 = "ICFOSS IoT Bootcamp" #string 2
print str1
print str2

#to get the lenth of strings we use len()
print len(str1)
print len(str2)

#we can combine two strings like below 
out = str2+" "+str1+" Session"
print out
print len(out)
#slicing ... extracting a portion of string is called slicing
#s[a:b] will show characters s[a] to s[b-1]
print out[1:4]
print out[7:-14]
string = "abcdefgh"

# Two-character substring
two = string[0:2]

# Three-character substring
three = string[0:3]

# Four-character substring
four = string[0:4]

# Five-character substring
five = string[0:5]

print(two)
print(three)
print(four)
print(five)
