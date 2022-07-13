
import os

def soldier(path, file_name, fileFormat):
    os.chdir(path)
    file = open(file_name)
    text = file.read()
    print(text)
    file.close()
    counter = 1
    while True:
        text1 = (yield)
        print(f"Text 1 is : {text1}" )
        for item in os.listdir(path):
            extension = os.path.splitext(item)
            # print(extension)

            if extension[1] == fileFormat or extension[1] == fileFormat:

                os.rename(item, f"{counter}{extension[1]}")
                counter = counter + 1
            if extension[0] in text:
                continue
            else:
                if item[0].isalpha():
                    print(item[0])
                    os.rename(item, item.capitalize())

            print((item))
            print((extension))
        pass




if __name__ == '__main__':
    # path = input("Enter the path here : ")
    # fileName = input("Enter file name here of which you dont want to captilize first letter : ")
    # fileFormat = input("Enter file format you want to rename the files : ")
    soldierFunc = soldier("C:\\Users\\Khan Mob s  Comp\\PycharmProjects\\AnotherProj", "Subhan2.txt", ".jpeg")
    next(soldierFunc)
    soldierFunc.send(0)
    