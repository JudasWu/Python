import random
value1 = 'y'
while value1 != 'n':
    min = 0
    max = 100
    bomb = random.randint(min,max)
    print({bomb})
    value = -1
    while value != bomb:
        value = int(input(f'請猜{min}~{max}的數字:'))
    
        if value < min or value > max:
            continue
        elif value > bomb :
            max=value
        else:
            min = value
    print("爆炸了!!!")
    value1 = input('要不要繼續?(y/n)')
        