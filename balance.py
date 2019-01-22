a = float(raw_input('What is the market value of your Canadian Index holding? '))
b = float(raw_input('What is the market value of your US Index holding? '))
c = float(raw_input('What is the market value of your Canadian Bond Index holding? '))
d = float(raw_input('What is the market value of your International Index holding? '))

depositing = float(raw_input('How much are you depositing? '))

current_total = a + b + c + d
desired_total = current_total + depositing

desired_per = float(desired_total / 4)

print('You want ${} per fund'.format(desired_per))
print('That means deposit the following... ')

print('- ${} into canadian index'.format(int(desired_per - a)))
print('- ${} into us index'.format(int(desired_per - b)))
print('- ${} into canadian bond index'.format(int(desired_per - c)))
print('- ${} into international index'.format(int(desired_per - d)))
