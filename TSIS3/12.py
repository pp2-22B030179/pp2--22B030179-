def histogram(data):
    for value in data:
        print('*' * value)


a = list(map(int, input("List: ").split()))
histogram(a)