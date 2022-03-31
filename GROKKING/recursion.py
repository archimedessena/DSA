# While loop 
#When you write a recursive function, you have to 
###The recursive case is when the function calls itself. 
#the base case is when the function doesn’t call 
#itself again … so it doesn’t go into an infinite loop.


def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")

# The recursion form of that code, every recursive function has two part the base case and the recursive case
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) # Recursion
        elif item.is_a_key():
            print("found the key!")





# the correct form of the code above
def countdown(i):
    if i <= 0: # Base case
        return i
    else: # Recursive Base
        countdown(i-1)


# Call stack with recursion
def fact(x):
    if x == 1:
        return 1
    else: 
        return x * fact(x - 1)

    
print(fact(5))