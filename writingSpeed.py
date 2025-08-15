import random
import os
import time as t

print("Test Your typing Speed...")

#Basically it Says if the os is windows then cls else clear
os.system('cls' if os.name == 'nt' else 'clear')

l1 = []

with open("Words.txt") as f:
    for i in f:
        i1 = i.strip("\n")
        l1.append(i1)

options = random.sample(l1,5)
print(options) 
s = t.time()
user_input = input("Here Type the each word By giving space :")
st = t.time()
time_taken  = st-s

length = len(user_input.split())
wpm = length/time_taken*60

print("Your WPM is :",int(wpm))




    



    

