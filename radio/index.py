import tkinter as tk


calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0,calculation)


def evaluate_calculation():
    global calculation
    try:  
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")
     

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "END")

root = tk.Tk()
root.geometry('300x275')

text_result = tk.Text(root, height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)
    
yetti =tk.Button(root, text="7",command=lambda:add_to_calculation(7))
yetti.grid(column=0, row=2 )
tort=tk.Button(root, text="4",command=lambda:add_to_calculation(4) ).grid(column=0, row=3)
bir=tk.Button(root, text="1",command=lambda:add_to_calculation(1) ).grid(column=0, row=4)
nol=tk.Button(root, text="0",command=lambda:add_to_calculation(0 )).grid(column=0, row=5)
sakkiz=tk.Button(root, text="8", command=lambda:add_to_calculation(8)).grid(column=1, row=2)
besh=tk.Button(root, text="5", command=lambda:add_to_calculation(5)).grid(column=1, row=3)
ikki=tk.Button(root, text="2", command=lambda:add_to_calculation(2)).grid(column=1, row=4)
toqqiz=tk.Button(root, text="9", command=lambda:add_to_calculation(9)).grid(column=2, row=2)
olti=tk.Button(root, text="6", command=lambda:add_to_calculation(6)).grid(column=2, row=3)
uch=tk.Button(root, text="3", command=lambda:add_to_calculation(3)).grid(column=2, row=4)
plus=tk.Button(root, text="+", command=lambda:add_to_calculation("+")).grid(column=1, row=1)
minus=tk.Button(root, text="-", command=lambda:add_to_calculation("-")).grid(column=1, row=5)
kopaytirish=tk.Button(root, text="*", command=lambda:add_to_calculation("*")).grid(column=2, row=1)
bolish=tk.Button(root, text="/", command=lambda:add_to_calculation("/")).grid(column=0, row=1)
teng=tk.Button(root, text="=", command=lambda:evaluate_calculation("=")).grid(column=2, row=5)
C=tk.Button(root, text="C", command=lambda:clear_field("C")).grid(column=2, row=6)
root.mainloop()