# 1. A Student class. Create a Student class with name and score attributes, 
# and a method is_passing() that returns True if the score is 50 or more.

# Make two students and test them:

class student:
 def __init__(self, name, marks):
    self.name = name
    self.marks = marks

 def is_passing(self):
      if self.marks >= 50:  # noqa: SIM103
       return True
      else:
       return False

s1 = student("Amna", 72)
s2 = student("Bilal", 41)

print(s1.name, s1.is_passing())  
print(s2.name, s2.is_passing())