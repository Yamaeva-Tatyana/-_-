import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as in_file:
        csv_data = list(csv.DictReader(in_file, delimiter=',', quotechar="\n"))

    with open(OUTPUT_FILENAME, "w") as out_file:
        json.dump(csv_data, out_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")