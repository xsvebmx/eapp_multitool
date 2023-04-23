# Calculator App
from customtkinter import *
 
class App(CTk):
    def __init__(self):
        super().__init__()
 
        self.title("Calculator")
        # width
        self.evwidth = 400
        self.bwidth1 = self.evwidth/4 - 20
        self.resizable(False, False)
        self.wm_iconbitmap(os.path.join(sys.path[0], 'images/Calculator.ico'))
 
        # colors
        self.configure(fg_color="#181b1f")
        self.obc = "#fb2f64"
        self.obch = "#cc2753"
        self.nbc = "#181b1f"
        self.nbch= "#14161a"
 
        # values
        self.values = CTkEntry(master=self, width=self.evwidth)
        self.values.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
 
        # number buttons
        self.button_1 = CTkButton(master=self, text="1", command=lambda: self.g_num("1"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_2 = CTkButton(master=self, text="2", command=lambda: self.g_num("2"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_3 = CTkButton(master=self, text="3", command=lambda: self.g_num("3"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_4 = CTkButton(master=self, text="4", command=lambda: self.g_num("4"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_5 = CTkButton(master=self, text="5", command=lambda: self.g_num("5"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_6 = CTkButton(master=self, text="6", command=lambda: self.g_num("6"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_7 = CTkButton(master=self, text="7", command=lambda: self.g_num("7"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_8 = CTkButton(master=self, text="8", command=lambda: self.g_num("8"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_9 = CTkButton(master=self, text="9", command=lambda: self.g_num("9"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
        self.button_0 = CTkButton(master=self, text="0", command=lambda: self.g_num("0"), width=self.bwidth1, fg_color=self.nbc, hover_color=self.nbch)
 
        # displaying number buttons
        self.button_1.grid(row=3, column=0, pady=5, padx=10)
        self.button_2.grid(row=3, column=1, pady=5, padx=10)
        self.button_3.grid(row=3, column=2, pady=5, padx=10)
 
        self.button_4.grid(row=2, column=0, pady=5, padx=10)
        self.button_5.grid(row=2, column=1, pady=5, padx=10)
        self.button_6.grid(row=2, column=2, pady=5, padx=10)
 
        self.button_7.grid(row=1, column=0, pady=5, padx=10)
        self.button_8.grid(row=1, column=1, pady=5, padx=10)
        self.button_9.grid(row=1, column=2, pady=5, padx=10)
        self.button_0.grid(row=4, column=0, pady=5, padx=10)
     
        # operation buttons
        self.add = CTkButton(master=self, text="+", command=lambda: self.operate("+"), width=self.bwidth1, fg_color=self.obc, hover_color=self.obch)
        self.sub = CTkButton(master=self, text="-", command=lambda: self.operate("-"), width=self.bwidth1, fg_color=self.obc, hover_color=self.obch)
        self.div = CTkButton(master=self, text="/", command=lambda: self.operate("/"), width=self.bwidth1, fg_color=self.obc, hover_color=self.obch)
        self.mul = CTkButton(master=self, text="*", command=lambda: self.operate("*"), width=self.bwidth1, fg_color=self.obc, hover_color=self.obch)
 
        self.equal = CTkButton(master=self, text="=", command=self.evaluate, width=self.bwidth1)
        self.clear = CTkButton(master=self, text="clear", command=self.all_clear, width=self.bwidth1)
 
        # displaying operation buttons
        self.add.grid(row=1, column=3, pady=5, padx=10)
        self.sub.grid(row=2, column=3, pady=5, padx=10)
        self.div.grid(row=3, column=3, pady=5, padx=10)
        self.mul.grid(row=4, column=3, pady=5, padx=10)
 
        self.equal.grid(row=4, column=1, pady=5, padx=10)
        self.clear.grid(row=4, column=2, pady=5, padx=10)
     
 
    def g_num(self, n):
        new_n = self.values.get()+n
        self.values.delete(0, END)
        self.values.insert(0, new_n)
 
    def all_clear(self):
        self.values.delete(0, END)
 
    def operate(self, o):
        self.f_num = int(self.values.get())
        self.op = o
        self.values.delete(0, END)
 
    def evaluate(self):
        s_num = int(self.values.get())
        self.values.delete(0, END)
 
        if self.op == "+":
            self.values.insert(0, self.f_num + s_num)
        elif self.op == "-":
            self.values.insert(0, self.f_num - s_num)
        elif self.op == "*":
            self.values.insert(0, self.f_num * s_num)
        elif self.op == "/":
            self.values.insert(0, self.f_num / s_num)
 
 
if __name__ == "__main__":
    app = App()
    app.mainloop()