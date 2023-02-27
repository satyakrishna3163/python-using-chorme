from tkinter import *

root = Tk()
root.geometry("500x300")

def getvals():
    print("accepted")


Label(root, text="python registration From", font = "arial 15 bold").grid(row=0,column=3)

name = Label(root,text= "Name").grid(row=1,column=2)
phone = Label(root,text= "phone").grid(row=2,column=2)
gender = Label(root,text= "gender").grid(row=3,column=2)
emergency = Label(root,text= "emergency").grid(row=4,column=2)
paymentmood = Label(root,text= "paymentmood").grid(row=5,column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue= StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

nameentry=Entry(root,textvariable=namevalue).grid(row=1,column=3)
phoneentry=Entry(root,textvariable=phonevalue).grid(row=2,column=3)
genderentry=Entry(root,textvariable=gendervalue).grid(row=3,column=3)
emergencyentry=Entry(root,textvariable=emergencyvalue).grid(row=4,column=3)
paymentmoodentry=Entry(root,textvariable=paymentmoodvalue).grid(row=5,column=3)

#creating checkbox
checkbtn = Checkbutton(text="remember me?",variable = checkvalue).grid(row=6,column=3)
# submit button
Button(text="submit",command=getvals).grid(row=7,column=3)
root.mainloop()
