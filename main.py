################### SLOT MACHINE ###################

import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET =100

ROWS = 3
COLS = 3

# availability of symbols in the slot machine
SYMBOLS_COUNT = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

# value of each symbol
SYMBOLS_VALUES = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

# user has to deposit some amount so that they can bet 
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid amount")
        else:
            print("please enter a number")
    return amount

# checking whether any rows are having same symbol. if yes, bet amount is multipied with symbol value
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines

    
# function that gets the number of lines , user is betting on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet: 1 - "+str(MAX_LINES)+ ' :')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <=  MAX_LINES:
                break
            else:
                print("Please enter a line number between 1 and 3")
        else:
            print("please enter a number")
    return lines

# function that collects the bet amount from the user
def get_bet_amount():
    while True:
        amount = input("Enter the amount you want to bet: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Please enter a valid bed amount")
        else:
            print("please enter a number")
    return amount

# function that sets the rows and columns of slot machine with values
def get_values_in_slots(rows,cols,symbols):

    all_Symbols = []
    for symbol,symbolcount in symbols.items():
        for _ in range(symbolcount):
            all_Symbols.append(symbol) # all_Symbols = ['A','A','B','B','B','B','C','C','C','C','C','C','D','D','D','D','D','D','D','D']
   
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_Symbols[:] # copying the contents of all_Symbols to current_symbol
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    
#printing the column list in a transpose way
def print_slot_symbols(columns):
    print(columns)
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print() 




def game(balance):
    lines = get_number_of_lines()
    
    while True:
        bet_amount =  get_bet_amount()
        total_bet_amount = bet_amount * lines
        if total_bet_amount > balance:
            print(f"You do not have enough balance to bet. your current balance is {balance}")
        else: 
            break
    print(f'you are betting ${total_bet_amount} on {lines}')

    slots = get_values_in_slots(ROWS,COLS,SYMBOLS_COUNT)
    print_slot_symbols(slots)
    winnings,winning_lines= check_winnings(slots,lines,bet_amount,SYMBOLS_VALUES)
    print(f"You won ${winnings} on", *winning_lines) #using *(splat operator)- enables us to use multiple value in same line
    return winnings - total_bet_amount

def main():
    balance = deposit()
    while True:
        print(f'Current balance is {balance}')
        text = input("please enter to continue or 'q' to quit : ")
        if text == 'q':
            break
        balance += game(balance)
    
main()
