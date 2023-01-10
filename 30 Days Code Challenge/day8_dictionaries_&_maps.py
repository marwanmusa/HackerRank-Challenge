"""
    Task:
        Given n names and phone numbers, assemble a phone book
        that maps friends' names to their respective phone numbers.
        You will then be given an unknown number of names to query
        your phone book for. For each name queried, print the associated entry
        from your phone book on a new line in the form name=phoneNumber;
        if an entry for name is not found, print Not found instead.

    Note:
        Your phone book should be a Dictionary/Map/HashMap data structure.
"""

if __name__ == "__main__":
    input_int = int(input().strip())
    phoneBook = dict()

    i = 0
    while i < input_int:
        input_contact = str(input().strip())
        list_contact = input_contact.split(" ")
        phoneBook[list_contact[0]] = list_contact[1]
        i += 1

    while True:
        try:
            Name = input()
            if Name in phoneBook.keys():
                print(f"{Name}={phoneBook[Name]}")
            else:
                print("Not found")
        except:
            break