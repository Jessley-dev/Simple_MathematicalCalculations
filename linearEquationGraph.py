import matplotlib.pyplot as plt
import numpy as np

print("===LINEAR FUNCTION PLOTTER===")
print("Do you have the function or the points of the graph")

while True:
    choice_1 = input("Input the word 'function' if you have function or "
"input the word 'points' if you have the points: ").strip().lower()

    if choice_1 == "function":

        print("A linear function is written in y = mx + c format where")
        print("y is the y component on the y-axis")
        print("m is the slope or gradient of the graph")
        print("x is the x component on the x-axis")
        print("c is the y-intercept")

        try:
            m = float(input("Input the slope: "))
            c = float(input("Input the y-intercept: "))
            
            while True:
                x_lowlim = float(input("Input the x lower limit in relation to the desired y lower limit on the graph: "))
                x_upplim = float(input("Input the x upper limit in relation to the desired y upper limit on the graph: "))

                if x_upplim > x_lowlim:
                    x = np.linspace(x_lowlim, x_upplim, 100) 
                    y = (m * x) + c 
                    break

                else:
                     print("Invalid the lower limit must always be smaller than the upper limit.")
                     continue

            plt.figure()    
            plt.plot(x, y, color="blue", linestyle="--", linewidth=2)
            plt.axhline(y = 0)
            plt.axvline(x = 0)
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.xlabel("x-axis", fontsize=12)
            plt.ylabel("y-axis", fontsize=12)
            plt.title(f"y = {m}x + {c}")
            plt.show()
            
        except ValueError:
                print("Please input real numbers")
                continue

    elif choice_1 == "points":
        print("To draw the graph you must enter at least two coordinate points which are" \
        " (x1,y1) and others to be (x2,y2)")
        try:
            while True:
                x1 = float(input("Enter the x component of the x-axis on the first point: "))
                y1 = float(input("Enter the y component of the y-axis on the first point: "))
                x2 = float(input("Enter the x component of the x-axis on the second point: "))
                y2 = float(input("Enter the y component of the y-axis on the second point: "))

            
                if x1 == x2 and y1 == y2:
                    print("Invalid because they are the same points")
                    continue
                elif x1 == x2:
                    print("Your graph is a vertical line which means its slope is undefined")
                    
                    while True:
                        y_lowlim = float(input("Input the y lower limit on the graph: "))
                        y_upplim = float(input("Input the y upper limit on the graph: "))

                        if y_lowlim < y_upplim:

                            plt.figure()
                            plt.axvline(x = x1, color="red", linestyle="--", linewidth=2)
                            plt.ylim(y_lowlim, y_upplim)
                            plt.grid(True, linestyle="--", alpha=0.5)
                            plt.xlabel("x-axis", fontsize=12)
                            plt.ylabel("y-axis", fontsize=12)
                            plt.title(f"x = {x1}")
                            plt.show()
                            break
                

                        else:
                            print("Please the y lower limit must be smaller than the y upper limit on the graph")
                            continue
                    break
                else:
                    m = (y2-y1) / (x2-x1)
                    c = (y1) - (m * x1)

                    x_lowlim = float(input("Input the x lower limit in relation to the desired y lower limit on the graph: "))
                    x_upplim = float(input("Input the x upper limit in relation to the desired y upper limit on the graph: "))

                    if x_lowlim >= x_upplim:
                        print("The lower limit must always be smaller than the upper limit")
                        continue
                             
                    else: 
                        x = np.linspace(x_lowlim, x_upplim, 100)
                        y = (m * x) + c

                        plt.figure()    
                        plt.plot(x, y, color="blue", linestyle="--", linewidth=2)
                        plt.axhline(y = 0)
                        plt.axvline(x = 0)
                        plt.grid(True, linestyle="--", alpha=0.5)
                        plt.xlabel("x-axis", fontsize=12)
                        plt.ylabel("y-axis", fontsize=12)
                        plt.title(f"y = {m}x + {c}")
                        plt.show()
                        break
 

        except ValueError:
             print("Please input real number")
             continue
    else:
            print("Please input a clear input")
            continue

    choice_2 = input("If you want to leave type yes, if you want to stay type anything: ").strip().lower()
    if choice_2 == "yes":
         break