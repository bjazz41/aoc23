import re

def process(ix, input_start, input_end):
    print('process', ix, input_start, input_end)
    for src_st, src_end, dest in converter_ranges[ix]:
        print('src_start', src_st, src_end, dest)
        if src_st <= input_start < src_end:
            if input_end < src_end:
                new_start, new_end = input_start - src_st + dest, input_end - src_st + dest
                return new_start if ix == 6 else process(ix+1, new_start, new_end)
            else:
                return min(process(ix, input_start, src_end-1), process(ix, src_end, input_end))
    return input_start if ix==6 else process(ix+1, input_start, input_end)

def return_map(mapping, n=3):
    for i in range(0, len(mapping), n):
        yield(mapping[i:i+n])

with open('input.txt') as f:
    p = f.read().split('\n\n')

numbers = [list(map(int, re.findall('\d+', part))) for part in p]
seeds, converters = numbers[0], numbers[1:]

converter_ranges = [[] for _ in range(7)]
for ix, conv in enumerate(converters):
    for dest, src, length in return_map(conv, 3):
        converter_ranges[ix].append([src, src + length, dest])


process_output = [process(0,  item[0], item[0]+item[1]) for item in return_map(seeds, 2)]
print(process_output)
print('Lowest location is', min(process_output))

# print(converter_ranges)