'''
    Lesson: Boolean Logic
    Author: Joyce Chen
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''

def q1():
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  int1 = int((input("Enter an integer: ")))
  print(int1 != 0)

def q3():
  num1 = float(input("Enter a number: "))
  print(num1 >= 0 and num1 <= 10)

def q4():
  food = input("Input food: ")
  drink = input("Input drink: ")
  print(food != "pizza" or drink != "pop")

def q5():
  int2 = int(input("Enter an integer: "))
  bool1 = int2%2 == 0
  print(f"The integer {int2} is {bool1}.")

#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
