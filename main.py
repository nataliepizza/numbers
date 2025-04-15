# if conditionals
# if statements are used to check if a condition is true or false
# if condition is true, do something
# if condition is false, do something else

# if conditional statemeents always start with if 
# and depend on a boolen value (true or false)
# example
classStarted = True #boolen variable
if classStarted:
    print("classs has started")
else:
    print("class has not started")

# logical and comparison operators
# == equal to
# != not equal to
age = 10
if age >= 18:
    print("you are an adult")
elif age == 17:
    print("you are almost an adult")
else:
    print("you are a minor")
number = int(input("what is your number?"))
if number % 2 == 0:
    print(F"{number} is even ") 
else:
    print(f"{number}") is odd 