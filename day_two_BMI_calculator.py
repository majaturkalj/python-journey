# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_height = float(height)
number_weight = float(weight)
BMI = number_weight / (number_height * number_height)
print(round(BMI))