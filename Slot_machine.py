# SLOT MACHINE GAME
        
import random

def spin_row():
    symbols=["🍎","🍒","👑","🌟","🐒"]
    return [random.choice(symbols) for i in range (3) ]

def show_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_pay(row, bet):
    if row [0] == row[1] == row[2]:
        if row[0]=="🍎":
            return bet * 2
        elif row[0]=="🐒":
            return bet * 5
        elif row[0]=="🍒":
            return bet * 10
        elif row[0]=="🌟":
            return bet * 15
        elif row[0]=="👑":
            return bet * 20
    return 0



def main():
    balance=50
    print("****************************")
    print("WELCOME TO PYTHON SLOT GAME")
    print("Symbols: [🍎 🍒 👑 🌟 🐒]")
    print("****************************")

    while balance > 0: 
        print(f"Current balance is: PKR {balance}")
        bet= input("Enter your bet amount: ")
            
        if not bet.isdigit():
            print("Plaese enter a valid amount")
            continue

        bet=int(bet)

        if bet > balance:
            print("Invalid Amount:Enter a valid amount")
            continue

        if bet <= 0:
            print("Insufficient balance")
            continue

        balance -= bet
            
        row = spin_row()
        print("....Spining....\n")
        show_row(row)

        payout=get_pay(row , bet)

        if payout>0:
            print(f"You won: PKR {payout}")
        else:
            print("You lost this round")
        
        balance += payout

        while True:
            play_again=input("Play again? (Y/N)").upper()
            if play_again == "Y":
                break
            elif play_again == "N":
                print("*******************************************")
                print(f"Game over! Your Balance is: PKR {balance}")
                print("*******************************************")
                return
            else:
                print("Select from (Y/N)")

if __name__=="__main__":
    main()
