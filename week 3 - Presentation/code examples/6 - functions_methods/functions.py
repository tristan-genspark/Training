

# the code below is not executed unless called
def ThisIsAFunction(a,b):
    # this function adds two values and returns a sum
    print("Doing some repeatable task")
    c =  "( " + a + "  " + b + " )";
    c = c[::-1]; # Reverse it
    return c;





# Call the function
returnvalue = ThisIsAFunction("Hello","World");

print("The return value is here \n\n " + returnvalue)
