import os
import string
import random

def get_participants():
    return ["Ana", "Bogdan", "Cristian"]

def make_pairs(participants):
    pairs = {}
    number_of_participants = len(participants)
    if (number_of_participants <= 1):
        print("We cannot do Secret Santa! Bring more people!")
        return
    random.shuffle(participants)
    for i in range(number_of_participants):
        pairs[participants[i]] = participants[i+1] if i < number_of_participants-1 else participants[0]
    #print("number of participants = ", len(participants))
    #pairs[participants[len(participants)-1]] = participants[0]
    #print(pairs)
    return pairs
        

print(get_participants())
print(make_pairs(get_participants()))
