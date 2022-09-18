from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 15")

def logout():
    os.system("shutdown -1")

def shutdown():
        os.system("shutdown /s /t 15")


st=Tk()
st.title("shutdown aap")
st.geometry("600x400")
st.config(bg= "red")

r_button= Button(st,text="Restart",font=("time new roman",20,"bold"),relief=RAISED,cursor="plus",command=restart )
r_button.place(x=200,y=30,height=30,width=200)

rt_button= Button(st,text="restart time",font=("time new roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time )
rt_button.place(x=200,y=100,height=30,width=200)


lg_button= Button(st,text="Log-out",font=("time new roman",20,"bold"),relief=RAISED,cursor="plus",command=logout )
lg_button.place(x=200,y=170,height=30,width=200)

sd_button= Button(st,text="Shutdown",font=("time new roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown )
sd_button.place(x=200,y=240,height=30,width=200)


st.mainloop()
