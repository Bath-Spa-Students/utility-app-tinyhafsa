#vending machine function
def vending_machine ():

    #displaying heading of vending machine using ASCII art
    print('''
    ▀█─█▀ █▀▀ █▀▀▄ █▀▀▄ ─▀─ █▀▀▄ █▀▀▀ 　 █▀▄▀█ █▀▀█ █▀▀ █──█ ─▀─ █▀▀▄ █▀▀ 
    ─█▄█─ █▀▀ █──█ █──█ ▀█▀ █──█ █─▀█ 　 █─▀─█ █▄▄█ █── █▀▀█ ▀█▀ █──█ █▀▀ 
    ──▀── ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▀───▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀''')

    #storing menu information in a three-level nested dictionary
    menu = {
        #storing items in beverage category
        "drinks": {
            "a": {"name": "Fanta"          , "price": 2.50 , "code": "1"  , "stock": 2},
            "b": {"name": "Cold Water"     , "price": 1.00 , "code": "2"  , "stock": 4},
            "c": {"name": "Guava Juice"    , "price": 2.00 , "code": "3"  , "stock": 3},
            "d": {"name": "Chocolate Milk" , "price": 3.00 , "code": "4"  , "stock": 3}
    },
        #storing items in snack category
        "snacks": {
            "e": {"name": "Lays Chips"     , "price": 2.25 , "code": "5"  , "stock": 4},
            "f": {"name": "Chunko Cookies" , "price": 2.00 , "code": "6"  , "stock": 3},
            "g": {"name": "Caramal Popcorn", "price": 3.50 , "code": "7"  , "stock": 3},
            "h": {"name": "Loackers Wafers", "price": 3.00 , "code": "8"  , "stock": 3}
    },
        #storing items in sweet category
        "sweets": {
            "i": {"name": "M&Ms"           , "price": 3.50 , "code": "9"  , "stock": 6},
            "j": {"name": "Bounty"         , "price": 3.00 , "code": "10" , "stock": 4},
            "k": {"name": "Hersheys"       , "price": 3.50 , "code": "11" , "stock": 4},
            "l": {"name": "Cake roll"      , "price": 3.00 , "code": "12" , "stock": 4}
    }
}
    
    #function to display the menu
    def show_menu():
        #displaying beverages category
        print ("\n\t\t\033[1;30m ＤＲＩＮＫＳ  \033[0m        ")
        print ("\t\t.------.------------------.--------.-------.")
        print ("\t\t| CODE |       NAME       | PRICE  | STOCK |")
        print ("\t\t:------+------------------+--------+-------:")
        #for loop goes through the items in the drink category and displays them
        for code, details in menu["drinks"].items():
            # STOCK MANAGEMENT - item is only displayed if the stock is more than 0 
            if details["stock"] > 0:
                print(f"\t\t|  {details['code']:<4}| {details['name']:<16} | ${details['price']:<6}|   {details['stock']:<4}|")
        print ("\t\t'------'------------------'--------'-------'\n")
        #displaying snacks category
        print ("\t\t\033[1;30m ＳＮＡＣＫＳ \033[0m     ")
        print ("\t\t.------.------------------.--------.-------.")
        print ("\t\t| CODE |       NAME       | PRICE  | STOCK |")
        print ("\t\t:------+------------------+--------+-------:")
        #for loop goes through the items in the drink category and displays them
        for code, details in menu["snacks"].items():
            # STOCK MANAGEMENT - item is only displayed if the stock is more than 0
            if details["stock"] > 0:
                print(f"\t\t|  {details['code']:<4}| {details['name']:<16} | ${details['price']:<6}|   {details['stock']:<4}|")
        print ("\t\t'------'------------------'--------'-------'\n")
        #displaying sweets category
        print ("\t\t\033[1;30m ＳＷＥＥＴＳ \033[0m    ")
        print ("\t\t.------.------------------.--------.-------.")
        print ("\t\t| CODE |       NAME       | PRICE  | STOCK |")
        print ("\t\t:------+------------------+--------+-------:")
        #for loop goes through the items in the drink category and displays them
        for code, details in menu["sweets"].items():
            # STOCK MANAGEMENT - item is only displayed if the stock is more than 0
            if details["stock"] > 0:
                print(f"\t\t|  {details['code']:<4}| {details['name']:<16} | ${details['price']:<6}|   {details['stock']:<4}|")
        print ("\t\t'------'------------------'--------'-------'\n")

