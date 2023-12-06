import re
import pandas as pd

parts = ['seeds', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
log = []

def load(file):
    with open(file) as f:
        return f.read().split('\n\n')

def return_map(mapping):
    for i in range(0, len(mapping), 3):
        yield(mapping[i:i+3])

def find_soil(seeds, seed_soil_map, ix):
    soil_mappings = []
    for seed in seeds:
        mapping = seed
        for item in return_map(seed_soil_map):
            if seed >= item[1] and seed < item[1]+item[2]:
                mapping = (seed-item[1]+item[0])
                print(parts[ix], seed, 'associated with this', parts[ix+1], item, 'and mapped to', mapping)
                log_info = {"index": ix, "converter": parts[ix]+'_'+parts[ix+1], "input": seed, "output": mapping, "input_start": item[1], "output_start": item[0], "range_step": item[2]}
        if mapping == seed:
            print(parts[ix], seed, 'not associated with any mapping, thus mapped to', parts[ix+1], mapping)
            log_info = {"index": ix, "converter": parts[ix]+'_'+parts[ix+1], "input": seed, "output": mapping, "input_start": "", "output_start": "", "range_step": ""}
        soil_mappings.append(mapping)
        log.append(log_info)
    return soil_mappings

def run(p):
    numbers = [list(map(int, re.findall('\d+', part))) for part in p]

    seeds, converters = numbers[0], numbers[1:]

    output = seeds.copy()
    index = 0
    for mapping in converters:
        output = find_soil(output, mapping, index)
        index += 1

    # print(output)
    print('lowest location = ', min(output))

    df_log = pd.DataFrame(log)
    df_log.to_csv('log.csv', sep=',')

    return

run(load('input.txt'))


# answers: 151676803, 173706076 (had inputs reversed!)
    