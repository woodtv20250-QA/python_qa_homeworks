lst = ["🍇", "🍑", "🍐", "🍊", "🍌", "🍎"]

length = len(lst)

for x in range(0, length):
    if x == 0:
        print(lst[x])

for x in range(0, length):
    if x == (length - 1):
        print(lst[x])
