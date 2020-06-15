from Block import Block
from os import listdir
from os.path import isfile, join
import os

def save_block(b):
    values = [b.name, b.mhp, b.chp, b.thp, b.xp, b.cp]
    for i in b.blips:
        values.append(i.name)
        values.append(i.max_value)
        values.append(i.curr_value)
    mypath = os.path.abspath(os.getcwd())
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if b.name in onlyfiles:
        print("Character already exists! Overwrite? (Y/N)")
        ans = input("@>>").upper()
        if ans == "Y":
            with open(b.name, 'w+') as f:
                for i in values:
                    f.write(str(i) + '\n')

def load_block(nm):
    file = open(nm, 'r').readlines()
    newchar = Block(file[0], int(file[1]), int(file[2]), int(file[3]), int(file[4]), int(file[5]))
    for i in range(6, len(file), 3):
        newchar.add_blip(file[i], file[i + 1], file[i + 2])
    return newchar

def tick_down(blip):
    for i in adventurer.blips:
        if i.name == cmd_args[1]:
            i.tick(False)
            break
    print("!!!Blip not found!!!")

def tick_up(blip):
    for i in adventurer.blips:
        if i.name == cmd_args[1]:
            i.tick(True)
            break
    print("!!!Blip not found!!!")


adventurer = Block('Creed', 32)
while True:
    cmd_args = input("@>>").split()
    if len(cmd_args) < 1:
        continue
    if cmd_args[0] == 'exit':
        break
    if cmd_args[0] == 'save':
        save_block(adventurer)
    if cmd_args[0] == 'load':
        if len(cmd_args) > 1:
            adventurer = load_block(cmd_args[1])
        else:
            mypath = os.path.abspath(os.getcwd())
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            for i in onlyfiles:
                if ".py" in i:
                    onlyfiles.remove(i)
            print(onlyfiles)
    if cmd_args[0] == 'rename':
        if len(cmd_args) > 1:
            adventurer.name = cmd_args[1]
    if cmd_args[0] == 'remove':
        if len(cmd_args) > 1:
            for i in adventurer.blips:
                if i.name == cmd_args[1]:
                    adventurer.blips.remove(i)
    if cmd_args[0] == 'add':
        adventurer.add_blip(cmd_args[1], cmd_args[2], cmd_args[3])
    if cmd_args[0] == 'temp':
        adventurer.thp += int(cmd_args[1])
    if cmd_args[0] == 'tick':
        if len(cmd_args) == 2:
            tick_down(cmd_args[1])
        elif cmd_args[2].lower() == 'up':
            tick_up(cmd_args[1])
        else:
            tick_down(cmd_args[1])
    if cmd_args[0] == 'dmg':
        if adventurer.thp > 0:
            adventurer.thp -= int(cmd_args[1])
            if adventurer.thp < 0:
                adventurer.chp += adventurer.thp
                adventurer.thp = 0
        else:
            adventurer.chp -= int(cmd_args[1])
    if cmd_args[0] == 'heal':
        adventurer.chp += int(cmd_args[1])
        if adventurer.chp > adventurer.mhp:
            adventurer.chp = adventurer.mhp
    if cmd_args[0] == 'xp':
        adventurer.xp += int(cmd_args[1])
    if cmd_args[0] == 'longrest':
        adventurer.longrest()
    if cmd_args[0] == 'spend' or cmd_args[0] == 'earn':
        if(len(cmd_args)<3):
            print("!!!Include a currency value followed by a type!!!")
        else:
            currency = cmd_args[2].upper()
            amt = int(cmd_args[1])
            if currency == 'PP':
                amt *= 1000
            elif currency == 'GP':
                amt *= 100
            elif currency == 'SP':
                amt *= 10
            elif currency != 'CP':
                print('Unsupported currency')
            if cmd_args[0] == 'spend':
                if adventurer.cp < amt:
                    print('Insufficient Funds!')
                else:
                    adventurer.cp -= amt
                    print('Successful Transaction!')
            else:
                adventurer.cp += amt
                print('Successful Transaction!')
    if cmd_args[0] == 'help':
        print("Oops! Will didn't write this yet!")
    adventurer.display()





