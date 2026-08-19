dictionary={}
while True:
    print("\nDictionary Management System ")
    print("1. Add a Word")
    print("2.Search for Meaning")
    print("3.Display all words")
    print("4.Update Meaning")
    print("5.Delete Word")
    print("6.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        word=input("Enter the word:").lower()
        meaning=input("Enter the meaning:")
        dictionary[word]=meaning

        print("Word Entered Successfully")

    elif choice==2:
        word=input("Enter the word for search:").lower()
        if word in dictionary:
            print("Meaning:",dictionary[word])
        else:
            print("Word not found in dictionary")

    elif choice==3:
        if dictionary:
            print("Words and their meanings")
            for w,j in dictionary.items():
                print(f"{w} : {j}")
        else:
            print("Dictionary is empty")
        

    elif choice==4:
        word=input("Enter the word:")
        if word in dictionary:
            new_meaning=input("Enter the meaning:")
            dictionary[word]=new_meaning
            print("Updated meaning:", dictionary[word])
            print("Word Updated Successfully")
        else:
            print("Word not found in dictoinary")
    elif choice==5:
        word=input("Enter the word to delete:")

        if word in dictionary:
            dictionary.pop(word)
            print("Word Succefully deleted :",word)
        else:
            print("this word not in dictionary")
    elif choice==6:
        print("program exit successfully")
        break


 