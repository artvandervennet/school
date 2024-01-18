def plus_min_som(aantal):
    som = 0
    for i in range(1, aantal + 1):
        if i % 2 == 1:
            som += i
        else:
            som -= i
    print(som)
plus_min_som(7)