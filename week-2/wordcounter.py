def word_counter(filename):
    words = 0
    lines = 0
    characters = 0
    try:
        with open("Programming.txt","r") as file:
         for line in file:
            lines += 1
            characters += len(line)

            words_in_line = line.split()
            words += len(words_in_line)

        print("File : " + filename)
        print("Words : " + str(words))
        print("Lines : " + str(lines))
        print("Characters : " + str(characters))
    
    except FileNotFoundError:
        print("Error : The file was not found.")    

filename =  "Programming.txt"
word_counter(filename)