import re
# Test by running unit test~

# Part 1
# Write a function to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9). Return true or false. Expected answers shown next to function calls.
def part1(text):
  character = re.compile(r"[^a-zA-Z0-9]")
  text = character.search(text)
  return not bool(text)

print(part1("ABCDEFabcdef123450"))  # True
print(part1("*&%@#!}{"))   # False

# Part 2
# Write a function that matches a string that has an a followed by zero or more b's. Return true or false. Expected answers shown next to function calls.
def part2(text):
  pattern = re.compile("^a(b*)$")
  match = re.search(pattern, text)
  if match:
    return True
  return False
    
print(part2("ac"))  # False
print(part2("abc"))  # False
print(part2("a"))  # True
print(part2("ab"))  # True
print(part2("abb"))  # True

# Part 3
# Write a function to find sequences of lowercase letters joined with a underscore. Return true or false. Expected answers shown next to function calls.
def part3(text):
  checker = re.compile("^[a-z]+_[a-z]+$")
  match = re.search(checker, text)
  if match:
    return True
  return False
print(part3("aab_cbbbc"))  # True
print(part3("aab_Abbbc"))  # False
print(part3("Aaab_abbbc"))  # False

# Part 4
# Write a function that matches a word containing 'z'. Return true or false. Expected answers shown next to function calls.
def part4(text):
  zchecker = re.compile("z")
  match = re.search(zchecker, text)
  if match:
    return True
  return False
    
print(part4("The quick brown fox jumps over the lazy dog."))  # True
print(part4("zebras are cool"))  # True
print(part4("Python Exercises."))  # False
# Part 5
# Write a function that matches a word containing 'z', not at the start or end of the word. Return true or false. Expected answers shown next to function calls.
def part5(text):
  zchecker1 = re.compile("\Bz\B")
  match = re.search(zchecker1, text)
  if match:
    return True 
  return False

print(part5("The quick brown fox jumps over the lazy dog."))  # True
print(part4("zebras are cool"))  # False
print(part5("Python Exercises."))  # False

# Part 6
# Write a function to remove leading zeros from an IP address. Return the updated IP address. Expected answers shown next to function calls.
def part6(text):
  new_ip = ".".join([str(int(i)) for i in text.split(".")])
  return new_ip

print(part6("216.08.094.196"))  # "216.8.94.196"
print(part6("127.02.02.007"))  # "127.2.2.7"

# Part 7
# Write a function to extract the numbers from a given string and sum them together. Return the sum. Expected answers shown next to function calls.
def part7(text):
  sum = 0
  for i in re.findall(("\d+"), text):
    sum += int(i)
  return sum 

print(part7("Ten 10, Twenty 20, Thirty 30"))  # 60
print(part7("There are 8 bears, 2 fish, and 4 turtles."))  # 14
print(part7("10, 10, 30; 24... 42"))  # 116
