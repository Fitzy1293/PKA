timeline = open('new_timeline.txt', 'r').read().splitlines()
with open('for_official_list.txt', 'w+') as f:
    for i in timeline:
        f.write(f'\n\t{i}')
