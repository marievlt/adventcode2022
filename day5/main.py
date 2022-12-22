#!/usr/bin/env python3

#--- Day 5: Supply Stacks ---
#The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.
#
#The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.
#
#The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.
#
#They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:
#
#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 
#
#move 1 from 2 to 1
#move 3 from 1 to 3
#move 2 from 2 to 1
#move 1 from 1 to 2
#In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.
#
#Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:
#
#[D]        
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 
#In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:
#
#        [Z]
#        [N]
#    [C] [D]
#    [M] [P]
# 1   2   3
#Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:
#
#        [Z]
#        [N]
#[M]     [D]
#[C]     [P]
# 1   2   3
#Finally, one crate is moved from stack 1 to stack 2:
#
#        [Z]
#        [N]
#        [D]
#[C] [M] [P]
# 1   2   3
#The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
#
#After the rearrangement procedure completes, what crate ends up on top of each stack?

#--- Part Two ---
#As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.
#
#Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
#
#The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.
#
#Again considering the example above, the crates begin in the same configuration:
#
#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 
#Moving a single crate from stack 2 to stack 1 behaves the same as before:
#
#[D]        
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 
#However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:
#
#        [D]
#        [N]
#    [C] [Z]
#    [M] [P]
# 1   2   3
#Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:
#
#        [D]
#        [N]
#[C]     [Z]
#[M]     [P]
# 1   2   3
#Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:
#
#        [D]
#        [N]
#        [Z]
#[M] [C] [P]
# 1   2   3
#In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
#
#Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    col      = 0
    row      = 0
    inst_idx = 0
    
    for i in range (len(lines)):
        if lines[i] in ['\n', '\r\n']:
            col = int(lines[i-1].strip().split()[-1])
            row = i-1
            inst_idx = i+1
            break;

    print (col, row)
    crates = create_crates(lines, col, row)
    crates = rearrange_crates_part2(lines[inst_idx:], crates)
    print (crates)
    message = get_message(crates)
    print (message)


def create_crates(lines, col, row):
    crates = []
    for i in range (col):
        crate = []
        for j in range (row-1, -1, -1):
            item = lines[j][i*4+1]
            if item not in [' ', '\t', '\r']:
                crate.append(item)
        crates.append(crate)
    return crates

def rearrange_crates_part1(instructions, crates):
    for inst in instructions:
        inst   = inst.strip().split()
        size   = int(inst[1])
        source = int(inst[3])-1
        dest   = int(inst[5])-1

        for i in range (size):
            tp = crates[source].pop()
            crates[dest].append(tp)

    return crates

def rearrange_crates_part2(instructions, crates):
    for inst in instructions:
        inst   = inst.strip().split()
        size   = int(inst[1])
        source = int(inst[3])-1
        dest   = int(inst[5])-1

        tp = []
        for i in range (size):
            tp.append(crates[source].pop())
        for i in range (size):
            crates[dest].append(tp.pop())

    return crates

def get_message(crates):
    message = ''
    for i in range(len(crates)):
        message = message + crates[i].pop()

    return message


main()
