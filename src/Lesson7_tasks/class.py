import pickle


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


if __name__ == '__main__':
    ex2()
