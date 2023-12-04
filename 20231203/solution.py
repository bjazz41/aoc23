import pandas as pd
import pandasql as ps

file = open('input.txt', 'r')
lines = file.readlines()
rows = []
index = 0
numbers = []
sp_chars = []

def add_item(ix, lc, rc, item):
    item_details = {}
    item_details['row'] = ix
    item_details['left_coord'] = lc
    item_details['right_coord'] = rc
    item_details['value'] = item
    return item_details 

def find_numbers(row, index):
    current_number = ""
    row_index = 0
    for char in row:
        if char.isnumeric():
            if current_number == "":
                left_coord = row_index
            current_number = current_number + char
            if row_index == len(row)-1: # last row
                numbers.append(add_item(index, left_coord, row_index, int(current_number)))
        else:
            if current_number != "":
                numbers.append(add_item(index, left_coord, row_index-1, int(current_number)))
            if not char.isalnum() and char not in ['.', '\n']:
                sp_chars.append(add_item(index, row_index, row_index, char))
            current_number = ""
        row_index = row_index + 1

    return numbers

for line in lines:
    # print(line)
    row = [x for x in line]
    numbers = find_numbers(row, index)
    rows.append(row)
    index = index + 1


def find_eligible_numbers(nums, sc):
    df_numbers = pd.DataFrame(nums)
    df_spchars = pd.DataFrame(sc)
    above = ps.sqldf("select n.*, sc.value as sp_char, 'above' as locale, sc.left_coord sp_char_coord, sc.value as spchar, sc.row as sc_row from df_numbers n join df_spchars sc on n.row=sc.row+1 and sc.left_coord between n.left_coord-1 and n.right_coord+1")
    next = ps.sqldf("select n.*, sc.value as sp_char, 'next' as locale, sc.left_coord sp_char_coord, sc.value as spchar, sc.row as sc_row from df_numbers n join df_spchars sc on n.row=sc.row where sc.left_coord between n.left_coord-1 and n.right_coord+1")
    below = ps.sqldf("select n.*, sc.value as sp_char, 'below' as locale, sc.left_coord sp_char_coord, sc.value as spchar, sc.row as sc_row from df_numbers n join df_spchars sc on n.row=sc.row-1 and sc.left_coord between n.left_coord-1 and n.right_coord+1")

    unified = pd.concat([above, next, below])
    unified_grp = unified.groupby(['row', 'left_coord', 'right_coord', 'value']).agg(locales=('locale', 'unique')).reset_index()

    sc_counts = unified.groupby(['sc_row', 'sp_char_coord']).agg(cnt=('value', 'count'), gear_ratio=('value', 'prod'), adj=('value', 'unique')).reset_index()
    
    gears = sc_counts[sc_counts.cnt==2]
    gears.to_csv("sc_counts.csv", sep=',')
    gear_ratio_sum = gears['gear_ratio'].sum()
    print("gear ratio sum:", gear_ratio_sum)
    unified_grp.to_csv('schematic.csv', sep=',')
    return unified_grp


df_eligible_numbers = find_eligible_numbers(numbers, sp_chars)
sum_part_numbers = df_eligible_numbers['value'].sum()

print("sum of eligible part numbers:", sum_part_numbers)




