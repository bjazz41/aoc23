file = open('input.txt', 'r')
readings = file.readlines()

next_values, prev_values = [], []

def get_diffs(lst):
    answers = []
    my_list = lst[-1]
    for i in range(len(my_list)-1):
        diff = my_list[i+1]-my_list[i]
        answers.append(diff)

    return answers


def get_all_diffs(lst):
    diffs = []
    diffs.append(lst)
    idx = 0
    while (1==1):
        idx += 1
        my_diffs = get_diffs(diffs)
        diffs.append(my_diffs)
        if all(diff==0 for diff in my_diffs):
            return diffs


def find_next_value(diffs):
    
    idx = 0
    for i in reversed(range(len(diffs)-1)):
        # print(i, diffs[i])
        if idx==0:
            next_diff = diffs[i][-1]
        else:
            next_diff = diffs[i][-1] + next_diff
        idx += 1
    
    return next_diff

def find_prev_value(diffs):
    idx = 0
    for i in reversed(range(len(diffs)-1)):
        # print(i, diffs[i])
        if idx==0:
            prev_diff = diffs[i][0]
        else:
            prev_diff = diffs[i][0] - prev_diff
        idx += 1
    
    return prev_diff



for reading in readings:
    lst_readings = [int(i) for i in reading.split()]
    diffs = get_all_diffs(lst_readings)
    next_values.append(find_next_value(diffs))
    prev_values.append(find_prev_value(diffs))


# print(next_values)
print('sum of next values is', sum(next_values))

# print(prev_values)
print('sum of prev values is', sum(prev_values))