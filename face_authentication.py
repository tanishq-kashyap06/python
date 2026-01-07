from importlib.resources import contents
from pyexpat import features
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  
from time import strftime
from datetime import datetime
import cv2 
import os
import numpy as np




class Face_Authentication :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")


        #Background Image
        img1 = Image.open(r"images\fau2.jpeg")
        img1 = img1.resize((700,700))
        self.photoimg = ImageTk.PhotoImage(img1)
        bg_img1 = Label(self.root,image=self.photoimg) 
        bg_img1.place(x=0,y=0,width=700,height=700)

        img2 = Image.open(r"images\fau5.jpeg")
        img2 = img2.resize((700,700))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img2 = Label(self.root,image=self.photoimg2) 
        bg_img2.place(x=700,y=0,width=700,height=700)

        b_bttn = Button(self.root,text="FACE AUTHENTICATION",cursor="hand2",command=self.face_authenticate,font=("times new roman",25,"bold"),bg="black",fg="light sky blue")
        b_bttn.place(x=120,y=640,width=458,height=50)


    #User Records
    def user_records (self,fet1,fet2,fet3,fet4) :
        with open ("record_sheet.csv","r+", newline="\n") as f:
            user_data_record = f.readlines()
            name_record=[]
            for line in user_data_record:
                input=line.split((","))
                name_record.append(input[0])

            if((fet1 not in name_record) and (fet2 not in name_record) and (fet3 not in name_record) and (fet4 not in name_record)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                date_str=now.strftime("%H:%M:%S")
                f.writelines(f"\n{fet1},{fet2},{fet3},{fet4},{date_str},{d1}")



    #face_authentication
    def face_authenticate(self):
        def face_enclose(img,classifier,scaleFactor,minNeighbors,color,text,clf): #TO DRAW BOUNDARY AROUND THE IMAGE
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #GRAY SCALE CONVERSION
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

            measures=[] #COORDINATES OF THE RECTANGLE AROUND THE FACE

            for(x,y,w,h) in features: #LOOP OF WIDTH AND HEIGHT
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)  # GREEN RECTANGLE AGAINST THE FACE  
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])   #GRAY SCALE IMAGE PREDICTION
                histo=int((100*(1-predict/300))) #THE FORMULA OF CONFIDENCE FROM THE ALGORITHM

                conn = mysql.connector.connect(host="localhost",username="root",password="Mayank@0422",database="face_recognition")
                my_cursor = conn.cursor() #FETCHING DATA FROM DATABASE

                my_cursor.execute("select `Department` from user_data where `ID No`="+str(id))
                fet1=my_cursor.fetchone()
                fet1="+".join(fet1)

                my_cursor.execute("select `Position` from user_data where `ID No`="+str(id))
                fet2=my_cursor.fetchone()
                fet2="+".join(fet2)

                my_cursor.execute("select `Name` from user_data where `ID No`="+str(id))
                fet3=my_cursor.fetchone()
                fet3="+".join(fet3)

                my_cursor.execute("select `ID No` from user_data where `ID No`="+str(id))
                fet4=my_cursor.fetchone()
                fet4="+".join(fet4)



                if histo>85: # CHECKING CONFIDENCE
                    cv2.putText(img,f"Department:{fet1}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                    cv2.putText(img,f"Position:{fet2}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                    cv2.putText(img,f"Name:{fet3}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                    cv2.putText(img,f"ID No:{fet4}",(x,y-0),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
                    self.user_records(fet1,fet2,fet3,fet4)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Face-Match Not Found",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                measures=[x,y,w,h]

            return measures    

        def authenticate(img,clf,FaceauthenCascade) :    
            measures= face_enclose(img,FaceauthenCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        FaceauthenCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("DataProcess.xml") 

        cap=cv2.VideoCapture(0) #0 AS WE USING THE LAPTOP CAMERA

        while True:
            ret,img=cap.read()
            img=authenticate(img,clf,FaceauthenCascade)
            cv2.imshow("Face Authentication",img)

            if cv2.waitKey(1)==13: #KEEP THE CAMERA OPEN UNTIL ENTER PRESSED
                break
        cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root= Tk()
    obj= Face_Authentication(root)
    root.mainloop()     