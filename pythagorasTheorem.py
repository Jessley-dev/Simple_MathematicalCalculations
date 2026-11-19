import numpy as np 


print("===THE PYTHAGORAS THEOREM===")
print("Enter hy to calculate hypothenus")
print("Enter b to calculate base")
print("Enter h to calculate height")


while True:
    side = input("Input the side you want to calculate(hy, b, or h): ").strip().lower()
    if side == "hy":
        try:
            b_hy = float(input("Input the base: "))
            h_hy = float(input("Input the height: "))
            
            if b_hy > 0 and h_hy > 0:
                hy_sol =  np.sqrt (b_hy**2 + h_hy**2)
                print("The hypothenus is: ",hy_sol)
            
            else:
                print("Both values must be greater than zero")
                continue

        except ValueError:
            print("Please enter valid numbers")
            continue

    elif side == "b":
        try:
            hy_b = float(input("Input the hypothenus: "))
            h_b = float(input("Input the height: "))
            
            if hy_b > h_b > 0:
                b_sol = np.sqrt (hy_b**2 - h_b**2)
                print("The base is: ",b_sol)
                
            else:
                print("Hypothenus must be greater than height and height must be greater than zero")
                continue

        except ValueError:
            print("Please enter valid numbers")
            continue

    elif side == "h":
        try:
            hy_h = float(input("Input the hypothenus: "))
            b_h = float(input("Input the base: "))
            
            if hy_h > b_h > 0:
                h_sol = np.sqrt (hy_h**2 - b_h**2)
                print("The height is: ",h_sol)

            else:
                print("Hypothenus must be greater than base and base must be greater  than zero")
                continue

        except ValueError:
            print("Please enter valid numbers")
            continue

    else:
        print("Your Input is invalid")
        continue   
  

    choice = input("Type yes to exit or type anything to continue: ").strip().lower()

    if choice == "yes":
        print("Done")
        break

    
