import logging

logging.basicConfig(
        filename="error.log",
        level=logging.ERROR,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

def file_read(filename):
    try:
        with open(filename, 'r') as rf:
            for f in rf:
                    print(f,end='')

    except FileNotFoundError :
        print("Error.....!!!")
        logging.error("File not found", exc_info=False)

# main 
over = True
while over:
    choice = True
    print("")
    filename = input("Enter file name with extension (Eg- file.txt):  ")
    file_read(filename)
    print("")
    while choice:
        o = input("Do you want to read more files ? (Y/N) : ")
        if o == 'N' or  o =='n':
            over = False
            choice = False
        elif o  == 'Y' or o == 'y':
            over = True
            choice = False
        else:
            print("wrong choice ")
            choice = True
            

            

        


