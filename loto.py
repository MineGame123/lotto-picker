import random
k=True
while k==True:
        loto = random.sample(range(0, 9), k=7)
        print("Your numbers:")
        numerele: list = list(map(int, input().split()))
        rez = list(zip(loto, numerele))
        print(f'Winning numbers: {" ".join([str(i) for i in loto])}')
        print(f'Your\'s choices : {" ".join([str(i) for i in numerele])}')
        print(' \n ----------- Results ----------- ')
        pct = 0
        for lot, aleg in rez:
            if lot == aleg:
                print(f'{lot} & {aleg} - match! {chr(10004)}')
                pct += 1
            else:
                print(f'{lot} & {aleg} - wrong! {chr(10005)}')
        print('\nYour score:', pct)
        option = input("Try again?(y/n)")
        if option == 'n' or 'no':
            K=False
if k == False:
    exit()
        