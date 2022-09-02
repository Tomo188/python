from test import square


def main():
    try:
        assert square(3) == 9
    except AssertionError:
        print("square from 3 not equal 9")


def hello(name):
    print(name)


def godbye(name):
    print(name)


if __name__ == "__main__":
    main()
