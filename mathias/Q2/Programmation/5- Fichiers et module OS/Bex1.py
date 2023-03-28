def read(file) :
    with open (file,"r") as file :
        text = file.read()
        return text

def write(file, text) :
    with open (file,"w") as file :
        file.write(text)


if __name__ == "__main__" :

    write("exo1-2.txt", read("exo1-1.txt"))
