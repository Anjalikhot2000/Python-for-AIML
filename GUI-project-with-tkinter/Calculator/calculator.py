# NoTE: Works on only two numbers at a time and does not support decimal numbers. It also does not support chaining of operations (e.g., 2 + 3 * 4 will not work as expected).

from tkinter import *


first_num=second_num=operator=None

def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)


def get_operator(op):
    global first_num,operator
    first_num=int(result_label['text'])
    operator=op
    result_label.config(text="")

def get_res():
    global first_num,second_num,operator
    second_num=result_label['text']
    if operator=='+':
        result_label.config(text=str(first_num+int(second_num)))
    elif operator=='-':
        result_label.config(text=str(first_num-int(second_num)))
    elif operator=='*':
        result_label.config(text=str(first_num*int(second_num)))
    elif operator=='/':
        if second_num=='0':
            result_label.config(text="Error")
        else:
            result_label.config(text=str(round(first_num/int(second_num),2)))   


root = Tk()

root.title("Simple Calculator")
root.geometry("280x380")
root.resizable(0, 0)
root.configure(bg="black")

result_label=Label(root,text="",bg="black",fg="white")
result_label.grid(row=0,column=0,pady=(50,25),columnspan=5,sticky='w')
result_label.config(font=("Arial", 30,'bold'))

btn7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("Arial", 14,'bold'))

btn8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("Arial", 14,'bold'))

btn9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("Arial", 14,'bold'))

btn_add=Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=("Arial", 14,'bold'))


btn4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("Arial", 14,'bold'))

btn5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("Arial", 14,'bold'))

btn6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("Arial", 14,'bold'))

btn_sub=Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=("Arial", 14,'bold'))


btn1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("Arial", 14,'bold'))

btn2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("Arial", 14,'bold'))

btn3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("Arial", 14,'bold'))

btn_mul=Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=("Arial", 14,'bold'))


btn_clr=Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command=lambda:result_label.config(text=""))
btn_clr.grid(row=4,column=0)
btn_clr.config(font=("Arial", 14,'bold'))

btn0=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("Arial", 14,'bold'))

btn_equals=Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_res())
btn_equals.grid(row=4,column=2)
btn_equals.config(font=("Arial", 14,'bold'))

btn_div=Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=("Arial", 14,'bold'))



root.mainloop()