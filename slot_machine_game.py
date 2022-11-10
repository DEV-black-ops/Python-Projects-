import random


MAX_LINES = 3
MAX_BET = 200
MIN_BET= 10

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winning(columns,lines, bet, values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings , winning_lines
    

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end =" | ")
            else:
                print(column[row], end= "")
        print()


def deposit():
    while True:
        amount = input("what would you like to deposite?? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater then 0.')
        else:
            print("please enter a amount.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("enter the no of lines to bet on (1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('lines must be in limits')
        else:
            print("please enter a amount.")
    return lines 

def get_bet():
    while True:
        amount = input("what is the amount you like to bet on each line ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'the bet must be in limits {MIN_BET}- {MAX_BET}')
        else:
            print("please enter a bet.")
    return amount
def spin(balance):
    
    lines = get_number_of_lines()
    while True:
        bet = get_bet()

        total_bet= lines * bet
        if total_bet > balance:
            print(f'you dont have enough to bet the amount, your current balance is {balance} ')
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet: {total_bet}")

    slots= get_slot_machine_spin(ROWS, COLS , symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines , bet , symbol_values)
    print(f"you won $ {winnings}")
    print(f"you won on lines:", *winning_lines)  
    return winnings - total_bet  

def main():
   balance = deposit()
   while True:
    print(f"current balnce is ${balance}")
    answer = input("press enter to spin(q to quit)")
    if answer =='q':
        break
    balance += spin(deposit)


main()