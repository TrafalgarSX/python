def multiargs(first, *args, second, **kwargs):
    print(first)
    print(args)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])


if __name__ == '__main__':
    multiargs(1, 2, 3, 4, second=5, name='guoyawen', age='25')
