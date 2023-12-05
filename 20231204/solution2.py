import re

file = open('input.txt', 'r')
lines = file.readlines()
card_details = []
card_dups = []
summary = {}


def parse_numbers(cd):
    winning_numbers, my_numbers = cd.split('|')
    winning_numbers = [num.strip() for num in winning_numbers.split(' ') if len(num.strip())>0]
    my_numbers = [num.strip() for num in my_numbers.split(' ') if len(num.strip())>0]
    return winning_numbers, my_numbers

def add_dups(cnt, start):
    print(cnt, start)
    for i in range(start, start+cnt+1):
        print(i)
        card_dups.append(i)
    return

for line in lines:
    print(line)
    line_info = {}
    card_number, card_details = line.split(':')
    card_number = int(re.sub("[^0-9]", "", card_number))
    print(card_number)
    winning_numbers, my_numbers = parse_numbers(card_details) 
    winners = [value for value in my_numbers if value in winning_numbers]
    cnt_winners = len(winners)
    # add_dups(cnt_winners, card_number)
    summary[card_number]=cnt_winners

    """
    What is needed
    For each card, how many winners, duplicate n+1 + winner count cards

    """

# process all the items in card_dups
for k, v in summary.items():
     add_dups(v, k)

add_dups_orig = card_dups.copy()
for item in add_dups_orig:
    add_dups(summary[item], item)

print(card_dups)
print(len(card_dups))
print(summary)