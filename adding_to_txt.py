# import requests
# from bs4 import BeautifulSoup
import time
from datetime import date

# the_truth = True
# def adder(txt):
#     with open(txt, 'a') as file:
#         file.write('\n')
#         try:
#             name = str(input('name of company '))
#         except ValueError:
#             print('please return a url value ')
#         file.writelines(name + ' ')

#         try:
#             url = str(input('Whats the url? '))
#         except ValueError:
#             print('please return a url value ')
#         file.writelines(url + ' ')

#         try:
#             title = str(input('name of title '))
#         except ValueError:
#             print('please return a url value ')
#         file.writelines(title + ' ')

#         try:
#             loco = str(input('location? '))
#         except ValueError:
#             print('please return a url value ')
#         file.writelines(loco + ' ')

#         c_date = date.today()
#         file.writelines(str(c_date)+' ')

        

# while the_truth== True:
#     adder('my_file.txt')
#     try:
#         out_q = str(input('done? '))
#     except ValueError:
#         print('please return a url value')
#     if out_q == 'yes':
#         the_truth = False
#     else: 
#         adder('my_file.txt')



import tkinter as tk
def dios_mio():
    top = tk.Tk()

    top.iconbitmap('icon.ico')

    l1= tk.Label(top, text='Tracking my Websites')
    l1.pack()
    # no e1 only e2/l1 to e5/l5
    l2 = tk.Label(top, text='URL of company')
    l2.pack()
    e2 = tk.Entry(top, bd =5)
    e2.pack()

    l3 = tk.Label(top, text='Name of company')
    l3.pack()
    e3 = tk.Entry(top, bd =5)
    e3.pack()

    l4 = tk.Label(top, text='Position of job')
    l4.pack()
    e4 = tk.Entry(top, bd =4)
    e4.pack()

    l5 = tk.Label(top, text='Location for job')
    l5.pack()
    e5 = tk.Entry(top, bd =5)
    e5.pack()

    new_field = tk.Label(top, text='other info')
    new_field.pack()

    l6 = tk.Label(top, text='URL for other')
    l6.pack()
    e6 = tk.Entry(top, bd =5)
    e6.pack()

    l7 = tk.Label(top, text='Name for other')
    l7.pack()
    e7 = tk.Entry(top, bd =5)
    e7.pack()

    def on_submit():
        with open('my_file.txt', 'a') as f:
            f.write('\n')
            f.writelines(e2.get()+' ')
            e2.delete(0, "end")
            f.writelines(e3.get()+' ')
            e3.delete(0, "end")
            f.writelines(e4.get()+' ')
            e4.delete(0, "end")
            f.writelines(e5.get()+' ')
            e5.delete(0, "end")
            f.write('other info')
            f.writelines(e4.get()+' ')
            e6.delete(0, "end")
            f.writelines(e7.get()+' ' )
            e7.delete(0, "end")
            c_date = date.today()
            f.writelines(str(c_date)+' ')

    button = tk.Button(top, text="Save", command=on_submit)
    button.pack()

    top.mainloop()

if __name__ == '__main__':
    dios_mio()
