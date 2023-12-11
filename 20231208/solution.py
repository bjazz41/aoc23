
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

        
final_step = 'AAA'
step_count = 0
call_count = 0
while (1==1):
    final_step, steps = follow_instructions(final_step)
    step_count += steps
    call_count += 1
    if final_step == 'ZZZ': break


print('ZZZ finally reached after', step_count, 'steps!...and', call_count, 'times through the instructions!')

