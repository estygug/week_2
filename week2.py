import re
import sys
game= input("enter game input")
def checkWinner(game):
    if re.search(r'(x)...\1...\1',game):
        print("The is a winner :x")
    if re.search(r'.(x)..\1..\1.',game):
        print("The is a winner :x")
    if re.search(r'..(x)..\1..\1',game):
        print("The is a winner :x")
    if re.search(r'(x)\1\1......',game):
        print("The is a winner :x")
    if re.search(r'...(x)\1\1...',game):
        print("The is a winner :x")
    if re.search(r'......(x)\1\1',game):
        print("The is a winner :x")
    if re.search(r'(x)..\1..\1..',game):
        print("The is a winner :x")
    if re.search(r'..(x).\1.\1..',game):
        print("The is a winner :x")
    if re.search(r'(o)...\1...\1',game):
        print("The is a winner :o")
    if re.search(r'.(o)..\1..\1.',game):
        print("The is a winner :o")
    if re.search(r'..(o)..\1..\1',game):
        print("The is a winner :o")
    if re.search(r'(o)\1\1......',game):
        print("The is a winner :o")
    if re.search(r'...(o)\1\1...',game):
        print("The is a winner :o")
    if re.search(r'......(o)\1\1',game):
        print("The is a winner :o")
    if re.search(r'(o)..\1..\1..',game):
        print("The is a winner :o")
    if re.search(r'..(o).\1.\1..',game):
        print("The is a winner :o")
    else:
        print("no winner")
checkWinner(game)




