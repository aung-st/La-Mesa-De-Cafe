import database


def menu():

    MENU_PROMPT = """\n-- La Mesa De Café --

    Please choose one of these options:

    1) Add a new bean
    2) See all beans
    3) Find a bean by name
    4) See best preperation method for a bean
    5) Exit
    Option: """

    connection = database.connect()
    database.create_tables(connection)

    while(user_input := int(input(MENU_PROMPT))) != 5:
        if user_input == 1:

            name = input("Enter bean name: ")
            method = input("Enter preperation style: ")
            rating = int(input("Enter your rating (0-100): "))

            database.add_bean(connection, name, method, rating)

        elif user_input == 2:

            beans = database.get_all_beans(connection)

            print("\nYour Selection:\n")
            print("-------Name---------------Method------Rating")

            for bean in beans:
                print(f"({bean[1].ljust(4)})      ({bean[2].ljust(15)}) - {bean[3]}/100")

        elif user_input == 3:

            name = input("Enter bean:")
            beans = database.get_beans_by_name(connection, name)
            print("\n-------Name---------------Method------Rating")
            for bean in beans:
                print(f"({bean[1]})      ({bean[2]}) - {bean[3]}/100")


        elif user_input == 4:

            name = input("Enter Bean:")
            best_method = database.get_best_prep_for_bean(connection, name)

            print(f'Best method for {name} is {best_method[2]}')

        elif user_input == 5:
            exit()

        else:
            print("Invalid input! Please try again!")
        

menu()
