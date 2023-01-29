def month_to_season():
    n = int(input())
    if n == 12 or 0<n<3:
        print("Зима")
    elif 2<n <6:
        print("Весна")
    elif 5<n<9:
        print("Лето")
    elif 8<n<12:
        print("Осень")
month_to_season()