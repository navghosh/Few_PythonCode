"""You are camping alone out in the jungle and you hear some animals in the dark nearby.
Based on the noise they make, determine which animals they are.

You are given the noises made by different animals that you can hear in the dark, evaluate each noise to
determine which animal it belongs to. Lions say 'Grr', Tigers say 'Rawr', Snakes say 'Ssss', and
Birds say 'Chirp'.

A string that includes each animal that you hear with a space after each one."""

"""Rawr Chirp Ssss
Tiger Bird Snake"""
animals = {"Grr" : "Lions", "Rawr" : "Tiger", "Chirp" : "Bird", "Ssss" : "Snake"}
noise = (input("enter: "))
noise_lst = noise.split()


answer = ""
for x in noise_lst:
    answer += animals[x] + " "
print(answer)

