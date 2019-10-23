from tkinter import*
import random
import time ;
root=Tk()
root.geometry("1600x800+0+0")
root.title("my project")

text_Input= StringVar()
operator=("")

Tops=Frame(root,width=1600,bg="white",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root, width=800,height=700, bg="white",relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,bg="white",relief=SUNKEN)
f2.pack(side=RIGHT)
#-----------------------------time-----------------------------------------
localtime=time.asctime(time.localtime(time.time()))   #Date and time
#----------------------------Info-------------------------------------
lbInfo=Label(Tops, font=('arial',50,'bold'),text= "my project",fg="blue",bd=10,anchor='w')
lbInfo.grid(row=0,column=0)
lbInfo=Label(Tops, font=('arial',20,'bold'),text= localtime,fg="Red",bd=10,anchor='w')
lbInfo.grid(row=1,column=0)

#---------------------------------calculator-----------------------------
def btnClick(numbers):
    global operator
    operator = operator + str (numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    text_Input.set("")

def btnEqualsInput():
    global operator
    sump=str(eval (operator))
    text_Input.set(sump)
    operator=""

def Ref():
    x= random.randint(10908,500876)
    randomRef = str(x)
    rand.set(randomRef)

    
    CoSamosha =float(Samosha.get())
    CoD =float(Drinks.get())
    COFries=float(Fries.get())
    CoBurger=float(Burger.get())
    CoChicken_Burger=float(Chicken_Burger .get())
    CoCheese_Burger=float(Cheese_Burger.get())

    costofSamosha=CoSamosha*10
    costofDrinks=CoD*20
    costofBurger=CoBurger*40
    costofChicken_Burger=CoChicken_Burger*100
    costoCheese_Burger=CoCheese_Burger*80
    costofFries=COFries*30

    Costofmeal = "Rs" , str('%.2f'%(costofSamosha + costofDrinks + costofBurger+ costofFries
                                    + costofChicken_Burger + costoCheese_Burger))

    payTax=((costofSamosha + costofDrinks + costofBurger+ costofFries
             + costofChicken_Burger + costoCheese_Burger)*0.2)
    
    Totalcost=(costofSamosha + costofDrinks + costofBurger+ costofFries
               + costofChicken_Burger + costoCheese_Burger)
    
    ser_Charge = ((costofSamosha + costofDrinks + costofBurger+ costofFries
                   + costofChicken_Burger + costoCheese_Burger)/99)
    
    service="Rs",str('%.2f'% ser_Charge)
    
    OverAllcost="Rs",str('%.2f'%(payTax + Totalcost + ser_Charge))
    paidTax="Rs",str('%.2f'% payTax)

    Ser_Charge.set(service)
    Cost.set(Costofmeal)
    Tax.set(paidTax)
    SubTotal.set(Totalcost)
    totalcost.set(OverAllcost)
            

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Samosha.set("")
    Burger.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
    Drinks.set("")
    Cost.set("")
    Ser_Charge.set("")
    Tax.set("")
    SubTotal.set("")
    totalcost.set("")
    

txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30, insertwidth=4,bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)
#----------------------------------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda: btnClick(3)).grid(row=4,column=2)
Multipy=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=4,column=3)
#--------------------------------------------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)
#---------------------------------------------------------------Resturent info 1---------------------------------------------------------------
rand=StringVar()
Fries=StringVar()
Samosha=StringVar()
Burger=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()
lblReference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10 ,insertwidth=4,
                   bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font=('arial',16,'bold'),text="Fries",bd=16, anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10 ,insertwidth=4,
                   bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

lblSamosha = Label(f1,font=('arial',16,'bold'),text="Samosha ",bd=16, anchor='w')
lblSamosha .grid(row=2,column=0)
txtSamosha =Entry(f1,font=('arial',16,'bold'),textvariable=Samosha ,bd=10 ,insertwidth=4,
                   bg="powder blue",justify='right')
txtSamosha .grid(row=2,column=1)

lblBurger = Label(f1,font=('arial',16,'bold'),text="Burger",bd=16, anchor='w')
lblBurger .grid(row=3,column=0)
txtBurger =Entry(f1,font=('arial',16,'bold'),textvariable=Burger ,bd=10 ,insertwidth=4,
                   bg="powder blue",justify='right')
txtBurger .grid(row=3,column=1)

lblChicken_Burger= Label(f1,font=('arial',16,'bold'),text="Chicken meal",bd=16, anchor='w')
lblChicken_Burger.grid(row=4,column=0)
txtChicken_Burger=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Burger,bd=10 ,insertwidth=4,
                   bg="powder blue",justify='right')
txtChicken_Burger.grid(row=4,column=1)

lblCheese_Burger= Label(f1,font=('arial',16,'bold'),text="Cheese meal",bd=16, anchor='w')
lblCheese_Burger.grid(row=5,column=0)
txtCheese_Burger=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_Burger,bd=10 ,insertwidth=4,
                   bg="powder blue",justify='right')
txtCheese_Burger.grid(row=5,column=1)

#------------------------------------------------------------Resturent info 2------------------------------------------------------------------------
Drinks=StringVar()
Cost=StringVar()
Ser_Charge=StringVar()
Tax=StringVar()
SubTotal=StringVar()
totalcost=StringVar()
lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10 ,insertwidth=4,
                   bg="white",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1,font=('arial',16,'bold'),text="cost of meal",bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10 ,insertwidth=4,
                   bg="white",justify='right')
txtCost.grid(row=1,column=3)

lblSer_Charge= Label(f1,font=('arial',16,'bold'),text="Service charge ",bd=16, anchor='w')
lblSer_Charge.grid(row=2,column=2)
txtSer_Charge =Entry(f1,font=('arial',16,'bold'),textvariable=Ser_Charge ,bd=10 ,insertwidth=4,
                   bg="white",justify='right')
txtSer_Charge.grid(row=2,column=3)

lblTax = Label(f1,font=('arial',16,'bold'),text="GST",bd=16, anchor='w')
lblTax .grid(row=3,column=2)
txtTax =Entry(f1,font=('arial',16,'bold'),textvariable=Tax ,bd=10 ,insertwidth=4,
                   bg="white",justify='right')
txtTax .grid(row=3,column=3)

lblSubTotal = Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16, anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal ,bd=10 ,insertwidth=4,
                   bg="white",justify='right')
txtSubTotal.grid(row=4,column=3)

lbltotalcost= Label(f1,font=('arial',16,'bold'),text="Total cost",bd=16, anchor='w')
lbltotalcost.grid(row=5,column=2)
txttotalcost=Entry(f1,font=('arial',16,'bold'),textvariable=totalcost,bd=10 ,insertwidth=4,
                   bg="white",justify='right')
txttotalcost.grid(row=5,column=3)
#-----------------------------------------button----------------------------------------------------
btnTotal=Button(f1,padx=16,pady=8,fg="Black",font=('arial',16,'bold'),width=10,
                text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,fg="Black",font=('arial',16,'bold'),width=10,
                text="Reset", bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,fg="Black",font=('arial',16,'bold'),width=10,
                text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)
































root.mainloop()
