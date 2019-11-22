# create a mapping of state to abbrevation 
states = {'Oregon': 'OR','Florida': 'FL','California': 'CA','New York': 'NY','Michigan': 'MI'}

#create abasic set of states and some cities in them
cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

#add some new cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some citites
print("-"*20)
print("NY state has: ",cities['NY'])
print("OR state has: ",cities['OR'])

#Print some states
print("-"*20)
print("Michigan's abbrevation is: ", states['Michigan'])
print("Florida's abbrevation is: ", states['Florida'])

# DO it by using the states then cities 
print("-"*20)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbrevation
print("-"*20)
for state, abbrev in states.items():
	print("{} is abbrevated {} ".format(state, abbrev))

#print every city in state
print("-"*20)
for abbrev, city in cities.items():
	print("{} has city {}".format(abbrev, city))

#now to do both at the same time
print("-"*20)
for state, abbrev in states.items():
	print("{} state is abbrevated {} and has city {}".format(state, abbrev, cities[abbrev]))

#Safely get an abbrevation by states that might not be their
print("-"*20)
state  = states.get('Texas', None)

if not state:
	print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', 'does not exist\n\n')
print("The city for the state TX is: {}".format(city))