from importlib.resources import contents
from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2 


class Dev :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")

        #Background Image
        img1 = Image.open(r"images\backdev.jpeg")
        img1 = img1.resize((1300,700))
        self.photoimg = ImageTk.PhotoImage(img1)
        bg_img1 = Label(self.root,image=self.photoimg) 
        bg_img1.place(x=0,y=0,width=1300,height=700)

        #dev_Frame
        dev_frame = LabelFrame(bg_img1,bd=2,relief=RIDGE,text="DEVELOPER",font= ("times new roman",25,"bold"),bg="black",fg="purple2")
        dev_frame.place(x=5,y=5,width=510,height=340)

        #TEXT
        tex_label=Label(dev_frame,text="Hi, I am Tanishq, a student from The LNM Institute of Information Technology",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=5)

        tex_label=Label(dev_frame,text="This is my first ever project and i was very delighted to work on this as ",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=30)

        tex_label=Label(dev_frame,text="I had no pre-knowledge of any of the skills required to work on it. I learned",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=55)

        tex_label=Label(dev_frame,text="all the skills while working on the project itself. It has definitely been a",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=80)

        tex_label=Label(dev_frame,text="topsy-turvy journey of four weeks filled with enjoyment and knowledge. ",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=105)

        tex_label=Label(dev_frame,text="At the end of four weeks, I came up with this face recognition project",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=130)

        tex_label=Label(dev_frame,text="which can be used by a large organization with many small units to store",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=155)

        tex_label=Label(dev_frame,text="data and scan/detect/recognize images of all it's employees in one place. ",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=180)

        tex_label=Label(dev_frame,text="Hoping you liked my project and I am definitely waiting for some ",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=205)

        tex_label=Label(dev_frame,text="improvement recommendations. THANK YOU !",font= ("times new roman",12,"bold"),fg="purple2")
        tex_label.place(x=0,y=230)













if __name__ == "__main__" :
    root= Tk()
    obj= Dev(root)
    root.mainloop()        

