from math import gcd

with open('input.txt') as f:
    p = f.read().split('\n\n')

instructions, nodes = p


def get_clean_nodes():
    clean_nodes = {}
    for item in nodes.splitlines():
        key, value = item.split(' = ') 
        tpl = value.strip().replace('(', '')
        tpl = tpl.replace(')', '')
        tpl = tpl.split(', ')
        clean_nodes[key.strip()]=tuple(tpl)
    return clean_nodes


def parse_nodes(next_node, step, clean_nodes):
    direction = 0 if step == 'L' else 1
    return clean_nodes[next_node][direction]
    

# follow instructions
def follow_instructions(next_node='AAA'):
    clean_nodes = get_clean_nodes()
    count = 0
    for step in instructions:
        next_node = parse_nodes(next_node, step, clean_nodes)
        count += 1
        if next_node == 'ZZZ': break
    return next_node, count

        
def find_nodes(clean_nodes, ends_with):
    return [k for k in clean_nodes.keys() if k.endswith(ends_with)]


def get_lcm(lst_nums):
    lcm = 1
    for i in lst_nums:
        lcm = lcm*i//gcd(lcm, i)    
    print(lcm)
    return lcm

clean_nodes = get_clean_nodes()
initial_steps = find_nodes(clean_nodes, 'A')

step_counts = {}
call_count = 0

for initial_step in initial_steps:
    final_step = initial_step
    step_counts[initial_step] = 0
    while (1==1):
        final_step, steps = follow_instructions(final_step)
        step_counts[initial_step] += steps
        call_count += 1
        if final_step.endswith('Z'): break

print(step_counts)

lcm = get_lcm([v for k, v in step_counts.items()])


# print('ZZZ finally reached after', step_count, 'steps!...and', call_count, 'times through the instructions!')

