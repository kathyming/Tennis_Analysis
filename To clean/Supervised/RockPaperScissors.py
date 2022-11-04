#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:36:05 2021

@author: FouadZ
"""

print('Rock Paper Scissors.. Can you beat me?')
def main():
    import random
    possible_actions=['rock','paper','scissors']
    rand = random.choice(possible_actions)
    choice = input('Enter rock or paper or scissors:\n').lower()
    if rand==choice:
        print('I chose ', choice, ' too... ITS A DRAW!')
        main()
    elif choice not in possible_actions:
        print('Please choose a VALID option')
        main()
    elif rand == "rock" and choice == "paper":
        print('I chose rock! You win')
    elif rand == "rock" and choice == "scissors":
        print('I chose rock! I win')
    elif rand == "paper" and choice == "rock":
        print('I chose paper! I win')
    elif rand == "paper" and choice == "scissors":
        print('I chose paper! You win')
    elif rand == "scissors" and choice == "paper":
        print('I chose scissors! I win')
    elif rand == "scissors" and choice == "rock":
        print('I chose scissors! You win')
main()
while True:
    again = input('Do you want to play agani? Yes / No\n').lower()
    if again == "yes":
        main()
    elif again == "no":
        print('Bye')
        quit()
        