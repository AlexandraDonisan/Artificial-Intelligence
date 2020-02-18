from Cotroller import Controller


def main():
    c = Controller("parameter.in")
    v = c.run()
    print("The result is: " + str(v))


main()
