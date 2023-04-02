class imageEncriptDecript:
    def __init__(self,name,path):
        self.name=name
        self.path=path

    def encrypt(self):
        file =open(self.path+"\\"+self.name,"rb")
        image=file.read()
        file.close()

        image=bytearray(image)
        key=48

        for x,y in enumerate(image):
            image[x]=y^key

        encryptName=self.name.split(".")

        file=open(encryptName[0]+"Encripted"+"."+encryptName[1],"wb")
        file.write(image)
        file.close()

    def decript(self):

        file =open(self.path+"\\"+self.name,"rb")
        image=file.read()
        file.close()

        image=bytearray(image)
        key=48

        for x,y in enumerate(image):
            image[x]=y^key
        
        decryptName=self.name.split(".")
        file=open(decryptName[0]+"Decrypted"+"."+decryptName[1],"wb")
        file.write(image)
        file.close()


print("""      _                            _     ______                             _     _____ __  __  _____ 
     | |                          | |   |  ____|                           | |   |_   _|  \/  |/ ____|
   __| | ___  ___ _ __ _   _ _ __ | |_  | |__   _ __   ___ _ __ _   _ _ __ | |_    | | | \  / | |  __ 
  / _` |/ _ \/ __| '__| | | | '_ \| __| |  __| | '_ \ / __| '__| | | | '_ \| __|   | | | |\/| | | |_ |
 | (_| |  __/ (__| |  | |_| | |_) | |_  | |____| | | | (__| |  | |_| | |_) | |_   _| |_| |  | | |__| |
  \__,_|\___|\___|_|   \__, | .__/ \__| |______|_| |_|\___|_|   \__, | .__/ \__| |_____|_|  |_|\_____|
                        __/ | |                                  __/ | |                              
                       |___/|_|                                 |___/|_|                              \n\t\t\t\t\t\tCoding by THIWA\n\n""")
print("............Select your choice.............\n\n [1] Encript image \n [2] Decript image\n [3] Exit\n\n")
choice=input(">>")
if choice !="3":
    name=input("Image name >>>") 
    path=input("Enter image path >>>")
    mainClass=imageEncriptDecript(name,path)
    if choice=="1":
        mainClass.encrypt()
    elif choice=="2":
        mainClass.decript()

elif choice=="3":
    exit()