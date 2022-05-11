cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = min(cars,drivers)#这里跟书上不一样，用min函数来表达会更加贴切
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are",cars,"cars availabe")
print("There are only",drivers,"drivers availabe")
print("There will be",cars_not_driven,"not driven")
print("We can transport",carpool_capacity,"prople today")
print("We have",passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in a car")
print("It can put all passengers?")

if(average_passengers_per_car < space_in_a_car):
    print("yes")
else:
    print("no")
