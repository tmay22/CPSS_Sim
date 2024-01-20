import Setup


def main():

    print("")
    setupOption= input("Choose Setup Option: \n 1. Default \n 2. Small (10 pers) \n...etc \n")
    

    print("You Selected " + setupOption)
    
    setupOutput = Setup.build(setupOption)

if __name__ == "__main__":
    main()