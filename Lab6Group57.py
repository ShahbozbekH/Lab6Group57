def encoder(password):
    res = [int(x) for x in str(password)]
    new_list = [n + 3 for n in res]
    enpass = ""
    for i in new_list:
        if i == "10":
            i = 0
        if i == "11":
            i = 1
        if i == "12":
            i = 2
        enpass += str(i) + ""
    print("Your password has been encoded and stored! ")
    return enpass
def decoder(enpass):
    res = [int(x) for x in str(enpass)]
    decodepass = [n- 3 for n in res]
    depass = ""
    for i in decodepass:
        depass += str(i) + ""
    print(f"The encoded password is {enpass}, and the original password is {depass}")
    return depass
if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menu = input("Please enter an option: ")
        if menu == "1":
            password = int(input("Please enter your password to encode: "))
            encoder(password)
        elif menu == "2":
            enpass = encoder(password)
            decoder(enpass)
        elif menu == "3":
            break