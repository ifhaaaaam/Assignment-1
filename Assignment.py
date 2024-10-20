#maximum between two numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if num1 > num2:
    print("The maximum number is:", num1)
else:
    print("The maximum number is:", num2)



#maximum between three numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print("The maximum number is:", a)
elif b >= a and b >= c:
    print("The maximum number is:", b)
else:
    print("The maximum number is:", c)
    
    
    #whether number is positive negative or zero
    
    num = int(input("Enter a number: "))
    
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
        
        
        
      #whether number is divisible by 5 and 11  

        number = int(input("Enter a number: "))
        
        if number % 5 == 0 and number % 11 == 0:
            print("The number is divisible by 5 and 11.")
        else:
            print("The number is not divisible by 5 and 11.")
            
            
            
     #whether number is even or odd       

    n = int(input("Enter a number: "))
    
    if n % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
        
        
       #whether a year is leap year or not 
        

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

            
   #whether a charecter is alphabet or not 
            

char = 'A'

if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
    print(char, "is an alphabet")
else:
    print(char, "is not an alphabet")


  

#Check Vowel or Consonant

alphabet = 'a'

if alphabet in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

#Check Character Type

char = '@'

if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")

# Check Uppercase or Lowercase

char = 'A'

if char.isupper():
    print("Uppercase")
else:
    print("Lowercase")

# Week Number to Week Day

week_number = 3

if week_number == 1:
    print("Monday")
elif week_number == 2:
    print("Tuesday")
elif week_number == 3:
    print("Wednesday")
elif week_number == 4:
    print("Thursday")
elif week_number == 5:
    print("Friday")
elif week_number == 6:
    print("Saturday")
elif week_number == 7:
    print("Sunday")
else:
    print("Invalid week number")

# Month Number to Days

month_number = 2

if month_number in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month_number in [4, 6, 9, 11]:
    print("30 days")
elif month_number == 2:
    print("28 or 29 days")
else:
    print("Invalid month number")

# Count Total Number of Notes

amount = 1350
notes_500 = amount // 500
amount = amount % 500
notes_100 = amount // 100
amount = amount % 100
notes_50 = amount // 50
amount = amount % 50
notes_10 = amount // 10
amount = amount % 10
notes_5 = amount // 5
amount = amount % 5
notes_1 = amount // 1

total_notes = notes_500 + notes_100 + notes_50 + notes_10 + notes_5 + notes_1
print("Total number of notes:", total_notes)

# Check Validity of Triangle by Angles

angle1 = 60
angle2 = 60
angle3 = 60

if angle1 + angle2 + angle3 == 180:
    print("Triangle is valid")
else:
    print("Triangle is not valid")

# Check Validity of Triangle by Sides

side1 = 3
side2 = 4
side3 = 5

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Triangle is valid")
else:
    print("Triangle is not valid")

# Check Type of Triangle

side1 = 3
side2 = 3
side3 = 5

if side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# Find Roots of a Quadratic Equation

a = 1
b = -3
c = 2

discriminant = b * b - 4 * a * c

if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2 * a)
    root2 = (-b - discriminant**0.5) / (2 * a)
    print("Roots are real and different:", root1, root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("Roots are real and the same:", root)
else:
    print("Roots are complex")

# Calculate Profit or Loss

cost_price = 100
selling_price = 120

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No profit, no loss")



  # Calculate Percentage and Grade

physics = 85
chemistry = 78
biology = 92
mathematics = 88
computer = 76

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print("Percentage:", percentage)
print("Grade:", grade)

# Calculate Gross Salary

basic_salary = 15000

if basic_salary <= 10000:
    hra = 0.20 * basic_salary
    da = 0.80 * basic_salary
elif basic_salary <= 20000:
    hra = 0.25 * basic_salary
    da = 0.90 * basic_salary
else:
    hra = 0.30 * basic_salary
    da = 0.95 * basic_salary

gross_salary = basic_salary + hra + da
print("Gross Salary:", gross_salary)

#Calculate Electricity Bill

units = 320
bill = 0

if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 50 * 0.50 + (units - 50) * 0.75
elif units <= 250:
    bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
else:
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

surcharge = bill * 0.20
total_bill = bill + surcharge

print("Total Electricity Bill:", total_bill)



                
                
                
                
                
            
            
            
            
            
