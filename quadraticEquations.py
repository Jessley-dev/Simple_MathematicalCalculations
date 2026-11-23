import numpy as np
print("===QUADRATIC EQUATION SOLVER===")
print("A quadratic equation is written as " \
"a(x^2) + bx + c = 0")
while True:
    try:   
        a = float(input("Input a: "))
        b = float(input("Input b: "))
        c = float(input("Input c: "))
        if a == 0:
            print("Sorry, a cannot be zero")
            continue
        else:
            delta = (b**2) - (4*a*c)
            if delta < 0:
                print("The solution set is not in a set of real numbers")
                
            elif delta == 0:
                x_1 = float((-b) / (2*a))
                print(f"The solution consists of only one value x: {x_1:.3f}")

            else:
                x_2 = float(((-b) + (np.sqrt(delta))) / (2*a))
                x_3 = float(((-b) - (np.sqrt(delta))) / (2*a))
                print(f"The solutions consists on two values of x which are {x_2:.3f} and {x_3:.3f}")
            
        choice = input("Type yes if you want to exit or type anything to continue: ").strip().lower()
        if choice == "yes":
            break
    except ValueError:
        print("Please enter real numbers")