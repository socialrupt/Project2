import multiprocessing


def Python_File1():
    import Settings

def Python_File2():
    import Group_1.Auto_Drop_Bot.Main_Auto_Drop

def Python_File3():
    import Group_1.Leeching_Bot.Get_Links_From_Group

def Python_File4():
    import Group_1.Delete_non_links_Bot.Delete_Non_Links

if __name__ == "__main__":
    P1 = multiprocessing.Process(target=Python_File1)
    P2 = multiprocessing.Process(target=Python_File2)
    P3 = multiprocessing.Process(target=Python_File3)
    P4 = multiprocessing.Process(target=Python_File4)
#Understand everything!!!
    P1.start()

    P2.start()

    P3.start()

    P4.start()

    P1.join()
    P2.join()
    P3.join()
    P4.join()

#FIX the not directory found error!!!