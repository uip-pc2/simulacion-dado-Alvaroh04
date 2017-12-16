def impar():
    for i in range(51):
        if i % 2 == 1:
            yield (i)


if __name__ == '__main__':
    imp = impar()
    try:
        for i in range(51):
            print(next(imp))
    except Exception as e:
        print(e)