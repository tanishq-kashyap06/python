from importlib.resources import contents
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2 
import os
import csv
from tkinter import filedialog

mydata=[]
class RecordsOfUser :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")

        #Creating Variables
        self.var_dep=StringVar()
        self.var_pos=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()


        #Background Image
        img1 = Image.open(r"images\bg9.jpeg")
        img1 = img1.resize((1300,700))
        self.photoimg = ImageTk.PhotoImage(img1)
        bg_img1 = Label(self.root,image=self.photoimg) 
        bg_img1.place(x=0,y=0,width=1300,height=700)

        #Left_Frame
        left_frame = LabelFrame(bg_img1,bd=2,relief=RIDGE,text="USER INFORMATION",font= ("times new roman",12,"bold"),bg="Slategray4",fg="white")
        left_frame.place(x=20,y=120,width=630,height=620)

        #User Info
        user_info_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,bg="Slategray4")
        user_info_frame.place(x=5,y=20,width=615,height=220)

        #Department
        dep_label = Label(user_info_frame,text="Department :",font=("times new roman",13,"bold"),bg="Slategray4")
        dep_label.grid(row=0,column=0,padx=5,pady=20,sticky=W)

        dep_entry = ttk.Entry(user_info_frame,textvariable=self.var_dep, font=("times new roman",13,"bold"))
        dep_entry.grid(row=0,column=1,padx=5,pady=20,sticky=W)

        #Position
        posn_label = Label(user_info_frame,text="Position :",font=("times new roman",13,"bold"),bg="Slategray4")
        posn_label.grid(row=0,column=2,padx=5,pady=20,sticky=W)

        posn_entry = ttk.Entry(user_info_frame,textvariable=self.var_pos, font=("times new roman",13,"bold"))
        posn_entry.grid(row=0,column=3,padx=5,pady=20,sticky=W)

        #NAME
        name_label = Label(user_info_frame,text="Name :",font=("times new roman",13,"bold"),bg="Slategray4")
        name_label.grid(row=1,column=0,padx=5,pady=20,sticky=W)

        name_entry = ttk.Entry(user_info_frame,textvariable=self.var_name, font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,padx=5,pady=20,sticky=W)

        #USER ID
        id_label = Label(user_info_frame,text="ID No :",font=("times new roman",13,"bold"),bg="Slategray4")
        id_label.grid(row=1,column=2,padx=5,pady=20,sticky=W)

        id_entry = ttk.Entry(user_info_frame,textvariable=self.var_id, font=("times new roman",13,"bold"))
        id_entry.grid(row=1,column=3,padx=5,pady=20,sticky=W)
        

        
        #Time
        time_label = Label(user_info_frame,text="Time :",font=("times new roman",13,"bold"),bg="Slategray4")
        time_label.grid(row=2,column=0,padx=5,pady=20,sticky=W)

        time_entry = ttk.Entry(user_info_frame,textvariable=self.var_time, font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=5,pady=20,sticky=W)

        #Date
        date_label = Label(user_info_frame,text="Date :",font=("times new roman",13,"bold"),bg="Slategray4")
        date_label.grid(row=2,column=2,padx=5,pady=20,sticky=W)

        date_entry = ttk.Entry(user_info_frame,textvariable=self.var_date, font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=5,pady=20,sticky=W)

        #Button Frames
        btn_frame1 = LabelFrame(left_frame,bd=2,relief = RIDGE,bg="Slategray4",highlightbackground="black")
        btn_frame1.place(x=5,y=270,width=605,height=34)

        imp_btn= Button(btn_frame1,text="Import Data",cursor="hand2",command=self.copycsv, width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        imp_btn.grid(row=0,column=0)

        exp_btn= Button(btn_frame1,text="Export Data",cursor="hand2",command=self.savecsv, width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        exp_btn.grid(row=0,column=1)

        upd_btn= Button(btn_frame1,text="Update Data",cursor="hand2",width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        upd_btn.grid(row=0,column=2)

        res_btn= Button(btn_frame1,text="Reset Data",cursor="hand2",command=self.data_reset, width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        res_btn.grid(row=0,column=3)


        #Right_Frame
        right_frame = LabelFrame(bg_img1,bd=2,relief=RIDGE,text="USER INFORMATION",font= ("times new roman",12,"bold"),bg="Slategray4",fg="white")
        right_frame.place(x=670,y=120,width=630,height=620)

        #table frame
        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,bg="Slategray4",fg="white")
        table_frame.place(x=5,y=40,width= 617,height=510)

        #scrollbars
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.userdata_table=ttk.Treeview(table_frame,column=("Department","Position","Name","ID No","Time","Date"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.userdata_table.xview)
        scroll_y.config(command=self.userdata_table.yview)

        self.userdata_table.heading("Department",text="Department")
        self.userdata_table.heading("Position",text="Position")
        self.userdata_table.heading("Name",text="Name")
        self.userdata_table.heading("ID No",text="ID No")
        self.userdata_table.heading("Time",text="Time")
        self.userdata_table.heading("Date",text="Date")
        self.userdata_table["show"] = "headings"

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("times new roman", 13,"bold"))

        self.userdata_table.column("Department",width="115")
        self.userdata_table.column("Position",width="115")
        self.userdata_table.column("Name",width="115")
        self.userdata_table.column("ID No",width="115")
        self.userdata_table.column("Time",width="115")
        self.userdata_table.column("Date",width="115")


        self.userdata_table.pack(fill=BOTH,expand=1)
        self.userdata_table.bind("<ButtonRelease>",self.get_pointer)



    #getting data
    def getdata(self,rows):
        self.userdata_table.delete(*self.userdata_table.get_children())  
        for i in rows:
            self.userdata_table.insert("",END,values=i)  

    #IMPORT DATA FROM CSV FILE
    def copycsv(self):
        global mydata 
        mydata.clear()
        fil_name=filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root) #Gets current working directory
        with open(fil_name) as user_file:
            csvread=csv.reader(user_file,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.getdata(mydata)    

    #EXPORT DATA 
    def savecsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Data Not Found","No Data Available to Save/Export",parent=self.root)
                return False
            fil_name=filedialog.asksaveasfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)             
            with open(fil_name,mode="w",newline="") as user_file:
                exp_write=csv.writer(user_file,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Saved","Data Successfully Saved/Exported to"+os.path.basename(fil_name))    
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent = self.root)          
    

    def get_pointer(self,event=""):
        point =self.userdata_table.focus()
        items=self.userdata_table.item(point)
        boxes =items['values']
        self.var_dep.set(boxes[0])
        self.var_pos.set(boxes[1])
        self.var_name.set(boxes[2])
        self.var_id.set(boxes[3])
        self.var_time.set(boxes[4])
        self.var_date.set(boxes[5])


    def data_reset(self):
        self.var_dep.set("")
        self.var_pos.set("")
        self.var_name.set("")
        self.var_id.set("")
        self.var_time.set("")
        self.var_date.set("")



        
        

if __name__ == "__main__" :
    root= Tk()
    obj= RecordsOfUser(root)
    root.mainloop()
    