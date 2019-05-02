def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    print("Hello, %s %s!"%(first_name,last_name))
    print()

    food = ['Apples', 'Cookies', 'Ice cream', 'Cereal']
    for food in food:
        print (food)

    print()
    aiy = float(input("How old are you? "))
    diy = aiy * 365
    wiy = aiy * 52.1429
    miy = aiy * 12
   
    print("You're at least", diy, "days old.")
    print("You're at least", wiy, "weeks old.")
    print("You're at least", miy, "months old.")

    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    ad = input("Enter a adjective: ")
    place = input("Enter a place: ")
   
    print("Take your %s %s and %s it at the %s"%(ad, noun, verb, place))

main()

