import json
import configparser
import requests
import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title('Sticker Stonks')


bought_stock_chall = config.getfloat('prices', 'stock_chall')
bought_stock_con = config.getfloat('prices', 'stock_con')
bought_ant_chall = config.getfloat('prices', 'ant_chall')
bought_rio_leg = config.getfloat('prices', 'rio_leg')
bought_rio_chall = config.getfloat('prices', 'rio_chall')

number_of_rio_leg = config.getint('number_bought', 'rio_leg')
number_of_rio_chall = config.getint('number_bought', 'rio_chall')
number_of_stock_chall = config.getint('number_bought', 'stock_chall')
number_of_stock_con = config.getint('number_bought', 'stock_con')
number_of_ant_chall = config.getint('number_bought', 'ant_chall')


stock_con = 1.3
stonks_stock_con = ((float(stock_con) - bought_stock_con)/bought_stock_con)*100

stock_chall = 1.67
stonks_stock_chall = (
    (float(stock_chall) - bought_stock_chall)/bought_stock_chall)*100

ant_chall = 0.19
stonks_ant_chall = ((float(ant_chall) - bought_ant_chall)/bought_ant_chall)*100

rio_leg = 0.19
stonks_rio_leg = ((float(rio_leg) - bought_rio_leg)/bought_rio_leg)*100

rio_chall = 0.15
stonks_rio_chall = ((float(rio_chall) - bought_rio_chall)/bought_rio_chall)*100

total_money_gain = ((stock_con*number_of_stock_con) + (stock_chall*number_of_stock_chall) + (
    ant_chall*number_of_ant_chall) + (rio_leg*number_of_rio_leg) + (rio_chall*number_of_rio_chall))
total_percentage_gain = ((total_money_gain - 1000)/1000)*100

if stock_con < 0:
    stock_con_colour = "red"
elif stock_con == 0:
    stock_con_colour = "black"
else:
    stock_con_colour = "green"

if stock_con < bought_stock_con:
    stock_con_label_colour = "red"
elif stock_con == bought_stock_con:
    stock_con_label_colour = "black"
else:
    stock_con_label_colour = "green"

if stock_chall < 0:
    stock_chall_colour = "red"
elif stock_chall == 0:
    stock_chall_colour = "black"
else:
    stock_chall_colour = "green"

if stock_chall < bought_stock_chall:
    stock_chall_label_colour = "red"
elif stock_chall == bought_stock_chall:
    stock_chall_label_colour = "black"
else:
    stock_chall_label_colour = "green"

if ant_chall < 0:
    ant_chall_colour = "red"
elif ant_chall == 0:
    ant_chall_colour = "black"
else:
    ant_chall_colour = "green"

if ant_chall < bought_ant_chall:
    ant_chall_label_colour = "red"
elif ant_chall == bought_ant_chall:
    ant_chall_label_colour = "black"
else:
    ant_chall_label_colour = "green"

if rio_leg < 0:
    rio_leg_colour = "red"
elif rio_leg == 0:
    rio_leg_colour = "black"
else:
    rio_leg_colour = "green"

if rio_leg < bought_rio_leg:
    rio_leg_label_colour = "red"
elif rio_leg == bought_rio_leg:
    rio_leg_label_colour = "black"
else:
    rio_leg_label_colour = "green"

if rio_chall < 0:
    rio_chall_colour = "red"
elif rio_chall == 0:
    rio_chall_colour = "black"
else:
    rio_chall_colour = "green"

if rio_chall < bought_rio_chall:
    rio_chall_label_colour = "red"
elif rio_chall == bought_rio_chall:
    rio_chall_label_colour = "black"
else:
    rio_chall_label_colour = "green"

if (total_money_gain-1000) < 0:
    total_money_colour = "red"
elif (total_money_gain-1000) == 0:
    total_money_colour = "black"
else:
    total_money_colour = "green"

if total_percentage_gain < 0:
    total_percentage_colour = "red"
