from importlib.resources import contents
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2 


class Particulars :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x800")
        self.root.title("Face Recognition System")


        #variables 
        self.var_dep = StringVar()
        self.var_pos = StringVar()
        self.var_adm = StringVar()
        self.var_wh = StringVar()
        self.var_name = StringVar()
        self.var_id = StringVar()
        self.var_gen = StringVar()
        self.var_dob = StringVar()
        self.var_mail = StringVar()
        self.var_ph = StringVar()
        self.var_add = StringVar()
        self.var_zip = StringVar()
        self.var_blood = StringVar()
        self.var_alt = StringVar()


        #Background Image
        img1 = Image.open(r"images\bg9.jpeg")
        img1 = img1.resize((1300,700))
        self.photoimg = ImageTk.PhotoImage(img1)
        bg_img1 = Label(self.root,image=self.photoimg) 
        bg_img1.place(x=0,y=0,width=1300,height=700)

        
        #Left_Frame
        left_frame = LabelFrame(bg_img1,bd=2,relief=RIDGE,text="DETAILS",font= ("times new roman",12,"bold"),bg="Slategray4",fg="white")
        left_frame.place(x=20,y=120,width=630,height=620)

        #Current Status
        current_status_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="CURRENT STATUS",font= ("times new roman",12,"bold"),bg="Slategray4",fg="white")
        current_status_frame.place(x=5,y=10,width=615,height=130)

        #Department
        dep_label = Label(current_status_frame,text="Department",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        dep_label.grid(row=0,column=0,padx=10)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", background= "white")

        dep_combo=ttk.Combobox(current_status_frame,textvariable = self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"] = ("Select Your Department","Engineering","Medical","Architecture","Designing","Banking","Journalism","Law")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #Position
        pos_label = Label(current_status_frame,text="Position",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        pos_label.grid(row=0,column=2,padx=10)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", background= "white")

        pos_combo=ttk.Combobox(current_status_frame,textvariable=self.var_pos, font=("times new roman",12,"bold"),state="readonly")
        pos_combo["values"] = ("Select Your Position","Student","Lecturer","Doctor","Lawyer","Accountant","Developer","Designer","Manager","Support Staff","Others")
        pos_combo.current(0)
        pos_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Admission
        adm_label = Label(current_status_frame,text="Admission Year",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        adm_label.grid(row=1,column=0,padx=10)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", background= "white")

        adm_combo=ttk.Combobox(current_status_frame,textvariable=self.var_adm, font=("times new roman",12,"bold"),state="readonly")
        adm_combo["values"] = ("YYYY","Before 2001","2001","2002","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022")
        adm_combo.current(0)
        adm_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #work hours
        wh_label = Label(current_status_frame,text="Work Hours",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        wh_label.grid(row=1,column=2,padx=10)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", background= "white")

        wh_combo=ttk.Combobox(current_status_frame,textvariable=self.var_wh, font=("times new roman",12,"bold"),state="readonly")
        wh_combo["values"] = ("Shift Hours","8:00 - 16:00","14:00 - 22:00","23:00 - 6:00","Other Hours")
        wh_combo.current(0)
        wh_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Personal Info
        personal_info_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="PERSONAL INFORMATION",font= ("times new roman",12,"bold"),bg="Slategray4",fg="white")
        personal_info_frame.place(x=5,y=150,width=615,height=400)


        #NAME
        name_label = Label(personal_info_frame,text="Enter Name :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        name_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        name_entry = ttk.Entry(personal_info_frame,textvariable=self.var_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #ID
        id_label = Label(personal_info_frame,text="ID No :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        id_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        id_entry = ttk.Entry(personal_info_frame,textvariable=self.var_id, width=19,font=("times new roman",13,"bold"))
        id_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)


        #gender
        gen_label = Label(personal_info_frame,text="Gender : ",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        gen_label.grid(row=1,column=0,padx=15,sticky=W)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", background= "white")

        gen_combo=ttk.Combobox(personal_info_frame,textvariable=self.var_gen,font=("times new roman",12,"bold"),state="readonly")
        gen_combo["values"] = ("Select Your Gender","Male","Female","Others")
        gen_combo.current(0)
        gen_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        #dob
        dob_label = Label(personal_info_frame,text="DOB :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(personal_info_frame,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        dob_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)


        #email
        mail_label = Label(personal_info_frame,text="Email ID :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        mail_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        mail_entry = ttk.Entry(personal_info_frame,textvariable=self.var_mail,font=("times new roman",13,"bold"))
        mail_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #phno.
        ph_label = Label(personal_info_frame,text="Phone :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        ph_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        ph_entry = ttk.Entry(personal_info_frame,textvariable=self.var_ph,width=19,font=("times new roman",13,"bold"))
        ph_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)


        #address
        add_label = Label(personal_info_frame,text="Address :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        add_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        add_entry = ttk.Entry(personal_info_frame,textvariable=self.var_add,font=("times new roman",13,"bold"))
        add_entry.grid(row=3,column=1,padx=10,pady=7,sticky=W)


        #zipcode
        zip_label = Label(personal_info_frame,text="Zip Code :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        zip_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        zip_entry = ttk.Entry(personal_info_frame,textvariable=self.var_zip,width=19,font=("times new roman",13,"bold"))
        zip_entry.grid(row=3,column=3,padx=3,pady=5,sticky=W)


        #blood group
        blood_label = Label(personal_info_frame,text="Blood Group : ",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        blood_label.grid(row=4,column=0,padx=10,sticky=W)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", background= "white")

        blood_combo=ttk.Combobox(personal_info_frame,textvariable=self.var_blood,font=("times new roman",12,"bold"),state="readonly")
        blood_combo["values"] = ("Select","O+ve","O-ve","A+ve","A-ve","B+ve","B-ve","AB+ve","AB-ve")
        blood_combo.current(0)
        blood_combo.grid(row=4,column=1,padx=10,pady=10,sticky=W)


        #alter number
        alt_label = Label(personal_info_frame,text="Alt No :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        alt_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        alt_entry = ttk.Entry(personal_info_frame,textvariable=self.var_alt,width=19,font=("times new roman",13,"bold"))
        alt_entry.grid(row=4,column=3,padx=3,pady=5,sticky=W)


        #radiobuttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(personal_info_frame,variable=self.var_radio1, text="Take Photo Sample",value="Yes",width=22)
        radiobtn1.grid(row=6,column=1,pady=15)

        radiobtn2=ttk.Radiobutton(personal_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No",width=22)
        radiobtn2.grid(row=6,column=3,pady=15)


        #Button Frames
        btn_frame1 = LabelFrame(personal_info_frame,bd=2,relief = RIDGE,bg="Slategray4",highlightbackground="black")
        btn_frame1.place(x=5,y=270,width=605,height=34)

        sav_btn= Button(btn_frame1,text="Save",command=self.add_data, width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        sav_btn.grid(row=0,column=0)

        upd_btn= Button(btn_frame1,text="Update",command=self.update_data,width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        upd_btn.grid(row=0,column=1)

        del_btn= Button(btn_frame1,text="Delete",command=self.delete_data,width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        del_btn.grid(row=0,column=2)

        res_btn= Button(btn_frame1,text="Reset",command=self.reset_data,width="14",font=("times new roman",13,"bold"),bg="white",fg="black")
        res_btn.grid(row=0,column=3)

        btn_frame2 = LabelFrame(personal_info_frame,bd=2,relief = RIDGE,bg="Slategray4",highlightbackground="black")
        btn_frame2.place(x=5,y=305,width=605,height=32)

        addps_btn= Button(btn_frame2,command=self.generate_dataset,text="Add Photo Sample",width="29",font=("times new roman",13,"bold"),bg="white",fg="black")
        addps_btn.grid(row=0,column=0)

        updateps_btn= Button(btn_frame2,text="Update Photo Sample",width="29",font=("times new roman",13,"bold"),bg="white",fg="black")
        updateps_btn.grid(row=0,column=1)



        #Right_Frame
        right_frame = LabelFrame(bg_img1,bd=2,relief=RIDGE,text="DETAILS",font= ("times new roman",12,"bold"),bg="Slategray4",fg="white")
        right_frame.place(x=670,y=120,width=630,height=620)

        #Search frame
        search_frame = LabelFrame(right_frame,bd=2,highlightbackground="black", relief=RIDGE,text="SEARCH RESULTS",font= ("times new roman",12,"bold"),bg="Slategray4",fg="white")
        search_frame.place(x=5,y=10,width=617,height=80)

        #SEARCH BY
        search_label = Label(search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="Slategray4",fg="black")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", background= "white")

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=12)
        search_combo["values"] = ("Select Option","ID No.","Name","Phone No.","Email ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #search entry
        ent_entry = ttk.Entry(search_frame,width=11,font=("times new roman",13,"bold"))
        ent_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        #search button
        sea_btn= Button(search_frame,text="Search",width="12",font=("times new roman",12,"bold"),bg="white",fg="black",highlightbackground="white")
        sea_btn.grid(row=0,column=3,padx=2)

        #show all button
        show_btn= Button(search_frame,text="Show All",width="12",font=("times new roman",12,"bold"),bg="white",fg="black",highlightbackground="white")
        show_btn.grid(row=0,column=4,padx=2)

        #table frame
        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,bg="Slategray4",fg="white")
        table_frame.place(x=5,y=100,width= 617,height=450)

        #scrollbars
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.user_table = ttk.Treeview(table_frame,column=("Department","Position","Admission Year","Shift Hours","Name","ID No","Gender","DOB","Email ID","Phone","Address","Zip Code","Blood Group","Alt No","Image"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)

        self.user_table.heading("Department",text="Department")
        self.user_table.heading("Position",text="Position")
        self.user_table.heading("Admission Year",text="Admission Year")
        self.user_table.heading("Shift Hours",text="Shift Hours")
        self.user_table.heading("Name",text="Name")
        self.user_table.heading("ID No",text="ID No")
        self.user_table.heading("Gender",text="Gender")
        self.user_table.heading("DOB",text="DOB")
        self.user_table.heading("Email ID",text="Email ID")
        self.user_table.heading("Phone",text="Phone")
        self.user_table.heading("Address",text="Address")
        self.user_table.heading("Zip Code",text="Zip Code")
        self.user_table.heading("Blood Group",text="Blood Group")
        self.user_table.heading("Alt No",text="Alt No")
        self.user_table.heading("Image",text="Image Status")
        self.user_table["show"] = "headings"

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("times new roman", 10,"bold"))

        self.user_table.column("Department",width="115")
        self.user_table.column("Position",width="115")
        self.user_table.column("Admission Year",width="115")
        self.user_table.column("Shift Hours",width="115")
        self.user_table.column("Name",width="115")
        self.user_table.column("ID No",width="115")
        self.user_table.column("Gender",width="115")
        self.user_table.column("DOB",width="115")
        self.user_table.column("Email ID",width="115")
        self.user_table.column("Phone",width="115")
        self.user_table.column("Address",width="115")
        self.user_table.column("Zip Code",width="115")
        self.user_table.column("Blood Group",width="115")
        self.user_table.column("Alt No",width="115")
        self.user_table.column("Image",width="115")

        self.user_table.pack(fill=BOTH,expand=1)
        self.user_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #Function Declaration 

    def add_data(self):
        if self.var_dep.get()=="Select Your Department" or self.var_name.get()=="" or self.var_id.get()== "":
            messagebox.showerror("Error","Please Enter the Required Data",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Mayank@0422",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into user_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.var_dep.get(),
                                                                                                            self.var_pos.get(),
                                                                                                            self.var_adm.get(),
                                                                                                            self.var_wh.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_gen.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_mail.get(),
                                                                                                            self.var_ph.get(),
                                                                                                            self.var_add.get(),
                                                                                                            self.var_zip.get(),
                                                                                                            self.var_blood.get(),
                                                                                                            self.var_alt.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            
            
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","User Details has been Updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent = self.root)    



    #Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Mayank@0422",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from user_data")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.user_table.delete(*self.user_table.get_children())
            for i in data:
                self.user_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus = self.user_table.focus()
        content = self.user_table.item(cursor_focus)  
        data = content["values"]   

        self.var_dep.set(data[0]),
        self.var_pos.set(data[1]),
        self.var_adm.set(data[2]),
        self.var_wh.set(data[3]),
        self.var_name.set(data[4]),
        self.var_id.set(data[5]),
        self.var_gen.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_mail.set(data[8]),
        self.var_ph.set(data[9]),
        self.var_add.set(data[10]),
        self.var_zip.set(data[11]),
        self.var_blood.set(data[12]),
        self.var_alt.set(data[13]),
        self.var_radio1.set(data[14])


    #Update Button
    def update_data(self): 
        if self.var_dep.get()== "Select Your Department" or self.var_name.get()=="" or self.var_id.get()== "":
            messagebox.showerror("Error","Please Enter the Required Data",parent=self.root)  
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do You Want to Update User Details",parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Mayank@0422",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update user_data set `Department`=%s,`Position`=%s,`Admission Year`=%s,`Shift Hours`=%s,`Name`=%s,`Gender`=%s,`DOB`=%s,`Email ID`=%s,`Phone`=%s,`Address`=%s,`Zip Code`=%s,`Blood Group`=%s,`Alt No`=%s,`Image Status`=%s where `ID No` = %s",(
                         
                                                                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                                                                 self.var_pos.get(),
                                                                                                                                                                                                                 self.var_adm.get(),
                                                                                                                                                                                                                 self.var_wh.get(),
                                                                                                                                                                                                                 self.var_name.get(),
                                                                                                                                                                                                                 self.var_gen.get(),
                                                                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                                                                 self.var_mail.get(),
                                                                                                                                                                                                                 self.var_ph.get(),
                                                                                                                                                                                                                 self.var_add.get(),
                                                                                                                                                                                                                 self.var_zip.get(),
                                                                                                                                                                                                                 self.var_blood.get(),
                                                                                                                                                                                                                 self.var_alt.get(),
                                                                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                                                                 self.var_id.get()
                
                                                                                                                                                                                                           ))
                else:
                    if not Upadate :
                        return
                messagebox.showinfo("Success","User Details Successfully Updated",parent=self.root)   
                conn.commit()
                self.fetch_data()
                conn.close()  
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                                                
   

    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","User ID is required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do You Want to Delete User Details ?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Mayank@0422",database="face_recognition")
                    my_cursor = conn.cursor()
                    sql= "delete from user_data where `ID No`=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted User Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)    
            
                          

    #reset button
    def reset_data(self):
        self.var_dep.set("Select Your Department"),
        self.var_pos.set("Select Your Position"),
        self.var_adm.set("YYYY"),
        self.var_wh.set("Shift Hours"),
        self.var_name.set(""),
        self.var_id.set(""),
        self.var_gen.set("Select Your Gender"),
        self.var_dob.set(""),
        self.var_mail.set(""),
        self.var_ph.set(""),
        self.var_add.set(""),
        self.var_zip.set(""),
        self.var_blood.set("Select"),
        self.var_alt.set(""),
        self.var_radio1.set("")



    #Taking photo sampless
    def generate_dataset(self):  
        if self.var_dep.get()=="Select Your Department" or self.var_name.get()=="" or self.var_id.get()== "":
            messagebox.showerror("Error","Please Enter the Required Data",parent=self.root)  
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Mayank@0422",database="face_recognition")
                my_cursor = conn.cursor()  
                my_cursor.execute("Select * from user_data") #TO SELECT ALL DATA from user data table
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1 #TO CALCULATE AND UPDATE ID OF EVERY NEW PHOTO SAMPLE
                my_cursor.execute("update user_data set `Department`=%s,`Position`=%s,`Admission Year`=%s,`Shift Hours`=%s,`Name`=%s,`Gender`=%s,`DOB`=%s,`Email ID`=%s,`Phone`=%s,`Address`=%s,`Zip Code`=%s,`Blood Group`=%s,`Alt No`=%s,`Image Status`=%s where `ID No` = %s",(
                         
                                                                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                                                                 self.var_pos.get(),
                                                                                                                                                                                                                 self.var_adm.get(),
                                                                                                                                                                                                                 self.var_wh.get(),
                                                                                                                                                                                                                 self.var_name.get(),
                                                                                                                                                                                                                 self.var_gen.get(),
                                                                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                                                                 self.var_mail.get(),
                                                                                                                                                                                                                 self.var_ph.get(),
                                                                                                                                                                                                                 self.var_add.get(),
                                                                                                                                                                                                                 self.var_zip.get(),
                                                                                                                                                                                                                 self.var_blood.get(),
                                                                                                                                                                                                                 self.var_alt.get(),
                                                                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                                                                 self.var_id.get()==id+1
                
                                                                                                                                                                                                           )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #load data from opencv
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  #IMPORTING FACE DETECTION FUNCTION OF OpenCV and storing it in a variable

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #CONVERTED TO GRAY SCALE
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #SCALING FACTOR=1.3 and MINIMUM NEIGHBOR=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w] #CREATING RECTANGLES with coordinates x and y with a width of w and height of h
                        return face_cropped


                cap=cv2.VideoCapture(0) #OPENING CAMERA
                img_id=0
                while True:
                    ret,my_frame=cap.read() #READING OUT PHOTO SAMPLES before storing the images 
                    if face_cropped(my_frame) is not NONE:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(350,350)) #CROPPING OUT IMAGE with width=450 and height=450
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) #CONVERTING TO GRAY SCALEE
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" #STORING USER's IMAGE SAMPLES IN DATA FOLDER   
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) #FOR SHOWING DETAILS OF THE IMAGE ON THE IMAGE ITSELF
                        cv2.imshow("Cropped Face",face) #TO SHOW FRONTAL FACE

                    if cv2.waitKey(1)==13 or int(img_id)==10: #TO STOP CAPTURING USER IMAGE AFTER 10 SAMPLES
                        break 
                cap.release() #RELEASING ALL THE IMAGES THAT HAVE BEEN CAPTURED
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Image Samples Stored Successfully")   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)        
                   

                

if __name__ == "__main__":
    root= Tk()
    obj= Particulars(root)
    root.mainloop()