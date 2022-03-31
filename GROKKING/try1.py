def countdown(x):
    for i in range(x):
        return x, countdown(x - 1)


print(countdown(3))