#function for user interaction
    def user_selection():
        #repurchase is set to true - the loop will end when if is false
        repurchase = True
        # MONEY MANAGEMENT - user inputs money
        money = float(input("\t\033[1;30mInsert your money = $\033[0m"))
        #menu function is called to print menu
        show_menu()
        user_cart = [] #empty list is created - this will store user purshases for the receipt
        #while loop that runs while repurchase is true
        while repurchase:
            #user inputs item code
            purchase = (input("\t\033[1;30mInput code of selected item:\033[0m "))
            #item found is initially set to false
            item_found = False
            
            #for loop - goes through items in menu 
            for category, items in menu.items():
                for code, details in items.items():

                    #if code matches the list and item is in stock
                    if purchase == details['code'] and details['stock'] > 0:
                        
                        #if money entered is equal to or more than price
                        if money >= details['price']:
                            item_found = True #item is found so value is set to true
                            # MONEY MANAGEMENT - price is subtracted from money entered
                            money = money - details['price']                        
                            print(f"\n\t{details['name']} dispensed.") # ITEM DISPENSE MESSAGE
                            print(f"\t${money} remaining.\n") #CHANGE MESSAGE
                            user_cart.append(details) #item is added to empty list created
                            details["stock"] -= 1 # STOCK MANAGEMENT - one subtracted from stock

                            #SUGGESTIONS
                            if purchase in ["drinks"]: # if user purchases a drink
                                #suggested snacks are printed
                                print ("\t\033[1;30mWe suggest a snack with your drink.\033[0m")
                                print ("\tWe offer: Lays Chips, Chunko Cookies, Caramel Popcorn and Loackers Wafers.")
                            elif purchase in ["snacks"]: # if user purchases a snack
                                #suggested sweets are printed 
                                print ("\t\033[1;30mWe suggest a sweet with your snack.\033[0m")
                                print ("\tWe offer: M&Ms, Bounty, Hersheys and Cake Roll.")
                            else: # if user purchases a sweet
                                #suggested drinks are printed
                                print ("\t\033[1;30mWe suggest a drink with your sweet.\033[0m")
                                print ("\tWe offer: Fanta, Cold Water, Guava Juice and Chocolate Milk.")

                            #user is asked if they want to continue
                            another_purchase = input("\n\t\033[1;30mWould you like to make another purchase [Y/N]?\033[0m ").upper()
                            
                            if another_purchase == "N": #if user doesn't want to continue                               
                                repurchase = False #repurchase is set to false and loop is broken
                                break
                            
                            elif another_purchase == "Y": #if user wants to continue
                                show_menu() #menu is shown again and loop starts over
                                continue

                            else: #if user enters anything else, loop ends
                                print("\tInvalid input. Exiting.")
                                return
                            
                        else: #if money entered or change remaining is not enough for a repurchase
                            item_found = True #item is found and value is changed to true
                            print("\n\tNot enough money. Please enter more money.")
                            #user is asked to inout more money - extra money is added to change
                            money += float(input("\t\033[1;30mInsert more money = $\033[0m"))
                            print(f"\tUpdated money balance: ${money:.2f}\n") #updated money is displayed

                    #if the code matches the list but item is out of stock        
                    elif purchase == details['code'].lower(): 
                        item_found = True #item code matches so value is set to true
                        print("\t\033[1;30mItem out of stock.\033[0m\n") #message informing user is displayed

            #if item is not found
            if not item_found:
                print("\tInvalid code.\n") #error message is printed
        #if user cart is not empty
        if user_cart:
            print_receipt(user_cart) #function to print receipt is called

    #function to print receipt
    def print_receipt(user_cart):
        print ("\n\t\t\033[1;30m ＲＥＣＥＩＰＴ \033[0m  ") #title is displayed
        print ("\t\t.-----------------------------.")
        #for loop - goes through the items in the user cart (purchases)
        for item in user_cart:
            #item name and price is printed 
            print (f"\t\t| {item['name']:<19}  ${item['price']:<6}|")
        print ("\t\t|                      ------ |")
        #total money spent is printed
        print (f"\t\t|               TOTAL: ${sum(item['price'] for item in user_cart):.2f}  |")
        print ("\t\t'-----------------------------'")
        #message displayed at the end of the program
        print("\n\t\033[1;30mTransaction complete. Enjoy your purchase.\033[0m\n")

    #function is called to begin user interaction     
    user_selection()
#function is called to start vending machine
vending_machine ()