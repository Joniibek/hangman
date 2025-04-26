nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    print("Введи X для выхода")
    a = input("Угадайте число из списка: ")
    if a == "X":
        print("Спасибо за участие!")
        break
    a = int(a)
    for i in range(0, len(nums)):
        if a == nums[i]:
            print("Вы угадали!")
            break
    else:
        print("Неверно, попробуйте ещё :(")
        



