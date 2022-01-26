from time import sleep
import os
import mouse

#Keep your PC busy and TEAMS status on.

min = int(input('How many minutes before your status change: '))
while True:
    power = input('Would you like to turn you PC off after the time has passed? [Y/N] ').upper().lstrip()[0]
    if power in 'YN':
        break
    else:
        print('Answer with Yes or No.')
for v in range(0, min):
    sleep(60)
    mouse.wheel(0.008)

if power in 'Y':
    os.system('shutdown /s /t 1')
else:
    print('The End')
