from tkinter import *
from bs4 import BeautifulSoup
import requests

root=Tk()
definiton_text=Label(root)

def search():

    button_search.config(state='disabled')

    link_no_word= 'https://www.oxfordlearnersdictionaries.com/definition/english/'
    word = word_entry.get()
    link = link_no_word + word + "_1"
    html_text = requests.get(link, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}).text
    soup = BeautifulSoup(html_text,features="lxml")

    raw_data = (soup.find('span', { 'class' : 'def' } ))
    data = raw_data.text
    

    global definiton_text
    definition_text = Label (root, text = data )
    my_canvas.create_window ( 30, 250, anchor="nw", window = definition_text )

    text_1 = Label(root, text = "The definition is : ", font =("Helvetica",12))
    my_canvas.create_window ( 70, 200, anchor="nw", window  = text_1)

def quit():
    root.destroy()


root.title('Dictionary')
root.geometry('700x370')
my_canvas = Canvas( root, width = 330 , height = 150)
my_canvas.pack(fill="both",expand=True)


button_search = Button(root, text="Search",command = lambda: search())
button_window_sp = my_canvas.create_window( 530, 150 , anchor="nw", window = button_search)

button_quit = Button(root, text='Quit', command =quit )
button_quit_window =  my_canvas.create_window( 620, 300, anchor="nw",window=button_quit)

Title_text = Label(root, text = "Dictionary : ", font =("Helvetica",12))
title_window = my_canvas.create_window ( 187, 40, anchor="nw", window  = Title_text )



word_entry = Entry(root, width = 40, borderwidth=5)
word_entry.insert(0,"Enter the word you want to search")
word_entry_window = my_canvas.create_window(25, 150, anchor="nw",window = word_entry)

root.mainloop()