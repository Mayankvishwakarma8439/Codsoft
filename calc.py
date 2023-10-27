while True:
        while True:
            try:
                print("\n......CALCULATOR......")
                print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit")
                choice=int(input("\nChoose the Operation to be performed(1-5): \n"))
                
            except Exception as e:
                    print("\nInvalid Choice!!")
                    break
            try:
                 if(choice==1):
                    print("ADDITION:")
                    A=float(input("Enter the 1st number:"))
                    B=float(input("Enter the 2nd number:"))
                    print("\nA + B = ",A+B)

                 elif(choice==2):
                    print("SUBTRACTION:")
                    A=float(input("Enter the 1st number:"))
                    B=float(input("Enter the 2nd number:"))
                    print("\nA - B = ",A-B)
    
                 elif(choice==3):
                    print("MULTIPLICATION:")
                    A=float(input("Enter the 1st number:"))
                    B=float(input("Enter the 2nd number:"))
                    print("\nA X B = ",A*B)
                
                 elif(choice==4):
                    print("DIVISION:")
                    A=float(input("Enter the 1st number:"))
                    B=float(input("Enter the 2nd number:"))
                    if(B==0):
                        print("\nNot defined...")
                    else:
                        print("\nA / B = ",A/B)
        
                 elif(choice==5):
                    print("\nThank You for using the Calculator....")
                    exit()
            
                 else:
                    print("\nChoose an integer from 1 to 5 !!")
                    break
            except Exception as e :
                print("\nInvalid Input!!!")
                break
