#IF Conditionals 
# ----------------

# age = 12
# age_group = "child" 
# if age > 18: 
#  age_group = "adult" 
# print(f"The age group is {age_group}") 


#if – else Conditionals
# ----------------

# wind_speed = 8
# if wind_speed < 10: 
#  print("It is a calm day") 
# else: 
#  print("It is a windy day") 


# Exercise 5: if – elif - else Conditionals 
# ----------------

# grade = 76
# if grade < 50: 
#  print("You failed") 
# elif grade < 60: 
#  print("You passed") 
# elif grade < 70: 
#  print("You got a good pass") 
# else: 
#  print("You got an excellent pass") 
 
 
#Exercise -6 : Compare Temperature 
# ----------------

# temperature1=40
# temperature2=78
# #using if statement to check if the temperatures are equal or not 
# if(temperature1==temperature2):
#     print("Both Temperature1 and 2 are equal")
# else:
#     print("The 2 given temperature arenot equal")


#Exercise-1  Python-list 
#Creating a string list 
# ----------------


# city_list=["Glasgow", "London", "Edinburgh"]
# print(city_list);
 
 
#Exercise -2 Accessing a List in Python 
# ----------------

# city_list=["Glasgow", "London", "Edinburgh"]
# third_item=city_list[2] #Numbering starts from 0 so third item is 2. 
# print(third_item)
# print(city_list[-2:]) #Prints Last 2 cities from the city_list 



#Exercise -4 Summary Task : Task Create, Access and Modify Lists: 
#--------------------------------------------------------------------
# colors=["red","yellow","green"] #created list of 3 colors as mentioned 
# #Printing a entire list 
# print(colors)
# #accessing 2nd elements and printing it 
# second_element=colors[1]
# print(second_element)
# #Modify the 1st element of the list and write another 
# colors[0]="blue" #modification of 1st element 
# print(colors) # In this print we can observe blue replaced red color 
#  #checking and printing a length of a list
 
# length=len(colors) # This line checks the length 
# print(length) # This prints the length of the list 

# #To check if red color is in the list or not 
# if "red" in "colors":
#     print("Red color is in the list ")
# else:
#     print("red color is not in the list ")
    
# #make new variable selected_colors with 2nd and 3rd elements of the list 
# selected_colors=colors[1:3]
# print(selected_colors) #print selected colors from the list 



#Python Loops 
#Exercise -1 While loops 
#--------------------------------------------------------------------

# i = 10 
# while i < 60:  #Starts with 10 and increament with 5 untll 100
#  print(i) 
#  i += 5

#Exercise -2 For loops 
#--------------------------------------------------------------------
# city_list=["Glasgow", "London", "Edinburgh"]
# for city in city_list:
#     print(city)


#Exercise -3  Loop Keywords: Range, break and continue 
#--------------------------------------------------------------------

# for i in range(5):
#     print(i)
#     if i==3:
#         break #This prints the 0 to 5 but when i becomes equal to 3 it will break the loop 
    

# for i in range(5): # Use of continue keyword 
#  if i == 2: 
#   continue 
#  print(i) 


#Exercise -4  Summary Task 
#Task : even numbers 
#--------------------------------------------

# numbers =list(range(1,11))
# for number in numbers:
#     if number%2==0:
#         print("even number")
#     else:
#         print("odd number")
        
        
#Task : sum of squares 
#--------------------------------------------

# sum_of_squares = 0
# for i in range(1, 6):
#    sum_of_squares += i ** 2
# print("Sum of squares from 1 to 5 is:", sum_of_squares)



#Task : Countdown
#--------------------------------------------
# countdown=10
# while countdown>=1:
#  print(countdown)
#  countdown-=1
 
# print("Liftoff")
 
 
#  Task: User Input and Conditional Statements 
#--------------------------------------------

# age = int(input("Enter your age: "))

# # Use conditional statements to determine the age category
# if age < 18:
#     print("You are a minor.")
# elif age <= 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")




#Task: Temperature Converter 
#----------------------------------------



#Get User Input in celcius 
celsius = float(input("Enter temperature in Celsius: "))

# Conversion formulae 
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Print the results of both converted 
print(f"Temperature in Fahrenheit: {fahrenheit} °F")
print(f"Temperature in Kelvin: {kelvin} K")
