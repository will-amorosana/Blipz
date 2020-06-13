from blip import Blip
from Block import Block

def save_block(b):
    values = [b.name, b.chp, b.mhp, b.thp, b.xp, b.cp]
    for i in b.blips:
        values.append(i.name)
        values.append(i.max_value)
        values.append(i.curr_value)
    with open(b.name, 'r') as f:
        for i in values:
            f.write(i + '\n')

def load_block(nm):
    values = []
    with open(nm, r) as f:
        

adventurer = Block('Creed', 31)
while True:
    cmd_args = input("@>>").split()
    if cmd_args[0] == 'save':
        save_block(adventurer)


    if cmd_args[0] == 'load':
        if cmd_args.len > 1:
            with open(cmd_args[1]) as f:
                read_file = f.read()


    if cmd_args[0] == 'exit':
        break
    if cmd_args[0] == 'add':
        adventurer.add_blip(cmd_args[1], cmd_args[2], cmd_args[3])
    if cmd_args[0] == 'temp':
        adventurer.thp += cmd_args[1]
    if cmd_args[0] == 'tick':
        for i in adventurer.blips:
            if i.name == cmd_args[1]:
                i.tick()
                break
    if cmd_args[0] == 'dmg':
        if adventurer.thp > 0:
            adventurer.thp -= cmd_args[1]
            if adventurer.thp < 0:
                adventurer.chp += adventurer.thp
                adventurer.thp = 0
        else:
            adventurer.chp -= cmd_args[2]
    if cmd_args[0] == 'heal':
        adventurer.chp += cmd_args[1]
        if adventurer.chp > adventurer.mhp:
            adventurer.chp = adventurer.mhp
    if cmd_args[0] == 'xp':
        adventurer.xp += cmd_args[1]
    if cmd_args[0] == 'longrest':
        adventurer.longrest()
    if cmd_args[0] == 'spend' or cmd_args[0] == 'earn':
        currency = cmd_args[2].upper()
        amt = cmd_args[1]
        if currency == 'PP':
            amt *= 1000
        elif currency == 'GP':
            amt += 100
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
    adventurer.display()





