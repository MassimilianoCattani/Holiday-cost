# Practical task

"""
- It will be built a holiday cost calculator following the task guide lines:
    Collect user data into variable:
        - CITY_FLIGHT. User destination.
        - num_nigths. User residence time in nights.
        - RENTAL_DAYS. User car rent in days.
    Create functions able to convert user input into bills.
        - plane_cost(). It takes CITY_FLIGHT as arg and return the fee.
        - hotel_cost(). It takes NUM_NIGHTS as arg and return the fee.
        - car_rental(). It takes RENTAL_DAYS as arg and return the fee.
        - holiday_cost(). It takes the previous three functions
        as arguments and display total holiday cost.
   
- The data for display and selection is stored in two variable:
    - A dictionary for the flight destinations.
    - A list of dictionaries with city name and the hotel and car type options.     
- Two mini functions have been implemented to support a better format of the option lists.
- CITY_FLIGHT, NUM_NIGHTS, RENTAL_DAYS are global variable and so all their validation structure.
- Hotel and car type inputs are local variable in their respective functions.
- The program has been designed to handle user wrong entries.


"""
# Data packages
#--------------------------
# Flights prices.
flight_prices = {
    'budapest' : 199,
    'london': 299,
    'madrid' : 169,
    'tokyo': 799,
    'rio de janeiro': 1099,
    'new york': 999
}

#-------------------------
# Hotels and car price per day.
destinations = [
    {'city' : {
        'name': 'budapest',
        'hotel': {
                'stars_5': 1000,
                'stars_4': 800,
                'stars_3': 250,
                'stars_2': 150,
                'stars_1': 70 
        },
        'car': {
                'mercedes' : 70,
                'audi': 68,
                'jaguar': 90,
                'toyota': 50
        }
    }},
    {'city': {
        'name': 'london',
        'hotel': {
                'stars_5': 1250,
                'stars_4': 950,
                'stars_3': 350,
                'stars_2': 250,
                'stars_1': 100 
        },
        'car': {
                'mercedes' : 100,
                'audi': 90,
                'jaguar': 120,
                'toyota': 75
        } 
    }},
    {'city': {
        'name': 'madrid',
        'hotel': {
                'stars_5': 1050,
                'stars_4': 900,
                'stars_3': 320,
                'stars_2': 110,
                'stars_1': 75 
        },
        'car': {
                'mercedes' : 75,
                'audi': 65,
                'jaguar': 100,
                'toyota': 50
        }
    }},
    {'city': {
        'name': 'tokyo',
        'hotel': {
                'stars_5': 1300,
                'stars_4': 1050,
                'stars_3': 400,
                'stars_2': 250,
                'stars_1': 130
        },
        'car': {
                'mercedes' : 120,
                'audi': 100,
                'jaguar': 190,
                'toyota': 30
        }
    }},
    {'city': { 
        'name': 'riodejaneiro',
        'hotel': {
                'stars_5': 990,
                'stars_4': 770,
                'stars_3': 310,
                'stars_2': 140,
                'stars_1': 60 
        },
        'car': {
                'mercedes' : 90,
                'audi': 80,
                'jaguar': 90,
                'toyota': 40 
        }
    }},
    {'city': {
        'name': 'newyork',
        'hotel': {
                'stars_5': 2500,
                'stars_4': 1800,
                'stars_3': 850,
                'stars_2': 450,
                'stars_1': 170 
        },
        'car': {
                'mercedes' : 210,
                'audi': 180,
                'jaguar': 190,
                'toyota': 150
        }
    }}
]

#----------------------
DOT_LINE_FLIGHT = 18 # DOT_LINE_FLIGHT is a dotted standard length line (for format purpose).
CITY_FLIGHT = '' # declare empty user input.
NUM_NIGHTS = '' # declare empty user input.
RENTAL_DAYS = '' # declare empty user input.
GLOBAL_FLAG = False # for global inputs validation.
print("\nWelcome to our customisable holiday packages.")

#---------------------------------------------------------------------
# Display destinations.

def display_flight(obj, n):
    """
        This function gets a list and an integer as args
        and displays key, value pair data in a more readeable way.\n
        It will be subtracted to DOT_LINE_FLIGHT (the given dotted line) the 
        length of the key in the list and  multyplied for the string '.'.\n
        Now, key, DOT_LINE_FLIGHT and value can be concatenated and displayed visually better.
        All the prices are aligned to the right at the same distance.
    """
    print('\nDestinations:\n')
    for key, val in obj.items():
        print(f"{key.capitalize()} {'.'*(n - len(key))} £ {val:,.2f}")
    print('\n')
display_flight(flight_prices, DOT_LINE_FLIGHT)

#----------------------------------------------------------------------
# Catch user flight destination input.

