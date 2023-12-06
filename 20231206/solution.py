file = open('input.txt', 'r')
lines = file.readlines()
inputs = {}

for line in lines:
    topic, values = line.split(':')
    inputs[topic]=values.split()

games = [[int(inputs['Time'][i]), int(inputs['Distance'][i])] for i in range(len(inputs['Time']))]
part2_games = [int(''.join(inputs['Time'])), int(''.join(inputs['Distance']))]
# debug
# print(part2_games)


def get_outcomes(race):
    record_outcomes = []
    time, record_distance = race
    for t in range(0, race[0]):
        d = (time - t)*t
        # debug
        # print('for t=', t, ' distance =', d)
        if d > record_distance: 
            record_outcomes.append(t)
    return record_outcomes

def multiply_list(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result


wayset = [get_outcomes(game) for game in games]
waycounts = [len(way) for way in wayset]
answer = multiply_list(waycounts)
print('The answer is', answer)

# debug
# for ways in wayset:
#     print('there are', len(ways), 'ways to beat the record in game they are', ways, 'seconds')


def find_first_last_winner(race, first=True):
    time, record = race
    start = int(time/2)
    winners = []
    while (1==1):
        d = (time-start)*start
        # debug
        # print('d=',d,'record=',record,'time=',time,'start=',start)
        if d > record:
            winners.append(start)
            start = start - 1 if first else start + 1
        else:
            break
    return start # first failing time


part2_range_start = find_first_last_winner(part2_games, True)
part2_range_end = find_first_last_winner(part2_games, False)

# debug
# print(part2_range_start, part2_range_end, (part2_range_end-1)-(part2_range_start+1))

print('part 2 answer =', (part2_range_end-1)-(part2_range_start+1)+1)
