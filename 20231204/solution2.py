import re

file = open('input.txt', 'r')
lines = file.readlines()
summary = {}
card_count = {}

def parse_numbers(cd):
    winning_numbers, my_numbers = cd.split('|')
    winning_numbers = [num.strip() for num in winning_numbers.split()]
    my_numbers = [num.strip() for num in my_numbers.split()]
    return winning_numbers, my_numbers

def calculate_duplicates(card, wins):
    # print(cnt, start)
    this_card_count = card_count[card]
    for i in range(card+1, card+wins+1):
        print('card_count for ', i, ' = card_count + ', this_card_count)
        card_count[i] += this_card_count
    return

line_index = 0
for line in lines:
    # print(line)
    line_info = {}
    card_number, card_details = line.split(':')
    card_number = int(re.sub("[^0-9]", "", card_number))
    # print(card_number)
    winning_numbers, my_numbers = parse_numbers(card_details) 
    winners = [value for value in my_numbers if value in winning_numbers]
    cnt_winners = len(winners)
    summary[card_number]=cnt_winners
    card_count[card_number]=1
    line_index += 1
    # if line_index > 10:
    #     break
    """
    What is needed
    For each card, how many winners, duplicate n+1 + winner count cards
    """

max_card_number = max([k for k, v in summary.items()])
print('max_card_number: ', max_card_number)

for i in range(1, max_card_number+1):
    calculate_duplicates(i, summary[i])

print('number of scratch cards:', sum(card_count.values())) #23806951