""" 
    - Only if user selection(city _flight) == key the condition will be true. 
    - Any other input will be consider invalid,
    hence, the program will carry on asking
    for the correct input.
    - There is a counter(option_length) checking
    if the length of the list has been reached.
    Note: a 'break' statement has been placed in the first 'if' statement.
    So, once the key match the input we stop the inner for loop. 
        - Without the 'break', even if the condition is passed, 
        in addition to our valid output we will have a error message. 
        This is because the counter will carry on untill
        it reaches the length of the dictionary.
""" 

while GLOBAL_FLAG is False:
    CITY_FLIGHT = input("--> Please, enter one of the available options: ").lower() 
    OPTIONS_LENGTH = 0 
    for key_destination, val_price in flight_prices.items():
        OPTIONS_LENGTH += 1
        if CITY_FLIGHT == key_destination:
            print('-'*  50)
            print(f"You have selected {key_destination.upper() + '.'*(DOT_LINE_FLIGHT - len(key_destination))}£ {val_price:,.2f}")
            print('-'*  50)
            GLOBAL_FLAG = True
            break
        if OPTIONS_LENGTH == len(flight_prices):
            print('Invalid  entry!')
         
# reset GLOBAL_FLAG to False.      
GLOBAL_FLAG = False

#----------------------------------------------------------------------
# Catch user number of nights.

"""
    This while loop acts as a function to
    get and check if the entry is valid:
    If user input(NUM_NIGHTS) is an integer
    the condition will be evaluated as true,
    else print error msg and ask to user to re-enter data.
"""

while GLOBAL_FLAG is False:
    NUM_NIGHTS = input("Enter number of nights: ")
    if NUM_NIGHTS.isnumeric():
        NUM_NIGHTS = int(NUM_NIGHTS) 
        print(f"Number of nights: {NUM_NIGHTS}")
        print('-'*  50)
        GLOBAL_FLAG = True    
    else:
        print("Please, enter a number!")
        
# Reset GLOBAL_FLAG to False.     
GLOBAL_FLAG = False

#--------------------------------------------------------------------
# Catch user car rental days.

"""
    Here, has been applied the same principle
    to check the number of nights( NUM_NIGHTS)
    but related to days of car rental.
    It is still required an integer as input. 
    Note: It is possible to create and re-use a function 
    to get and validate 'num_night' and 'RENTAL_DAYS' inputs.
"""
while GLOBAL_FLAG is False:
    RENTAL_DAYS = input("Enter number of days you wish to rent a car: ")
    if RENTAL_DAYS.isnumeric(): 
        RENTAL_DAYS = int(RENTAL_DAYS)
        print(f"Days of car rent: {RENTAL_DAYS}")
        print('-'*  50)
        GLOBAL_FLAG = True    
    else:
        print("Please, enter a number!")
    
#--------------------------------------------------------------------------------
# Flight cost.

def plane_cost(destination):
    """
    Once it finds destination matching with key, returns the value (price of the flight).
    """
    for key, val in flight_prices.items():
        if destination == key:
            return val
            
city_f = CITY_FLIGHT.replace(' ', '')
""" 
    CITY_FLIGHT input gets modified to match
    key for hotel and car selection:
    Rio de janeiro -> riodejaneiro.
    To void keys made of multiple words.
    Note: When we grasp data for 'destinations'
    list of dictionary, the name of the city
    is needed just to identify the related
    hotel and car prices.
"""
#---------------------------------------------------------------------------------   
# Hotel cost for the whole tenancy.

def hotel_cost(n_nights):
    """
    This function displays hotel type options, gets the choosed option form the user
    and return the total price for the whole hotel room tenancy.\n 
    1- If user destination (city_f) match the name key/value
    in 'destinations' list of dictionary of dictionaries (destination['city']['name']),
    hotel data in the same dict of name will be displayed (destination['city']['hotel']). 
        - On every iteration an incrementing counter (c) will be added to enumerate the list. \n 
    2 - User input hotel type.\n
    3 - Check if user hotel type selection is a number: 
        - If ok, cast user hotel input into integer.
            - Enumerate each key value pair of hotel dict:
                - Compare keys of enumerated hotel list with user input.
                - Option 0 to skip the selection.
                - If key and user inp match:
                    - Calc tot cost tenancy -> price = value * n_nights (argument: NUM_NIGHTS)
                    - Display selection and price per night.
                    - Return price 
                - Else if user inp == 0, return 0 (skip) 
                - If user inp is integer but bigger than the length of the list or smaller than 0:
                    - Error msg, ask input again.
        - Else, error msg, ask again input.
    """
    user_hotel_inp = ''
    c = 1 
    flag = False
    price = 0
    
    for i in destinations:
        
        if i['city']['name'] == city_f:
            print('Listed prices are charges per night.')
            print("Hotel Type - Digit a relative number option or 0 to skip: \n")
            
            for k, v in i['city']['hotel'].items():
                print(f"{c}: {k.capitalize()}..... £: {v:,.2f}")
                c += 1
            print('\n') 
            
            while flag is False:
                
                user_hotel_inp = input("--> Enter your selection: ")
                
                if user_hotel_inp.isnumeric():
                    user_hotel_inp = int(user_hotel_inp)
                    
                    for k, v in enumerate(i['city']['hotel'].items(), 1): 
                        
                        if user_hotel_inp == k:
                            print(f"Option {k}. Hotel type: {v[0]}.....Price: £ {v[1]:,.2f} per night.")
                            print('-'*  50)
                            price = n_nights * v[1]
                            flag = True
                            return price
                        if user_hotel_inp == 0:
                            flag = True
                            return 0
                        if user_hotel_inp > len(i['city']['hotel']) or user_hotel_inp < 0:
                            print("Invalid entry!")
                            break              
                else:
                    print("Invalid input!")
    

