s1 = {'Blue', 'Black', 'Green'}
s2 = {'Red', 'Black', 'Yellow', 'Blue', 'Brown'}
print('Add them all: {}'.format(s1 | s2))
print('In s1 and s2: {}'.format(s1 & s2))
print('In s1, not in s2: {}'.format(s1 - s2))
print('In s1, not in s2 AND in s2, not in s1: {}'.format(s1 ^ s2))