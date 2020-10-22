import socket
c=socket.socket()
c.connect(('Server Ip',9999))
#print(c.recv(1024).decode())
import tkinter as tk
root=tk.Tk()
root.geometry('400x300')
root.title("Chat App client side")

def send():
  msg=x.get()
  c.send(bytes(msg,'utf-8'))
def income():
  x=c.recv(1024).decode()
  l.configure(text=x)

  
x=tk.StringVar()
l=tk.Label(root,text='')
l.place(x=40,y=55)
e=tk.Entry(root,txtvariable=x)
e.place(x=40,y=105,height=30,width=320)
b=tk.Button(root,text='send',command=send,bg="red",fg="white")
b.place(x=160,y=140,height=40,width=80)
b2=tk.Button(root,text="refresh",command=income,bg="red",fg="white")
b2.place(x=260,y=140,height=20,width=40)
root.mainloop()
