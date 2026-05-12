while True:
#_______________________________________________________________________________________
    print("HowOldAmI")

    from datetime import date
    import calendar
    today = date.today()

    print("Today's date is: ", today, "\n")
    #________________________________________________________________________________________
    ty = today.year
    tm = today.month
    td = today.day

    print("\nPlease enter your date of birth.\n")

    oy = int(input("What year were you born?    YYYY   : "))
    om = int(input("What month were you born?   MM     : "))
    od = int(input("What day were you born?     DD     : "))

    real_ty = ty
    real_tm = tm
    real_td = td


    if td < od:
        tm = tm - 1
        td = td + calendar.monthrange(ty, tm)[1]
        #td = td + 30

    if tm < om:
        ty = ty - 1
        tm = tm + 12

    if ty < oy:
        print("\nYou have not been born yet.\n")
        g = input("Run again? (y/n): ")
        if g == "n":
            break

    years = ty - oy
    months = tm - om
    days = td - od

    print("*****************************************************************************")
    print("\nYou are ", years, " years, ", months, " months, and ", days, " days old.\n")

    birth = date(oy, om, od)
    today = date(real_ty, real_tm, real_td)
    age = today - birth
    print("You are ", age.days, " days old.\n")
    again = input("Run again? (y/n): ")
    if again == "n":
        break