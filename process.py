from importlib.resources import contents
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2 
import os
import numpy as np




class Process_Data :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")


        #Background Image
        img1 = Image.open(r"images\bgdp.jpeg")
        img1 = img1.resize((1100,700))
        self.photoimg = ImageTk.PhotoImage(img1)
        bg_img1 = Label(self.root,image=self.photoimg) 
        bg_img1.place(x=0,y=0,width=1430,height=700)

        #Process Button 
        b_bttn = Button(self.root,text="PROCESS THE DATA",command=self.process_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="black",fg="light sky blue")
        b_bttn.place(x=520,y=355,width=470,height=50)

    
    def process_classifier(self):
        data_dir=("data") #STORING DATA PATH in a variable
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[] #FACES and ID's INITIALISED TO EMPTY LIST according to algorithm
        ids=[]

        for image in path: #ACCESSING ALL IMAGES STORED IN PATH
            img=Image.open(image).convert('L') #CONVERSION TO GRAY SCALE
            imageNp=np.array(img,'uint8')  #CONVERSION TO GRID FORM USING NUMPY and storing it in a variable 
            id=int(os.path.split(image)[1].split('.')[1]) #TO GET THE INTEGER ID

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Processing",imageNp)
            cv2.waitKey(1)==13 #closing window on pressing enteR

        ids = np.array(ids)

        #Processing Classifierss
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("DataProcess.xml")  #TO SAVE DATA IN A FILE
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Data Processing Completed")


        









if __name__ == "__main__":
    root= Tk()
    obj= Process_Data(root)
    root.mainloop()        