def main():
    print("\nThis program converts celsius to fahrenheit, and vice versa. \n")
    print("Celsius temperature\tfahrenheit temperature\n")
    for c in range (0, 101, 10):
        f = 9/5 * c + 32
        print(c,"°C","\t\t\t\t", f,"°F")
        if c == 101:
            break

    def ctf():
        for i in range(5):
            cel = eval(input("What is the Celsius temperature? "))
            fah = 9 / 5 * cel + 32
            print("The temperature is", fah, "degrees Fahrenheit.")
            print(" ")
            if i == 6:
                break

    def ftc():
        for i in range(5):
            fah = eval(input("What is the fahrenheit temperature? "))
            cel = (fah-32)*5/9
            print("The temperature is", cel, "degrees celsius.")
            print(" ")
            if i == 6:
                break

    uc = input("\nDo you want to convert Celsius to Fahrenheit (Press 'c'), Fahrenheit to Celsius (Press 'f'), or quit (Press 'e'): ")
    while uc !='e':
        if uc == 'c': 
            ctf()
            uc = input("\nDo you want to convert Celsius to Fahrenheit (Press 'c'), Fahrenheit to Celsius (Press 'f'), or quit (Press 'e'): ")

        elif uc == 'f':
            ftc()
            uc = input("\nDo you want to convert Celsius to Fahrenheit (Press 'c'), Fahrenheit to Celsius (Press 'f'), or quit (Press 'e'): ")    

        elif uc !='c' and uc !='f':
            print("**Please enter a valid input**")
            uc = input("\nDo you want to convert Celsius to Fahrenheit (Press 'c'), Fahrenheit to Celsius (Press 'f'), or quit (Press 'e'): ")

    print("Exiting")
main()