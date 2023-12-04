# read input.txt
# export AOC_SESSION=....
# aocd > input.txt

file = open('input.txt', 'r')
lines = file.readlines()
game_details = []

def add_game(game_dict):
    game_details.append(game_dict)

def check_if_possible(color, num):
    if color == 'red' and num > 12:
        return False
    elif color == 'green' and num > 13:
        return False
    elif color == 'blue' and num > 14:
        return False
    else:
        return True

def set_max_color(max_vals, set_info):
    for k, v in set_info.items():
        if v > max_vals[k]:
            max_vals[k] = v
    return max_vals

def calc_power(max_colors):
    nums = [v for k, v in max_colors.items()]
    result = 1
    for num in nums:
        result = result * num
    return result

def parse_line(line):
    game_number, game_details = line.split(':')
    game_dict = dict()
    game_dict['game_number'] = int(game_number.split(' ')[1])
    sets = game_details.split(';')
    set_list = []
    possible_flag = True
    max_colors = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        set_details = set.split(',')
        set_info = {}
        for item in set_details:
            num, color = item.strip().split(' ')
            set_info[color] = int(num)
            max_colors = set_max_color(max_colors, set_info)
            if possible_flag: 
                possible_flag = check_if_possible(color, set_info[color])
        set_list.append(set_info)
    game_dict['sets'] = set_list
    game_dict['is_possible'] = possible_flag
    game_dict['power'] = calc_power(max_colors)
    game_dict['max_colors'] = max_colors
    add_game(game_dict)
    return

for line in lines:
    parse_line(line)
    
possible_games = [game['game_number'] for game in game_details if game['is_possible']]
sum_of_possible_games = sum(possible_games)
# print(possible_games)
print("sum of possible game numbers:", sum_of_possible_games)
sum_of_powers = sum(game['power'] for game in game_details)
print("sum of powers:", sum_of_powers)