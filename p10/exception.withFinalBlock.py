try :
    file_open("myfile.txt",'r')
except IOError :
    print("Errror : Unable to read the file !")
finally :
    file.close()
