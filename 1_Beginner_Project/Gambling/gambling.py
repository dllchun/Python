import random

max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_count = {
    "A": 2, 
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items:
        for i in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value  = random.choice(all_symbols)
            current_symbol.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns
        
        


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('The amount should be greater than 0')
        else: 
            print("Please enter than number!")
        
    return amount     

def get_number_of_line():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(max_lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print('Enter a valid number of lines')
        else: 
            print("Please enter than number!")
        
    return lines  

def get_bet():
    while True:
        lines = input("What would you like to bet  ")
        if lines.isdigit():
            lines = int(lines)
            if min_bet <= lines <= max_bet:
                break
            else:
                print(f'Amount must be between ${min_bet} - ${max_bet}')
        else: 
            print("Please enter than number!")
        
    return lines 

def main():
    balance = deposit()
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        if total_bet >= balance:
            print(f"You do not  have enough to bet, your current balance is ${balance}")
        else:
            break
   
    print(f'You are betting ${bet} on {lines}. Total bet is equal to: ${total_bet} ')


main()