submarine = {'forward': 0, 'down': 0, 'up': 0}

with open('resources/day2_input.txt') as f:
    data = f.readlines()

# data = ['forward 5\n', 'down 5\n', 'forward 8\n', 'up 3\n', 'down 8\n', 'forward 2\n']

for command in data:
    direction, units = command.strip().split()
    curr = submarine.get(direction)
    submarine.update({direction: curr + int(units)})

print(f"forward: {submarine.get('forward')}, depth: {submarine.get('down') - submarine.get('up')}")
print(submarine.get('forward') * (submarine.get('down') - submarine.get('up')))

submarine = {'forward': 0, 'down': 0, 'up': 0, 'depth': 0}

for command in data:
    direction, units = command.strip().split()
    curr = submarine.get(direction)
    submarine.update({direction: curr + int(units)})
    if direction == 'forward':
        depth = submarine.get('depth')
        aim = submarine.get('down') - submarine.get('up')
        submarine.update({'depth': depth + int(units) * aim})

print(f"forward: {submarine.get('forward')}, depth: {submarine.get('depth')}")
print(submarine.get('forward') * submarine.get('depth'))
