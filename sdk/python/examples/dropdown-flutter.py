from concurrent.futures import thread
from pickletools import string1
from time import sleep
import flet
from flet import Stack, Button, Dropdown, dropdown

page = flet.page("page-1", no_window=True)

dd = Dropdown(options=[
    dropdown.Option("a", "Item A"),
    dropdown.Option("b", "Item B"),
    dropdown.Option("c", "Item C")
])

def btn2_click(e):
    dd.options.append(dropdown.Option("d", "Item D"))
    page.update()

def btn3_click(e):
    dd.options[1].text = "Item Blah Blah Blah"
    page.update()    

btn2 = Button("Add new item!", on_click=btn2_click)
btn3 = Button("Change second item", on_click=btn3_click)

page.add(dd, btn2, btn3)

input()