import re
import tkinter
import tkinter.messagebox

def onclick(btn):
    operation = ('+', '-', '*', '/', '**', '//')
    content = contentVar.get()
    if content.startswith('.'):
        content = '0' + content
    if btn in '0123456789':
        content += btn
    elif btn == '.':
        # Separate content from the +-*/ characters.
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('error', 'repeated decimal points')
            return
        else:
            content += btn
    elif btn == 'C':
        # clear
        content = ''
    elif btn == '=':
        try:
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('error', 'expression error')
            return
    elif btn in operation:
        if content.endswith(operation):
            tkinter.messagebox.showerror('error', 'continuous operators are not allowed')
            return
        content += btn
    elif btn == '√':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('error', 'expression error')
            return
    contentVar.set(content)

# Create main window
tk = tkinter.Tk()
tk.geometry('300x210')

tk.title('Calculator')
contentVar = tkinter.StringVar(tk, '')
contentEntry = tkinter.Entry(tk, textvariable=contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=20, y=10, width=260, height=30)
bvalue = ['C', '+', '-', '//', '2', '0', '1', '√', '3', '4', '5', '*', '6', '7', '8', '.', '9', '/', '**', '=']
index = 0
for row in range(5):
    for col in range(4):
        d = bvalue[index]
        index += 1
        btnDigit = tkinter.Button(tk, text=d, command=lambda x=d: onclick(x))
        btnDigit.place(x=20 + col * 70, y=50 + row * 30, width=50, height=20)
tk.mainloop()