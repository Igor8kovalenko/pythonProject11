from functions import *

def main():
    try:
        data = read_json('operations.json')
        data = sort_data(data)[:5]
        for row in data:
            print(output_data(row))

    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    main()