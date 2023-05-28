from utils import *

def main():
    data = load_date("operation.json")
    lates_list = lates_take(data)
    for operation in lates_list:
        print(print_oper(operation))
        print()

if __name__ == '__main__':
    main()


