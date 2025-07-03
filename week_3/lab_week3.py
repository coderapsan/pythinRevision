#1 Function in Python 
#Exercise 1: Creating a first function 
#-------------------------------------------


# def greet_student():
#     print("Good Morning Student")
# greet_student()

#Exercise:  Creating Function with parameter
#------------------------------------

# def greet_student(name):
#     print(f"Hello  {name } Welcome to UWS !!")

# greet_student("Michael")


#3 Task :  Create function greet_friends with list of names 
#----------------------------------------------------

# friend_list=["Mahesh","Raja", "Sambat"]
# def greet_friends(friend):
#     print(f"Hello {friend}" )
# for friend in friend_list: 
#   greet_friends(friend)


#Task : Tax Calculation 
#----------------------------------------------------


# def calculate_tax(income, tax_rate):
#     result = income * tax_rate
#     return result

# # Call the function and print the returned value
# print(calculate_tax(50000, 0.2)) # value as per instruction on task 

 
#Task : Compound Interest Calculator function 
#------------------------------------------------

# def compound_interest(principal, duration, interest_rate):
#     # Validate as per instruction in a question 
#     if interest_rate < 0 or interest_rate > 1:
#         print("Please enter a decimal number between 0 and 1")
#         return None

#     # Validation of duration as per the question 
#     if duration < 0:
#         print("Please enter a positive number of years")
#         return None

#     # Loop through each year using for loop as per question 
#     for year in range(1, duration + 1):
#         total_for_the_year = principal * (1 + interest_rate) ** year
#         print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} £")

#     # Return the final investment value as an integer
#     final_amount = principal * (1 + interest_rate) ** duration
#     return int(final_amount)

# result = compound_interest(1000, 5, 0.05) # used interest rate 0.05 that gave different output 
# print(f"Final investment value after 5 years: {result} £")




#Task : Fixing Errors 
#---------------------------------


# pritn("Hello, World!")  
# #Correct code is  that is semantic erro 
# print("Hello World")
# #defining favorite_color to erase the error 
# favorite_color="red"

# print("My favorite color is", favorite_color) 

# number1 = "5" 
# number1=int(number1) #converted string to integer to fix the issues 
# number2 = 3 
# result = number1 + number2 

# fruits = ["apple", "banana", "cherry"] 
# print(fruits[3]) #index error because 3 is not available 

# print (fruits[1])

# time = 11 
# if time <=12:  # add = sign 
    
# print("Good morning!") 
# print("good morning") 



#Task : My first larger scale python program 
# tasks_list=[""]


