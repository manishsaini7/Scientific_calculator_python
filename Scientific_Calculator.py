import math

while True:
    print("\nChosse the amath operation.\n\n0 - Additioin.\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raise to a power\n6 - square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")     
    oper = input("\nYour option from the menu: ")
    #Addition
    if oper == "0":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))
        
        print("\nThe Result of Additioin is:" + str(val1+val2)+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break    
    
    #Subtraction
    elif oper == "1":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))
        
        print("\nThe Result of Subtraction is:" + str(val1-val2)+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
            
    #Multiplication
    elif oper == "2":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))
        
        print("\nThe Result of Multiplication is:" + str(val1*val2)+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
            
    #Division
    elif oper == "3":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))
        
        print("\nThe Result of Division is:" + str(val1/val2)+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
            
    #Modulo  
    elif oper == "4":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))
        
        print("\nThe Result of Modulo is:" + str(val1%val2)+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
    
    #raisetothepower    
    elif oper == "5":
        val1 = float(input("\nEnter the base: "))
        val2 = float(input("\nEnter the Power: "))
        
        print("\nThe Result of Raise to the power is:" + str(math.pow(val1,val2))+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
    
    #Square root
    elif oper == "6":
        val1 = float(input("\nEnter the value for square root: "))
        
        print("\nThe Result of Square Root is:" + str(math.sqrt(val1))+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
            
    #Logarithm
    elif oper == "7":
        val1 = float(input("\nEnter the value for Logarithm to base 2: "))
        
        print("\nThe Result of Raise to the power is:" + str(math.log(val1, 2))+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
    
    #Sine
    elif oper == "8":
        val1 = float(input("\nEnter the value(in degrees) for calculating the sine: "))
        
        print("\nThe Result of Sin is:" + str(math.sin(math.radians(val1)))+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
    
    #Cosine
    elif oper == "9":
        val1 = float(input("\nEnter the value(in degrees) for calculating the cosine:"))
        
        print("\nThe Result of Cosine is:" + str(math.cos(math.radians(val1)))+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
            
    #Tangent
    elif oper == "10":
        val1 = float(input("\nEnter the value(in degrees) for calculating the tangent:"))
        
        print("\nThe Result of Sin is:" + str(math.tan(math.radians(val1)))+ "\n")
        
        back = input("\nGo back to the main menu?(y/n)")
        if(back == "y"):
            continue
        else: 
            break
     
    #Handling invalid Inputs
    else:
        print("\nInvalid Options.\n")
        continue
       
#End of Program