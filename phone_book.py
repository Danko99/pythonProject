phone_book = {}


def phonebook(str):
    array = str.split()
    if array[0] == "ADD":
        def ADD():
            global phone_book
            if array[1] not in phone_book.keys():
                phone_book[array[1]] = [i for i in array[2].split(",")]

            else:
                phone_book[array[1]] += [i for i in array[2].split(",")]

        ADD()

    if array[0] == "REMOVE_PHONE":
        def REMOVE_PHONE():
            counter = 0
            global phone_book
            for value in phone_book.values():
                for i in value:
                    if i == array[1]:
                        value.remove(i)
                        counter += 1

            if counter >= 1:
                return True
            else:
                return False

        return REMOVE_PHONE()

    if array[0] == "SHOW":
        def SHOW():

            global phone_book
            temp = phone_book
            phone_book = sorted(phone_book.keys())
            phone_book = dict.fromkeys(phone_book)
            for keys, values in temp.items():
                if keys in phone_book.keys():
                    phone_book[keys] = values

            for keys, values in phone_book.items():
                phone_book[keys] = sorted(values)
                if values:
                    print(f"{keys}:{values}", end=" ")
            print()

        SHOW()


phonebook("ADD Ivan 555-10-01,555-10-03")
phonebook("ADD Ivan 555-10-02")
phonebook("SHOW")

phonebook("REMOVE_PHONE 555-10-03")
phonebook("ADD Alex 555-20-01")
phonebook("SHOW")

phonebook("REMOVE_PHONE 555-20-01")
phonebook("SHOW")

phonebook("REMOVE_PHONE 555-10-01")
phonebook("REMOVE_PHONE 555-10-02")
phonebook("SHOW")
