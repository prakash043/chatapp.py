import socket
s=socket.socket()
s.bind(('your ip',port))
print("server up")
s.listen(3)
import tkinter as tk
root=tk.Tk()
root.geometry('400x540')
root.title("chat app server side")
root.configure(bg="black")
c,addr=s.accept()
print("connection with",addr)
def send():
  global msg
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
