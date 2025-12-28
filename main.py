# Restaurant Selector

# asking user for input
vegetarian = input("Is anyone in your party a vegetarian?")
vegan = input("Is anyone in your party a vegan?")
halal = input("Is anyone in your party halal?")

# Restaurant options
print("Here are your restaurant choices:")

# Check if no dietary restrictions
if vegetarian.lower() == "no" and vegan.lower() == "no" and halal.lower() == "no":
    print("Good Burger")

# Check for vegetarian but no other dietary restrictions
if vegetarian.lower() == "yes" and vegan.lower() == "no" and halal.lower() == "no":
    print("Main Street Pizza")

# Check for vegetarian and vegan but not halal
if (vegetarian.lower() == "yes" or vegan.lower() == "yes" and halal.lower() == "no") and not (vegetarian.lower() == "yes" and vegan.lower() == "yes" and halal.lower() == "yes"):
    print("Chef's Kitchen")

 # Check if any dietary restrictions present
if vegetarian.lower() == "yes" or vegan.lower() == "yes" or halal.lower() == "yes":
    print("Yemeni Cafe\nMasala Grill")

else:print("No suitable restaurants found for your party's dietary preferences.\n \"Please enter either yes or no.\"") # when the user enters anything other than 'yes' or 'no', it will display this message
    
