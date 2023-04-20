import requests
from bs4 import BeautifulSoup
import time
from datetime import date

the_truth = True
def adder(txt):
    with open(txt, 'a') as file:
        file.write('\n')
        try:
            name = str(input('name of company '))
        except ValueError:
            print('please return a url value ')
        file.writelines(name + ' ')

        try:
            url = str(input('Whats the url? '))
        except ValueError:
            print('please return a url value ')
        file.writelines(url + ' ')

        try:
            title = str(input('name of title '))
        except ValueError:
            print('please return a url value ')
        file.writelines(title + ' ')

        try:
            loco = str(input('location? '))
        except ValueError:
            print('please return a url value ')
        file.writelines(loco + ' ')

        c_date = date.today()
        file.writelines(str(c_date)+' ')

        

while the_truth== True:
    adder('my_file.txt')
    try:
        out_q = str(input('done? '))
    except ValueError:
        print('please return a url value')
    if out_q == 'yes':
        the_truth = False
    else: 
        adder('my_file.txt')