#----------------------------------------------------------------------------------------------
# Display cars and prices per day. (Helper function)

def display_car(obj, n):
    """ 
        - This function help to format the output of the car type list. All the prices will be aligned to the right, following a standard dotted line (n), from which length will be subtracted the length of the car type key.
        - It has been picked this approach because the keys length in car sub-dictionary are not equal.
        - It has been separated the display functionality from the select functionality.
        - counter is used to enumerate displayed list elements. 
    """
    counter = 1
    for key, val in obj.items():
        print(f"{counter}: {key.capitalize() + '.'*(n - len(key))} £ {val:,.2f}")
        counter += 1

# Car rental total cost.

def car_rental(n_days):
    
    """
        This function displays car type options, gets the choosed option form the user and return the total price for the entire car rental.\n 
        1- If user destination (city_f) match the name key/value in 'destinations' list of dictionaries (destination['city']['name']),
            - display_car (destination['city']['car'], dotted line var).
        2 - Get user car input.
        3 - Check if user car type selection is a number: 
            - If ok, cast user car input into integer.
                - Enumerate each key value pair of car dict:
                    - Compare keys of enumerated car list with user input.
                    - Option 0 to skip the selection.
                    - If key and user inp match:
                        - Calc tot cost car rental -> price = value * n_days (argument: RENTAL_DAYS)
                        - Display selection and price per day.
                        - Return price 
                    - Else if user inp == 0, return 0 (skip) 
                    - If user inp is integer but bigger than the length of the list or smaller than 0:
                        - Error msg, ask input again.
            - Else, error msg, ask again input.
        
    """
    
    dot_line_car = 13
    user_car_inp = ''
    flag = False
    price = 0
    
    for i in destinations:
        if i['city']['name'] == city_f:
            print('Listed prices are daily charges.')
            print("Car Type - Digit a relative number option or 0 to skip: \n")
            display_car(i['city']['car'], dot_line_car)
            print('\n')
            
            while flag is False:
    
                user_car_inp = input("--> Enter your selection: ")
                
                if user_car_inp.isnumeric():
                    user_car_inp = int(user_car_inp)
                
                    for k, v in enumerate(i['city']['car'].items(), 1): 
                        
                        if user_car_inp == k:
                            print(f"Option {k}. Car type: {v[0].capitalize()}.....Price: £ {v[1]:,.2f} per day.")
                            print('-'*  50)
                            price = n_days * v[1]
                            flag = True 
                            return price  
                        if user_car_inp == 0:
                            flag = True
                            return 0
                        if user_car_inp > len(i['city']['car']) or user_car_inp < 0:
                            print("Invalid entry!")
                            break
                else:
                    print("Invalid input!")                        
#-------------------------------------------------------------------------------
# Calculate and display total holiday bill.

def holiday_cost(flight, hotel, car):
    
    """
    - This function takes three args(plane_cost(CITY_FLIGHT),
    hotel_cost(NUM_NIGHTS), car_rental(RENTAL_DAYS)). 
    These args return an integer (Which is the total of each single selection.
    - It displays the total cost for each option selected.
    - Return the total of total (tot -> sum of the three args)
    - All the costs will be aligned to the right,
    following a standard dotted line,
    from which length will be subtracted the
    length of the variable holding the text. 
    """
    
    dot_sep = 20
    text_flight = "Flight cost"
    text_hotel = "Hotel cost"
    text_car = "Car cost" 
    tot =  flight + hotel + car
    print('-'*  50)
    print('Final bill:\n')
    
    print(f"{text_flight}{(dot_sep - len(text_flight)) * '.'}£ {flight:,.2f}\n{text_hotel}{(dot_sep - len(text_hotel)) * '.'}£ {hotel:,.2f}\n{text_car}{(dot_sep - len(text_car)) * '.'}£ {car:,.2f}")
    
    print('-'*  50)
    return f"Total holiday cost: £ {tot:,.2f}"

print(holiday_cost(plane_cost(CITY_FLIGHT), hotel_cost(NUM_NIGHTS), car_rental(RENTAL_DAYS)))       
print('-'*  50,'\n')