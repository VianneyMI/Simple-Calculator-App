from memory import expression
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    #equation.set(expression) 
    return expression
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        #equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
        return total
    # if error is generate then handle 
    # by the except block 
    except: 
  
        #equation.set(" error ") 
        expression = "" 
        return "error"
  
# Function to clear the contents 
# of text entry box 
def clear_field(): 
    global expression 
    expression = "" 
    return expression
    #equation.set("") 