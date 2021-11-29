from bs4 import BeautifulSoup
import requests
import pandas as pd

#Browsing Laptops
product_name1=[]
price1=[]
rating1=[]

flipkart1=requests.get("https://www.flipkart.com/laptops/~cs-g5q3mw47a4/pr?sid=6bo%2Cb5g&collection-tab-name=Browsing&wid=13.productCard.PMU_V2_3")

#print(content.status_code)

soup1=BeautifulSoup(flipkart1.content, 'html.parser')
for a in soup1.find_all('div', class_='_4rR01T'):
    product_name1.append(a.get_text())
i=0
for a in soup1.find_all('div', class_='_3LWZlK'):
    rating1.append(a.get_text())
    i=i+1
    if i==len(product_name1):
        break
for a in soup1.find_all('div', class_='_30jeq3 _1_WHN1'):
    price1.append(a.get_text())

browsing_laptop=pd.DataFrame({
    "Name": product_name1,
    "Price": price1,
    "Rating": rating1
})
print("BROWSING LAPTOPS")
print(browsing_laptop)

#Performance Laptops
product_name2=[]
price2=[]
rating2=[]
i=0
flipkart2=["https://www.flipkart.com/laptops/~cs-kfthfhsblc/pr?sid=6bo%2Cb5g&collection-tab-name=Performance&wid=14.productCard.PMU_V2_4","https://www.flipkart.com/laptops/~cs-kfthfhsblc/pr?sid=6bo%2Cb5g&collection-tab-name=Performance&wid=14.productCard.PMU_V2_4&page=2"]

#print(content.status_code)
for link in flipkart2:
    
    x=requests.get(link)
    soup2=BeautifulSoup(x.content, 'html.parser')
    
    for a in soup2.find_all('div', class_='_4rR01T'):
        product_name2.append(a.get_text())
    
    for a in soup2.find_all('div', class_='_3LWZlK'):
        rating2.append(a.get_text())
        i=i+1
        if i==len(product_name2):
            break
    for a in soup2.find_all('div', class_='_30jeq3 _1_WHN1'):
        price2.append(a.get_text())
    
performance_laptop=pd.DataFrame({
    "Name": product_name2,
    "Price": price2,
    "Rating": rating2
})
print("\n\nPerformance Laptops")
print(performance_laptop)

#Gaming Laptop
product_name3=[]
price3=[]
rating3=[]
i=0
flipkart3=["https://www.flipkart.com/laptops/~cs-umaioepjhw/pr?sid=6bo%2Cb5g&collection-tab-name=Gaming&wid=16.productCard.PMU_V2_5","https://www.flipkart.com/laptops/~cs-umaioepjhw/pr?sid=6bo%2Cb5g&collection-tab-name=Gaming&wid=16.productCard.PMU_V2_5&page=2"]

#print(content.status_code)
for link in flipkart3:
    
    x=requests.get(link)
    soup3=BeautifulSoup(x.content, 'html.parser')
    
    for a in soup3.find_all('div', class_='_4rR01T'):
        product_name3.append(a.get_text())
    
    for a in soup3.find_all('div', class_='_3LWZlK'):
        rating3.append(a.get_text())
        i=i+1
        if i==len(product_name3):
            break
    for a in soup3.find_all('div', class_='_30jeq3 _1_WHN1'):
        price3.append(a.get_text())
    
gaming_laptop=pd.DataFrame({
    "Name": product_name3,
    "Price": price3,
    "Rating": rating3
})
print("\n\nGaming Laptops")
print(gaming_laptop)

#Mobiles
product_name4=[]
price4=[]
rating4=[]
i=0
flipkart4 = ["https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1", "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=2", "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=3"]

for link in flipkart4:
    x=requests.get(link)

    soup4=BeautifulSoup(x.content, 'html.parser')
    for a in soup4.find_all('div', class_='_4rR01T'):
        product_name4.append(a.get_text())

    for a in soup4.find_all('div', class_='_3LWZlK'):
        rating4.append(a.get_text())
        i=i+1
        if i==len(product_name4):
            break
    for a in soup4.find_all('div', class_='_30jeq3 _1_WHN1'):
        price4.append(a.get_text())

mobile=pd.DataFrame({
    "Name": product_name4,
    "Price": price4,
    "Rating": rating4
})
print("mobiles")
print(mobile)


# user interface 


from tkinter import *
import sys

def laptops():
    laptop_win=Tk()
    laptop_win.geometry("1000x600")
    laptop_win.resizable(width="False",height="False")
    txt = Text(laptop_win,height=100,width=200,bg='#f0f0f2',spacing1=2) 
    class PrintToTXT(object): 
        def write(self, s): 
             txt.insert(END, s)
    sys.stdout = PrintToTXT() 
    print("Browsing Laptops")
    print(browsing_laptop)
    print("\n\nPerformance Laptops")
    print(performance_laptop)
    print("\n\nGaming Laptops")
    print(gaming_laptop)
    txt.config(state='disabled')
    txt.pack(expand="True") 
    laptop_win.mainloop()


def mobiles():
    mobile_win=Tk()
    mobile_win.geometry("1000x600")
    mobile_win.resizable(width="False",height="False")
    txt = Text(mobile_win,height=100,width=200,bg='#f0f0f2',spacing1=2) 
    class PrintToTXT(object): 
        def write(self, s): 
             txt.insert(END, s)
    sys.stdout = PrintToTXT()
    print("Mobiles")
    with pd.option_context('display.max_rows',None,'display.max_columns',None):
        print(mobile)
    txt.config(state='disabled')
    txt.pack(expand="True")
    mobile_win.mainloop()


root = Tk()      
root.resizable(height=FALSE,width=FALSE)
root.geometry("902x480")
root.config(bg="#F0F0F2")
pic_frame=Frame(root,bg="#F0F0F2")
pic_frame.grid(row=1,column=0)
buttons_frame=Frame(root,bg="#F0F0F2")
buttons_frame.grid(row=2,column=0,)

img1 = PhotoImage(file="D:\laptop.png") 
laptop=Button(pic_frame,image=img1,background="#F0F0F2",border=0,padx=0,pady=0, command = laptops)  
laptop.grid(row=0,column=0,padx=(130,65),pady=50) 

img2=PhotoImage(file="D:\phone.png")
phone=Button(pic_frame,image=img2,background="#F0F0F2",border=0,padx=0,pady=0, command = mobiles)
phone.grid(row=0,column=1,padx=(90,100),pady=50)

button1=Button(buttons_frame,bg="#F0F0F2",fg="navy",text="Search Laptops",font=("Lato",20,"bold"),border=0)
button1.grid(row=0,column=0,padx=(30,0))

button2=Button(buttons_frame,bg="#F0F0F2",fg="navy",text="Search Phones",font=("Lato",20,"bold"),border=0)
button2.grid(row=0,column=1,padx=(220,15))

root.mainloop()