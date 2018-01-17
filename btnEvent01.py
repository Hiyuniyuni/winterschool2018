from tkinter import*

def process():
        print("꺼져버려요!!")

window=Tk()
button=Button(window,text="클릭하세요!",command=process)
button.pack()

window.mainloop()
