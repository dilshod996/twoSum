import random
def twoSum():
  
  numbers = [int(numbers) for numbers in input("Enter multiple value: ").split(",")]
  print("Number of list is: ", numbers)
  target1 = random.choice(numbers)
  target2 = random.choice(numbers)
  
  total_target = target1 + target2
  one = numbers.index(target1)
  two = numbers.index(target2)
  if one>two:
    result = [two, one]
  else:  
    result = [one, two]
  print(total_target)
  print(result)
twoSum()  
