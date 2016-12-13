a = float(raw_input('canadian index'))
b = float(raw_input('us index'))
c = float(raw_input('canadian bond index'))
d = float(raw_input('international index'))

depositing = float(raw_input('depositing?'))

current_total = a + b + c + d
desired_total = current_total + depositing

desired_per = desired_total / 4

print('You want ${} per fund'.format(desired_per))
print('That means deposit the following... ')

print('- ${} into canadian index'.format(desired_per - a))
print('- ${} into us index'.format(desired_per - b))
print('- ${} into canadian bond index'.format(desired_per - c))
print('- ${} into international index'.format(desired_per - d))