elif total_percentage_gain == 0:
    total_percentage_colour = "black"
else:
    total_percentage_colour = "green"


stock_con_label = Label(
    root, text="Current price of Stockholm Contenders: ").grid(row=0, column=0)
stock_con_price_label = Label(root, text="£{:.2f}".format(
    stock_con), foreground=stock_con_label_colour, font=("", 10, "bold")).grid(row=0, column=1)
stonks_stock_con_label = Label(
    root, text="Stockholm Contenders percentage gain = ").grid(row=1, column=0)
stonks_stock_con_percentage_label = Label(root, text="{:.2f}".format(
    stonks_stock_con) + "%", foreground=stock_con_colour, font=("", 10, "bold")).grid(row=1, column=1)

stock_chall_label = Label(
    root, text="Current price of Stockholm Challengers: ").grid(row=2, column=0)
stock_chall_price_label = Label(root, text="£{:.2f}".format(
    stock_chall), foreground=stock_chall_label_colour, font=("", 10, "bold")).grid(row=2, column=1)
stonks_stock_chall_label = Label(
    root, text="Stockholm Contenders percentage gain = ").grid(row=3, column=0)
stonks_stock_chall_percentage_label = Label(root, text="{:.2f}".format(
    stonks_stock_chall) + "%", foreground=stock_chall_colour, font=("", 10, "bold")).grid(row=3, column=1)

ant_chall_label = Label(
    root, text="Current price of Antwerp Challengers: ").grid(row=4, column=0)
ant_chall_price_label = Label(root, text="£{:.2f}".format(
    ant_chall), foreground=ant_chall_label_colour, font=("", 10, "bold")).grid(row=4, column=1)
stonks_ant_chall_label = Label(
    root, text="Antwerp Challengers percentage gain = ").grid(row=5, column=0)
stonks_ant_chall_percentage_label = Label(root, text="{:.2f}".format(
    stonks_ant_chall) + "%", foreground=ant_chall_colour, font=("", 10, "bold")).grid(row=5, column=1)

rio_leg_label = Label(
    root, text="Current price of Rio Legends: ").grid(row=6, column=0)
rio_leg_price_label = Label(root, text="£{:.2f}".format(
    rio_leg), foreground=rio_leg_label_colour, font=("", 10, "bold")).grid(row=6, column=1)
stonks_rio_leg_label = Label(
    root, text="Rio Legends percentage gain = ").grid(row=7, column=0)
stonks_rio_leg_percentage_label = Label(root, text="{:.2f}".format(
    stonks_rio_leg) + "%", foreground=rio_leg_colour, font=("", 10, "bold")).grid(row=7, column=1)

rio_chall_label = Label(
    root, text="Current price of Rio Challengers: ").grid(row=8, column=0)
rio_chall_price_label = Label(root, text="£{:.2f}".format(
    rio_chall), foreground=rio_chall_label_colour, font=("", 10, "bold")).grid(row=8, column=1)
stonks_rio_chall_label = Label(
    root, text="Rio Challengers percentage gain = ").grid(row=9, column=0)
stonks_rio_chall_percentage_label = Label(root, text="{:.2f}".format(
    stonks_rio_chall) + "%", foreground=rio_leg_colour, font=("", 10, "bold")).grid(row=9, column=1)

total_money_gain_label = Label(
    root, text="Total money gain:").grid(row=10, column=0)
total_money_gain_price_label = Label(root, text=" £{:.2f}".format(
    total_money_gain-1000), foreground=total_money_colour, font=("", 10, "bold")).grid(row=10, column=1)
total_percentage_gain_label = Label(
    root, text="Total percentage gain:").grid(row=11, column=0)
total_percentage_gain_price_label = Label(root, text=" {:.2f}".format(
    total_percentage_gain) + "%", foreground=total_percentage_colour, font=("", 10, "bold")).grid(row=11, column=1)

root.mainloop()
