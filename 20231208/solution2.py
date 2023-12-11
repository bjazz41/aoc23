
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


def parse_node_vector(next_nodes, step, clean_nodes):
    direction = 0 if step == 'L' else 1
    return [clean_nodes[next_node][direction] for next_node in next_nodes]
    

# follow instructions
def follow_instructions(clean_nodes, next_nodes=['AAA']):
    count, finish = 0, False
    for step in instructions:
        # print('starting at', next_nodes)
        next_nodes = parse_node_vector(next_nodes, step, clean_nodes)
        # print('ending at', next_nodes)
        count += 1
        if all(node.endswith('Z') for node in next_nodes): 
            finish = True
            break
    return next_nodes, count, finish

def find_nodes(clean_nodes, ends_with):
    return [k for k in clean_nodes.keys() if k.endswith(ends_with)]


clean_nodes = get_clean_nodes()
final_steps = find_nodes(clean_nodes, 'A')
print(final_steps)
step_count = 0
call_count = 0
while (1==1):
    final_steps, steps, finish = follow_instructions(clean_nodes, final_steps)
    step_count += steps
    call_count += 1
    if finish: break

print(final_steps)
print('All Zs finally reached after', step_count, 'steps!...and', call_count, 'times through the instructions!')



