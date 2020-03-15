import os
import pickle
import platform


def ex1():
    with open('a.txt', 'tr+') as file:
        lines = list(file)
        for line in lines:
            print(line, end='')
        print('-'*40)
        print(file.tell())
        file.write('Hello world ========\n')
        file.seek(0)
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()
        file.seek(0)
        a = file.readlines()
        print('*'*40)
        print(a)


def ex2():
    with open('b.dump', 'bw+') as file:
        fList = ['1', '2', '3']
        s = pickle.dumps(fList)
        pickle.dump(fList, file)
        file.flush()
        print(s)
        eList = pickle.loads(s)
        print(eList)
        file.seek(0)
        eList = pickle.load(file)
        print(eList)


def ex3():
    print('OS core: ', os.name)
    print('-'*20)
    path = os.getcwd()
    p = path[1:].split('/')
    for folder in p:
        print(folder)
    print(path)
    print('-'*20)
    print('OS core by Platform: {0} - {1}'.format(platform.system(), platform.platform()))
    print('Machine: ', platform.machine(), platform.processor(), platform.node())


class MyEx(Exception):
    pass


def ex4():
    try:
        print("Try branch")
        raise MyEx('ERROR')
    except MyEx as e:
        print('** Custom exception error: ', e)
    except Exception as e:
        print(e)
    else:
        print('Else branch')
    finally:
        print('Finally branch')


if __name__ == '__main__':
    ex4()
