def quiz(numheads, numlegs):
    cnt_rab = int((numlegs - 2*numheads) / 2)
    cnt_chick = int(numheads - cnt_rab)
    print(f"Количество зайцев {cnt_rab}, количество куриц {cnt_chick}")
x = int(input("Введите количество голов: "))
y = int(input("Введите количество ног: "))
quiz(x , y)