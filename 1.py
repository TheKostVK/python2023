
def compare_numbers():
    num_1 = float(input("Введите произвольное число: "))
    limit = float(input("Введите пограничное число: "))

    if num_1 < limit:
        print(f"{num_1} меньше, чем пограничное число {limit}")
    elif num_1 > limit:
        print(f"{num_1} больше, чем пограничное число {limit}")
        if num_1 > limit * 3:
            print(f"{num_1} больше, чем пограничное число {limit} более, чем в 3 раза")
    else:
        print(f"{num_1} равно пограничному числу {limit}")


if __name__ == '__main__':
    compare_numbers()
