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


    def _get_db_connection(self):
        """Return a mysql.connector connection using env vars with sensible defaults.
        Returns None and shows a dialog on failure."""
        user = os.getenv("DB_USER", "root")
        password = os.getenv("DB_PASS", "SHubh123")
        host = os.getenv("DB_HOST", "127.0.0.1")
        database = os.getenv("DB_NAME", "face_recognition")
        try:
            return mysql.connector.connect(user=user, password=password, host=host, database=database)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"DB connection failed: {err}")
            return None


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

                conn = self._get_db_connection()
                if not conn:
                    # If DB connection failed, fall back to unknown labels so UI keeps working
                    fet1 = fet2 = fet3 = fet4 = "Unknown"
                else:
                    try:
                        my_cursor = conn.cursor()
                        my_cursor.execute("SELECT `Department`,`Position`,`Name`,`ID No` FROM user_data WHERE `ID No`=%s", (id,))
                        row = my_cursor.fetchone()
                        if row:
                            fet1 = str(row[0]) if row[0] is not None else ""
                            fet2 = str(row[1]) if row[1] is not None else ""
                            fet3 = str(row[2]) if row[2] is not None else ""
                            fet4 = str(row[3]) if row[3] is not None else ""
                        else:
                            fet1 = fet2 = fet3 = fet4 = "Unknown"
                    except mysql.connector.Error as err:
                        messagebox.showerror("Database Error", f"Query failed: {err}")
                        fet1 = fet2 = fet3 = fet4 = "Unknown"
                    finally:
                        conn.close()



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

        cap=cv2.VideoCapture(0) #0 AS WE ARE USING THE LAPTOP CAMERA

        if not cap.isOpened():
            messagebox.showerror("Camera Error","Could not open the camera. Make sure it's connected and not used by another app.")
            return

        # Try to read an initial frame to validate the camera
        ret, test_frame = cap.read()
        if not ret or test_frame is None:
            messagebox.showerror("Camera Error","Failed to read from camera. Check permissions and that the camera is not used by another app.")
            cap.release()
            return

        # Show the camera feed inside a Tkinter Toplevel window so it appears over the app
        win = Toplevel(self.root)
        win.title("Face Authentication")
        win.geometry("660x540")
        win.resizable(False, False)

        frame_holder = Frame(win, width=640, height=480, bg="black")
        frame_holder.pack(padx=10, pady=(10,5))
        lmain = Label(frame_holder, width=640, height=480)
        lmain.pack()

        status_label = Label(win, text="Initializing...", anchor="w")
        status_label.pack(fill='x', padx=10, pady=(0,10))

        # placeholder image shown when there is an error
        placeholder = Image.new('RGB', (640,480), (120,120,120))
        placeholder_tk = ImageTk.PhotoImage(placeholder)
        lmain.imgtk = placeholder_tk
        lmain.configure(image=placeholder_tk)
        status_label.config(text="Camera OK — starting feed")

        def stop_camera():
            if cap.isOpened():
                cap.release()
            win.destroy()
            cv2.destroyAllWindows()

        win.protocol("WM_DELETE_WINDOW", stop_camera)

        def update_frame():
            try:
                ret, frame = cap.read()
                if not ret or frame is None:
                    status_label.config(text="Error: no frame received — retrying...")
                    lmain.after(100, update_frame)
                    return

                frame = authenticate(frame,clf,FaceauthenCascade)

                # validate frame type
                if not isinstance(frame, np.ndarray):
                    status_label.config(text="Error: processed frame invalid")
                    lmain.imgtk = placeholder_tk
                    lmain.configure(image=placeholder_tk)
                    lmain.after(100, update_frame)
                    return

                # convert from BGR (OpenCV) to RGB (PIL) and resize to widget
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(cv2image).resize((640,480))
                imgtk = ImageTk.PhotoImage(image=pil_image)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                status_label.config(text="Running")

            except Exception as e:
                # show the error to the user and keep the placeholder visible
                status_label.config(text=f"Error: {e}")
                lmain.imgtk = placeholder_tk
                lmain.configure(image=placeholder_tk)

            finally:
                lmain.after(30, update_frame)

        # prime the first frame with the test frame
        try:
            cv2image = cv2.cvtColor(test_frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv2image).resize((640,480))
            imgtk = ImageTk.PhotoImage(image=pil_image)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
        except Exception:
            lmain.imgtk = placeholder_tk
            lmain.configure(image=placeholder_tk)

        update_frame()




if __name__ == "__main__":
    root= Tk()
    obj= Face_Authentication(root)
    root.mainloop()     