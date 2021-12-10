import random
  
# Open the file in read mode
while True:
    with open("shrek.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    
        # print random string
        print(random.choice(words))
        a = input()
        if a == '':
            continue