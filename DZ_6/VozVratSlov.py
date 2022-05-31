def first_world(world="Hello World"):
    if type(world) == str:
        one_w = world.split()
        print(one_w[0])
    else:
        print(False, type(world))


sentence = input('Введите предложение: ')
first_world(sentence)


def middle(*h):
    print(int(sum(h) / len(h)))


middle(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def passw(password):
    if len(password) > 6:
        if password.isdigit():
            print(False, 1)
        elif password.isalpha():
            print(False, 2)
        else:
            print(password)
    else:
        print(False, False)

d
passw('Kairat13')