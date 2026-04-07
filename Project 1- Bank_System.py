#PROJECT
#BANK SYSTEM 

account = {}

def create_account():
    name = input('Enter name: ')
    if name in account:
        print('Account already exists')
    else:
        balance = int(input('Enter amount to create account: '))
        account[name] = {'balance': balance}
        print(f'Welcome {name}')


def deposit():
    name = input('Enter name: ')
    if name in account:
        amount = int(input('Enter deposited amount: '))
        account[name]['balance'] += amount
        print('Balance:', account[name]['balance'])
    else:
        print('Account does not exist')


def withdraw():
    name = input('Enter name: ')
    if name in account:
        amount = int(input('Enter withdrawal amount: '))
        if amount <= account[name]['balance']:
            account[name]['balance'] -= amount
            print('Balance:', account[name]['balance'])
        else:
            print('Insufficient balance')
    else:
        print('Account does not exist')


def transfer():
    sender = input('Sender name: ')
    receiver = input('Receiver name: ')

    if sender in account and receiver in account:
        amount = int(input('Enter transfer amount: '))
        if amount <= account[sender]['balance']:
            account[sender]['balance'] -= amount
            account[receiver]['balance'] += amount
            print('Transfer successful')
        else:
            print('Insufficient balance')
    else:
        print('User not found')


def check_balance():
    name = input('Enter name: ')
    if name in account:
        print('Balance:', account[name]['balance'])
    else:
        print('Account not found')


def main():
    print('WELCOME TO BANK SYSTEM')

    while True:
        print('\n1. Create\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Balance\n6. Exit')

        try:
            choice = int(input('Enter choice (1-6): '))
        except ValueError:
            print('Invalid input')
            continue

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            transfer()
        elif choice == 5:
            check_balance()
        elif choice == 6:
            print('Goodbye!')
            break
        else:
            print('Invalid choice')


main()
