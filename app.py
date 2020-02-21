print(''' 
Hello, This is a simple interactive program that will allow you to prints out your name, 
your favorite color, calculate your age and calculate your weight from kilograms to tons 
''')
print('Let us Begin')
name = input('What is your name? ')
colour = input('What is your favourite Colour?')
birth_year = input('Please enter your Birth Year: ')
weight_kgs = input('Please enter your Weight in Kilograms= ')
print('Hello ' + name)
print('Your Favourite colour is ' + colour)
age = 2020 - int(birth_year)
print("You are " + str(age) + 'years old')
weight_tons = int(weight_kgs) / 1000
print('Your Weight in Tons is = ' + str(weight_tons))
