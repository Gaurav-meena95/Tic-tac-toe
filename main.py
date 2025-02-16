import os

n = 13
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def parteenPrint():
    os.system('clear')
    p = 0
    for i in range(n):
        for j in range(n):
            if i == 4 or i == 8 or j == 4 or j == 8:
                print('*', end=' ')
            elif (j == 2 or j == 6 or j == 10) and (i == 2 or i == 6 or i == 10):
                print(ls[p], end=' ')
                p += 1
            else:
                print(' ', end=' ')
        print()

def verify(x):
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if x not in a:
        return False
    x = int(x)
    if ls[x - 1] == "X" or ls[x - 1] == "O":
        return False
    return True

def update(x, i):
    if i % 2 == 0:
        ls[x - 1] = "X"
    else:
        ls[x - 1] = 'O'

def is_won():
    if ls[0] == ls[1] == ls[2]:
        return True
    elif ls[3] == ls[4] == ls[5]:
        return True
    elif ls[6] == ls[7] == ls[8]:
        return True
    elif ls[0] == ls[3] == ls[6]:
        return True
    elif ls[1] == ls[4] == ls[7]:
        return True
    elif ls[2] == ls[5] == ls[8]:
        return True
    elif ls[0] == ls[4] == ls[8]:
        return True
    elif ls[6] == ls[4] == ls[2]:
        return True
    return False

def is_draw():
    return all(isinstance(x, str) for x in ls) and not is_won()

def print_winner(i):
    if i % 2 == 0:
        print('User 2 won 🎉🎉')
    else:
        print('User 1 won 🎉🎉')

def reset_game():
    global ls
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    while True:
        parteenPrint()
        i = 0
        while i < 9:
            if i % 2 == 0:
                print('User 1 Turn')
            else:
                print('User 2 Turn')
            print('Enter choice (1-9):', end=' ')
            z = input()
            y = verify(z)
            if not y:
                parteenPrint()
                print('Invalid Choice ... Please Try Again!!!!')
                continue
            else:
                update(int(z), i)
                i += 1
                parteenPrint()
                if is_won():
                    print_winner(i)
                    break
                elif is_draw():
                    print("It's a draw! 😞")
                    break
        
        print("Do you want to play again? (y/n): ", end="")
        choice = input().lower()
        if choice != 'y':
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            reset_game()

main()
