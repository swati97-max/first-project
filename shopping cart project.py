from tkinter import Tk, W , E
from tkinter.ttk import Frame, Button, Entry,Style    
import tkinter as tk
from PIL import Image, ImageTk
class ShoppingCart(frame):
    def __init__(self):
        super().__init__()
        self.shoppinglist = []
        self.adding = True
        self.initUI()
    def initUI(self):
        def press():
            sc.delete("1.0", tk.END)
            sc.insert(tk.END, getList(self))
        def addpress():
            self.adding=not self.adding
            if self.adding==True:
                ar['text'] = "Click to Start \r Removing"
                press()
            else:
                ar['text']="Click to Start \r Adding"
                press()
        def shop(s):
            if(self.adding==True):
                self.shoppingList.append(s)
            else:
                if s in self.shoppingList:
                    self.shoppingList.remove(s)
        self.master.title("Your Shopping Store ||"
                                 " \r Location: New Delhi ||"
                                 "\r Number : 9121234567"
        ar = tk.Button(self, text= "click to Remove \r Item" , bg = "purple",fg = "white", font = 'Calibri 18 bold', width=15, height = 5, command = lambda: [addpress()])
                ar.grid(row=3,column=5)
            
        exit = tk.Button(self,text= "Exit", fg = "white",bg = "blue", font = 'Calibri 18 bold', command = self.master.destroy, width = 15, height = 5)
                exit.grid(row = 4,column = 5)

        asus = tk.Button(self,command = lambda:[shop("Asus-P25,000"),press()])
        image = ImageTk.PhotoImage(file = "asus.gif")
        asus.config(image=image,width=200,height=200, bg= "purple")
        asus.image = image
        asus.grid(row=2,column=1)
        
        dell = tk.Button(self,command = lambda:[shop("Dell- P30,000"),press()])
        image = ImageTk.photoImage(file = "dell=touchscreen.gif")
        dell.config(image = image, width = 200, height= 200, bg= "purple")
        dell.image = image
        dell.grid(row = 2,column = 2)
        
        headseat = tk.Button(self,command = lambda : [shop("headseat - P500"),press()])
        image = ImageTk.photoImage(file= "headseat.gif")
        headseat.config(image = image,width = 200,height = 200,bg = "purple")
        headseat.image = image
        headseat.grid(row = 2,column=3)
        
        hp = tk.Button(self,command = lambda : [shop("HP-P45,000"),press()])
        image = ImageTk.phoImage(file="hp.gif")
        hp.config(image=image,width=200,height=200,bg= "purple")
        hp.image= image
        hp.grid(row=2,column=4)
        
        longsleeve = tk.Button(self,command=lambda:[shop("long Sleeve-p%,000"),press()])
        image = ImageTk.PhotoImage(file="longsleeves.gif")
        longsleeve.config(image=image,width=200,height=200,bg= "purple")
        longsleeve.image = image
        longsleeve.grid(row=3,column=1)
        
        pants = tk.Button(self,command = lambda:[shop("pants-P4,500"),press()])
        image = ImageTk.photoImage(file="pants.gif")
        pants.config(image=image,width = 200,height=200,bg="purple")
        pants.image = Image
        pants.grid(row = 3,column=2)
        
        samsung = tk.Button(self,command = lambda:[shop("Samsung=p15,000"),press()])
        image = ImageTk.photoImage(file = "samsung.gif")
        samsung.config(image=image,width=200,height=200,bg="purple")
        samsung.image = image
        samsung.grid(row=3,column=3)
        
        shoes = tk.Button(self, command = lambda :[shop("shoes-p15,000"),press()])
        image = ImageTk.PhptImage(file= "shoes.gif")
        shoes.config(image=image,width=200,height=200,bg="purple")
        shoes.image = image
        shoes.grid(row=3,column=4)
        
        vivo = tk.Button(self,command = lambda:[shop("Vivo-P16,000"),press()})
        image = ImageTk.photoImage(file = "vivo.gif")
        vivo.config(image=image,width = 200,height=200,bg="purple")
        vivo.image= image
        vivo.grid(row=4,column=1)
        
        rolex = tk.Button(self,command=lambda:[shop("Rolex Watch=P12,000"),press()])
        image = ImageTk.photoImage(file="watch1.gif")
        rolex.config(image=image,width=200,height=200, bg="purple")
        rolex.image = image
        rolex.grid(row=4,column=2)
        
        applewatch = tk.Button(self,command = lambda:[shop("Apple Watcg-P10,000"),press()])
        image = ImageTk.PhotoImage(file="watch2.gif")
        applwwatch.comfig(image=image,width=200,height=200,bg="purple")
        applewatcg.image = image
        applewatch.grid(row=4,column=3)
        
        sc = tk.text(self,height = 13,width=30)
        sc.insert(tk.END,getList(self))
        sc.grid(row=2,column=5)
        
        self.pack()
      
def getList(self):
    items = 'Cart Items: \n'
    for item in self.shoppingList:
        items+= item + "\n"
    return items
def main():
    root = Tk()
    app = ShoppingCart()
    root.configure(background)
    root.mainloop()
    

\
