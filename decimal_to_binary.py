int_str = input("Insert a positive integer please: ")

my_int = int(int_str)

bin_str = ""

if my_int == 0:
    bin_str = '0'

elif my_int < 0:
    print("Sorry, that is not a valid number.")

else:

    while my_int > 0:

        if my_int % 2 == 0:
            bin_str = '0' + bin_str

        else:
            bin_str = '1' + bin_str

        my_int //= 2

print(bin_str)
