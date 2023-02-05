lyrics = ["Baby Shark", "Mommy Shark", "Daddy Shark", "Grandma Shark", "Grandpa Shark", "Let's go hunt", "Run away", "Safe at last", "It's the end"]
doo = "doo"

for i in range(len(lyrics)):
  print(((lyrics[i] + ' ' + (doo + ' ') * 6 + '\n')*3) + lyrics[i] + '\n')
  i += 1
        
