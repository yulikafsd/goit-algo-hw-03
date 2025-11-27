def khanoi(n, source, target, auxiliary, rods):
    if n == 1:
        disk = rods[source].pop()
        rods[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {rods}")
    else:
        khanoi(n - 1, source, auxiliary, target, rods)
        disk = rods[source].pop()
        rods[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {rods}")
        khanoi(n - 1, auxiliary, target, source, rods)


n = 5
rods = {"A": list(range(n, 0, -1)), "B": [], "C": []}

print(f"Початковий стан: {rods}")
khanoi(n, "A", "C", "B", rods)
print(f"Кінцевий стан: {rods}")
