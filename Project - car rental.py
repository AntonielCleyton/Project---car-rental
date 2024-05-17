import time
import os

class RentalService:
    
    # Dictionary of available cars for rent with their prices per day
    cars = {
        '0':  'Chevrolet Tracker - $120 /day',
        '1': 'Chevrolet Onix - $90 /day',
        '2': 'Chevrolet Spin - $150 /day',
        '3': 'Hyundai HB20 - $85 /day',
        '4': 'Hyundai Tucson - $120 /day',
        '5': 'Fiat Uno - $60 /day',
        '6': 'Fiat Mobi - $70 /day',
        '7': 'Fiat Pulse - $130 /day'
    }

    # Dictionary to store rented cars
    rented_cars = {}

    def __init__(self):
        self.name = 'name'  # Initialize with a default name

    def greetings(self):
        os.system('cls')
        print('-------------------------------')
        print('Welcome to the car rental service!')
        print('-------------------------------')
        self.name = str(input('What is your name? '))
        os.system('cls')
        bar = '='
        for i in range(10):  # Display a loading animation
            test = bar * i
            print(f'Nice to meet you, {self.name}!')
            print('Starting the system...')
            print(test)
            time.sleep(1)
            os.system('cls')
        print('System loaded!')
        time.sleep(1)
        os.system('cls')

    def portfolio(self):
        os.system('cls')
        while True:
            print('Welcome to the car rental service!')
            print('--------------------------------')
            print('-------Cars for rent-------')
            print('--------------------------------')
            # Main menu for selecting different actions
            menu = int(input('0 - Show portfolio | 1 - Rent a car | 2 - Return a car | 3 - Exit the program\nAnswer: '))
            print('Entering the chosen menu...')
            time.sleep(1)
            os.system('cls')
            if menu == 0:
                # Display the car portfolio
                print('-----CAR PORTFOLIO-----')
                for i, n in self.cars.items():
                    print(f'[{i}] - {n}\n')
                print('------------------------------')
                # Option to go back to the main menu or exit
                choice = int(input('0 - Back to menu | 1 - Exit the program\nAnswer: '))
                if choice == 0:
                    print(f'Okay {self.name}! Returning to the main menu...')
                    time.sleep(1)
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    print(f'Okay {self.name}! Exiting the program...')
                    time.sleep(1)
                    break
            elif menu == 1:
                # Rent a car menu
                while True:
                    print('-----CARS FOR RENT-----')
                    for i, n in self.cars.items():
                        print(f'[{i}] - {n}\n')
                    print('------------------------------')
                    choice = int(input('0 - Continue | 1 - Exit\nAnswer: '))
                    if choice == 0:
                        choice1 = int(input('Choose the car code:\nAnswer: '))
                        if choice1 == 0:
                            # Rent Chevrolet Tracker
                            chosen_car = self.cars['0']
                            del self.cars['0']
                            self.rented_cars['0'] = 'Chevrolet Tracker - $120 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 120 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                        elif choice1 == 1:
                            # Rent Chevrolet Onix
                            chosen_car = self.cars['1']
                            del self.cars['1']
                            self.rented_cars['1'] = 'Chevrolet Onix - $90 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 90 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                        elif choice1 == 2:
                            # Rent Chevrolet Spin
                            chosen_car = self.cars['2']
                            del self.cars['2']
                            self.rented_cars['2'] = 'Chevrolet Spin - $150 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 150 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                        elif choice1 == 3:
                            # Rent Hyundai HB20
                            chosen_car = self.cars['3']
                            del self.cars['3']
                            self.rented_cars['3'] = 'Hyundai HB20 - $85 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 85 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                        elif choice1 == 4:
                            # Rent Hyundai Tucson
                            chosen_car = self.cars['4']
                            del self.cars['4']
                            self.rented_cars['4'] = 'Hyundai Tucson - $120 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 120 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                        elif choice1 == 5:
                            # Rent Fiat Uno
                            chosen_car = self.cars['5']
                            del self.cars['5']
                            self.rented_cars['5'] = 'Fiat Uno - $60 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 60 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                        elif choice1 == 6:
                            # Rent Fiat Mobi
                            chosen_car = self.cars['6']
                            del self.cars['6']
                            self.rented_cars['6'] = 'Fiat Mobi - $70 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 70 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                        elif choice1 == 7:
                            # Rent Fiat Pulse
                            chosen_car = self.cars['7']
                            del self.cars['7']
                            self.rented_cars['7'] = 'Fiat Pulse - $130 /day'
                            days = int(input('Choose how many days you want to rent: '))
                            print(f'You rented the {chosen_car} for {days} days')
                            total_cost = 130 * days
                            choice2 = int(input(f'The rental will total ${total_cost}. Do you want to continue? 1-YES | 2-NO\nAnswer:  '))
                            if choice2 == 1:
                                print(f'Okay {self.name}! Returning to the car rental menu...')
                                time.sleep(1)
                                os.system('cls')
                                continue
                            else:
                                os.system('cls')
                                print(f'Okay {self.name}! Returning to the main menu...')
                                time.sleep(1)
                                break
                    elif choice == 1:
                        # Exit rent a car menu
                        print(f'Okay {self.name}! Returning to the main menu...')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        # Handle invalid choice
                        print(f'{self.name}, you made an invalid choice! Try again...')
                        time.sleep(2)
                        os.system('cls')
                        continue
            elif menu == 2:
                # Return a car menu
                while True:
                    print('-----CAR RETURN-----')
                    for i, n in self.rented_cars.items():
                        print(f'[{i}] - {n}\n')
                    print('----------------------------')
                    choice = int(input('0 - Continue | 1 - Exit\nAnswer: '))
                    if choice == 0:
                        choice1 = int(input('Choose the car code:\nAnswer: '))
                        chosen_car = self.rented_cars[str(choice1)]
                        self.cars[str(choice1)] = self.rented_cars[str(choice1)]
                        del self.rented_cars[str(choice1)]
                        print(f'{self.name}, you returned the {chosen_car}!')
                        print('---------------------------------------------')
                        if not self.rented_cars:
                            print('There are no more cars to return...')
                        else:
                            print('There are still cars to be returned...')
                        print('---------------------------------------')
                        choice2 = int(input('Do you want to return another car? 0 - YES | 1 - NO\nAnswer: '))
                        if choice2 == 0:
                            print(f'Okay {self.name}! Returning to the main menu...')
                            time.sleep(1)
                            os.system('cls')
                            continue
                        else:
                            print(f'Okay {self.name}! Returning to the main menu...')
                            time.sleep(1)
                            os.system('cls')
                            break
                    elif choice == 1:
                        # Exit return a car menu
                        print(f'Okay {self.name}! Returning to the main menu...')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        # Handle invalid choice
                        print(f'{self.name}, you chose an invalid option! Returning to the options...')
                        time.sleep(1)
                        os.system('cls')
                        continue
            elif menu == 3:
                # Exit the program
                print(f'Okay {self.name}! Leaving the car rental program...')
                time.sleep(1)
                os.system('cls')
                break

# Create an instance of RentalService
user = RentalService()

# Call greetings method
user.greetings()

# Call portfolio method
user.portfolio()
