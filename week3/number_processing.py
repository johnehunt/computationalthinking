print('Start')

done_flag = False

total = 0
while not done_flag:
    num = int(input('Please input an integer: '))

    if num > 0:
        total = total + num
    else:
        done_flag = True

print('Total: ', total)

print('Stop')
