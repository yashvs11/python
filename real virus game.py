country_list = []

NZ = ("New Zealand")
Aus =("Australia")
country_list.append(NZ)
country_list.append(Aus)
nz = (20)
aus = (20)
def add_country():
    while True:
        country = input("name of country you want to add ?")
        if country != "done":
            infected = int(input("how many people affected ?"))

        else:
            break
        newlist = [country]
        i = country_list.append(newlist)
        for i in country_list:
            print(i)

def help():
    help_country = "which country would you like to help? choose from the following"
    while True:
        for i in country_list:
            print(i)
        okk = (input(help_country))
        if okk in country_list:
            return advance_day(okk)
        elif okk is not NZ:
            print("invalid error try again")

def advance_day(f):
    print("**NEW DAY**")
    if f == "New Zealand":
        if nz >= 20:
            new = nz - 20
            new_auss = aus + 20
            lock = ("lockdown")
            print(str(f) +"currently has " + str(int(new)) + " not is in " + str(lock))
            print("Australia currently has " + str(int(new_auss)) + " not is in " + str(lock))
            return help()


    elif f == "Australia":
        if aus >= 20:
            neww_aus = aus -20
            nzz = nz + 20
            lockdown = ("lockdown")
            print("New Zealand currently has " + str(int(nzz)) + " is in " + str(lockdown))
            print(str(f) + "currently has " + str(int(neww_aus)) + " not is in " + str(lockdown))
            return help()

    print("**END DAY**")



def main():
    country = input("if you would like to type in a country type in \"add\" or type in \"done\" and click enter")
    if country.lower() == "add":
        add_country()
    elif country.lower() == "done":
        help()


if __name__ == "__main__":
    main()
