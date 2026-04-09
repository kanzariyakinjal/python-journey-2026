course = "python's course for beginners" 
print(course)
# accessing characters
print(course[0])  #p
print(course[-1]) #s

#slicing
print(course[0:3]) #pyt
print(course[1:])  #ython for beginners
print(course[:5])  #pytho

#copy string
another = course[:]
print(another)

#multi-line string
message = """
hi john,
here is our first email to you.
thank you,
the support team
"""
print(message)

      
