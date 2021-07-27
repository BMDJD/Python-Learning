from tkinter import *

questions = []
file_name = []
for num in range(1, 6):
    file_name.append("0{}.txt".format(str(num)))
for txt in file_name:
    with open('D:/photos/text/{}'.format(txt), 'r', encoding='utf-8') as f:
        questions.append(f.read().format('\n', '\n', '\n'))
print(questions)
on_hit = False
on_hit_enter = True

def main():
    for x in range(4):

        win = Tk()
        win.title('知识答答答')
        win.geometry('600x900+660+50')
        text = Label(win, text=questions[x], font=('Arial', 12), width=100, height=9, )
        text.pack(side=TOP)
        var = StringVar()
        l = Label(win, textvariable=var, bg=None, fg='black', font=('Arial', 12), width=30, height=2)
        l.pack()

        def hit_me_A():
            global on_hit
            if on_hit == False:
                on_hit = True
                var.set('A')
            else:
                on_hit = False
                var.set('')
        def hit_me_B():
            global on_hit
            if on_hit == False:
                on_hit = True
                var.set('B')
            else:
                on_hit = False
                var.set('')
        def hit_me_C():
            global on_hit
            if on_hit == False:
                on_hit = True
                var.set('C')
            else:
                on_hit = False
                var.set('')

        def hit_me_enter():
            global on_hit_enter
            if on_hit_enter == True:
                on_hit_enter = False

            else:
                on_hit_enter = True


        button_A = Button(win, text='A', font=('Arial', 12), width=30, height=2, command=hit_me_A)
        button_B = Button(win, text='B', font=('Arial', 12), width=30, height=2,command=hit_me_B)
        button_C = Button(win, text='C', font=('Arial', 12), width=30, height=2,command=hit_me_C)
        button_enter = Button(win,text='确定',font=('Arial', 12),width=10,height=2,command=hit_me_enter)

        button_A.pack()
        button_B.pack()
        button_C.pack()
        button_enter.pack()
        if on_hit_enter:
            win.mainloop()

main()
