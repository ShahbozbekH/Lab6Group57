#Shahbozbek Hakimov
def encoder(password):
    res = [int(x) for x in str(password)]
    new_list = [n + 3 for n in res]
    enpass = ""
    #shifts password upwards by 3 integers#
    for i in new_list:
        if i == 10:
            i = 0
        if i == 11:
            i = 1
        if i == 12:
            i = 2
        enpass += str(i) + ""
    print("Your password has been encoded and stored! ")
    return enpass
    #returns enpass to be later used#
def decoder(enpass):
    enc_password = []
    for num in enpass:
        enc_password.append(int(num))
    dec_password = []
    for value in enc_password:
        value -= 3
        if value == -1:
            value = 9
        if value == -2:
            value = 0
        if value == -3:
            value == 1
        dec_password.append(str(value))
    password_dec = ''.join(dec_password)
    print(f'The encoded password is {enpass}, and the original password is {password_dec}')
    return password_dec

if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menu = input("Please enter an option: ")
        if menu == "1":
            password = input("Please enter your password to encode: ")
            encoder(password)
        elif menu == "2":
            enpass = encoder(password)
            decoder(enpass)
        elif menu == "3":
            break
        #prints menu and allows for input from the user#
