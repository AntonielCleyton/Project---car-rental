import os
import time

# Dictionary containing car models and their rental prices
car_portfolio = {
    "Chevrolet Tracker": "R$ 120 /day",
    "Chevrolet Onix": "R$ 90 /day",
    "Chevrolet Spin": "R$ 150 /day",
    "Hyundai HB20": "R$ 85 /day",
    "Hyundai Tucson": "R$ 120 /day",
    "Fiat Uno": "R$ 60 /day",
    "Fiat Mobi": "R$ 70 /day",
    "Fiat Pulse": "R$ 130 /day"
}

# Dictionary containing rented cars
rented_cars = {
    "Chevrolet Tracker": "R$ 120 /day",
    "Chevrolet Onix": "R$ 90 /day",
    "Chevrolet Spin": "R$ 150 /day",
    "Hyundai HB20": "R$ 85 /day",
    "Hyundai Tucson": "R$ 120 /day",
    "Fiat Uno": "R$ 60 /day",
    "Fiat Mobi": "R$ 70 /day",
    "Fiat Pulse": "R$ 130 /day"
}

# Dictionary containing returned cars
returned_cars = {}

while True:
    os.system("cls")  # Clear the console screen
    print("Welcome to the car rental service!")
    print("===================================")
    main_menu = int(input("0 - Show car portfolio, 1 - Rent a car, 2 - Return a car\n"))
    
    if main_menu == 0:
        i = 0
        for model, price in car_portfolio.items():
            print(i, "-", model, "-", price)
            i += 1
        print("=========================")
        choice_1 = int(input("1 - CONTINUE | 2 - EXIT\n"))
        if choice_1 == 1:
            print("Returning to the main menu...")
            time.sleep(2)
        else:
            print("Exiting the program...")
            time.sleep(2)
            quit()
            
    if main_menu == 1:
        i = 0
        for model, price in car_portfolio.items():
            print(i, "-", model, "-", price)
            i += 1    
        print("=========================")
        rent_car = int(input("Choose a code: "))
        if rent_car in range(len(car_portfolio)):
            days_rented = int(input("For how many days do you want to rent? "))
            rental_cost = days_rented * 120  # Assuming the rental cost for all cars is the same
            os.system("cls")
            print("You have chosen the Chevrolet Tracker for {} days. The total rental cost would be R${}. Do you want to proceed?\n".format(days_rented, rental_cost))
            finish_contract = int(input("1 - YES | 2 - NO\n"))
            if finish_contract == 1:
                selected_car = list(car_portfolio.keys())[rent_car]
                del car_portfolio[selected_car]
                del rented_cars[selected_car]
                returned_cars[selected_car] = "R$ 120 /day"
                os.system("cls")
                print("Congratulations! You rented the {} for {} day(s)".format(selected_car, days_rented))
                print("=====================")
                choice_1 = int(input("1 - CONTINUE | 2 - EXIT\n"))
                if choice_1 == 1:
                    print("Returning to the main menu...")
                    time.sleep(2)
                else:
                    print("Exiting the program...")
                    time.sleep(2)
                    quit()
        else:
            print("Invalid car code! Please select a valid option.")
            time.sleep(2)
            continue
            
    if main_menu == 2:
        i = 0
        for model, price in returned_cars.items():
            print(i, "-", model, "-", price)
            i += 1
        print("===================")
        return_car = int(input("Which car do you want to return? "))
        car_list = list(returned_cars)
        car_to_return = car_list[return_car]
        car_portfolio[car_to_return] = returned_cars[car_to_return]
        del returned_cars[car_to_return]
        print("You have returned the {}! Thank you for choosing us.".format(car_to_return))
        print("Returning to the main menu...")
        time.sleep(4)
