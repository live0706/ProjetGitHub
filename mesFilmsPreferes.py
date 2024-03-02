def doubleNo(no):
    return no * 2
def main():
    noDepart = int(input("Saisissez un nombre : "))
    for i in range(5):
        noDepart = doubleNo(noDepart)
        print(noDepart)


main()
