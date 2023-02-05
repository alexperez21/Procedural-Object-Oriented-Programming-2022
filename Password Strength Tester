prompt = input("What is your new password?: ")

spcl_char = "()~!@#$%^&*-+=|{}[]:;\"\'<>,.?/"

good = 0
bad = 0

if any(i.isdigit() for i in prompt) != True:
  print("Does not contain any numbers.")
  bad += 1
else:
  pass
  
if any(i.isalpha() for i in prompt) != True:
  print("Does not contain any letters.")
  bad += 1
else: 
  pass
  
if any(not i.isalnum() for i in prompt) != True:
  print("Does not contain any special characters.")
  bad += 1
else:
  pass
  
if len(prompt) < 8:
    print("Not 8 or more characters.")
    bad += 1
else:
  pass

if bad > 0:
  print("Bad password. Failed some of the criteria.")
else:
  print("Good password. Met all criteria.")
  
  
