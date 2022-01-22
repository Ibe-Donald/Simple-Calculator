#!/usr/bin/env python
# coding: utf-8

# # A SIMPLE CALCULATOR

# In[ ]:


#User enters an input of the operation his or she requires to be carried out


# In[ ]:


user_operation  = input("Enter the Operation you wish to carry out :")

#next program makes use of the if condtional statement 

if (user_operation == "add"):
    first_num = float(input("Enter a number : "))
    second_num = float(input("Enter another number : "))
    #it then takes the addition of both numbers
    result = first_num + second_num
    print(result)
    
elif (user_operation == "subtraction") :
    first_num = float(input("Enter a number : "))
    second_num = float(input("Enter another number : "))
     #it then takes the subtraction of both numbers
    result = first_num - second_num
    print(result)   

elif (user_operation == "multiply") :
    first_num = float(input("Enter a number : "))
    second_num = float(input("Enter another number : "))
     #it then takes the multiplicatioN of both numbers
    result = first_num * second_num
    print(result) 
    
elif (user_operation == "division") :
    first_num = float(input("Enter a number : "))
    second_num = float(input("Enter another number : "))
     #it then takes the division of both numbers
    result = first_num / second_num
    print(result)  
    
elif (user_operation == "exponetial") :
    first_num = float(input("Enter a number : "))
    second_num = float(input("Enter another number : "))
     #it then takes the first number to the power of the second number
    result = first_num ** second_num
    print(result)
    
else :
    print("You will need to renter")
    


# In[ ]:





# In[ ]:




