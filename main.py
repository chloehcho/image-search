# main file

def main():
    keepGoing = True
    while keepGoing:
        print("---KEY---")
        print("create: prints a list of all the images into a text file ")
        print("open <id>: opens the image of the id")
        print("quit: quit out of input loop")
        key = input("Enter: ")
        if key == "create":
            createImageList("itemList.txt")
        elif key.split(" ")[0] == "open":
            openImage("00_pants.gif")
        elif key == "quit":
            keepGoing = False
        else:
            print("Not a valid input")


if __name__ == "__main__":
    main()
