print("===CELSIUS DEGREES TO FAHRENEIT DEGREES===")
try:
    celsius = float(input("Input the celsius degrees(numerals only): "))
    fahreneit = ((9 * celsius) / 5) + 32
    print(f"The degrees fahreneit of the given degrees celsius is {fahreneit:.3f}°F")
except ValueError:
    print("Input valid input please")