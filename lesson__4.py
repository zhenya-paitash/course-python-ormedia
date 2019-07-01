import random as r

score = int(input('Enter the number of attempts that you need ... '))  # сколько попыток тебе дать?
num = r.randint(1, 100)  # загаданное число
guesses = 0  # текущее кол-во попыток

while guesses < score:
    guess = int(input('Enter a number from 1 to 100: '))
    guesses += 1

    if guess < num:
        if num - guess > 10:
            print('Coldly... Too LOW, try again.')
        if num - guess > 5 and num - guess <= 10:
            print('Heat! Too LOW, try again.')
        if num - guess <= 5:
            print('HOT !!! LOW, try again.')
    if guess > num:
        if guess - num > 10:
            print('Coldly... So HIGH, try again.')
        if guess - num > 5 and guess - num <= 10:
            print('Heat! So HIGH, try again.')
        if guess - num <= 5:
            print('HOT !!! HIGH, try again.')
    # разница 11+ чисел = холодно, 6-10 = тепло, 5- = ГОРЯЧО

    if guess == num:
        print('You guessed the number in ' + str(guesses) + ' tries!')
        break
else:
    print('You did not guess the number, it was ' + str(num))

# не уверен в следующей конструкции ...
print('TRY AGAIN ?')
question = str(input('YES / NO ?'))
if question == 'YES' or question == 'yes':
    print('Парень(мб девушка), в этом я еще не разобрался, поэтому просто запусти файл заного :) ')
    print('Boy (maybe girl), I haven’t figured it out yet, so just run the file again :) ')
else:
    print('GAME OVER')
