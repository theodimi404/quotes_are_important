import csv
import random


def entry():
    quote = input("Insert the quote: ")
    creator = input("\nInsert the source of the quote: ")

    new_entry = [quote, creator]
    file = open('output.csv', 'a', encoding='utf-8-sig')

    file.write(new_entry[0])
    file.write('    by    ')
    file.write(new_entry[1])
    file.write('\n')

    file.close()


def random_quote():
    try:
        file = open("output.csv", 'r')
        num_line = len(file.readlines())
        num1 = random.randint(1, num_line)
        with open('output.csv', encoding='utf-8-sig') as fd:
            reader = csv.reader(fd)
            random_row = [row for idx, row in enumerate(reader) if idx == num1 - 1]
            print(random_row[0][0])
    except:
        print('There is no quote saved')


choice = int(input("If you want to create a new quote    type 1,\nif you want to see a random quote    type 2\n-> "))

if choice == 1:
    entry()
elif choice == 2:
    random_quote()

input('\n\n\nPress ENTER to exit')