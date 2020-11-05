


# python3  使用 tkinter
import tkinter as tk
# python2 使用 Tkinter
#import Tkinter as tk
 
 
root = tk.Tk()
#root.grid(row=6,column=6)
frame1=tk.Frame(root,bg="blue")
frame2=tk.Frame(root,bg="red")

w = tk.Label(frame1, text="Hello RUNOOB!")
w.pack()

frame1.pack(padx=1,pady=1)
frame2.pack(padx=2,pady=2)

root.mainloop()