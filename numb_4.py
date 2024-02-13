import os



def get_instance(mark: str) -> str:
    '''
    возвращает относительрный путь для объекта класса, переданного
    в функцию Если такого пути нет, функция возвращает None.
    '''
    path = os.path.join("dataset_1", mark)
    names = os.listdir(path)
    names.append(None)
    for i in range(len(names)):
        if names[i] is not None:
            yield os.path.join(path, names[i])
        elif names[i] is None:
            yield None


def main() -> None:

    class1 = 'cat'
    # class2 = 'dog'

    print(*get_instance(class1))


if __name__ == "__main__":
    main()


