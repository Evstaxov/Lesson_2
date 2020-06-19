my_list = [4, 3, 3, 2, 1]

while True:
    print(f"Current rating: {my_list}")
    number = input("Enter rating number or 111 to finish - ")
    if number.lstrip('-').isdigit() and number != "111":
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), float(number))
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    if param < i:
                        param = i
                        n_param = n
                else:
                    n_param = n + 1
            my_list.insert(n_param, number)
    elif not number.isdigit():
        print("Enter number please")
    else:
        break