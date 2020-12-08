from selenium import webdriver
from bs4 import BeautifulSoup 
import requests 
import csv 

from time import sleep
from random import randint

import tkinter as tk
from tkinter import ttk 

def randomize_sleep(min, max):
    sleep(randint(min*100, max*100) / 100)

def navigate_to(city_state, category):
    PATH = "/Users/daggerpov/Documents/GitHub/Wedding-Scraper/chromedriver"
    driver = webdriver.Chrome(PATH)
    
    driver.get("https://www.theknot.com/marketplace")
    randomize_sleep(1,3)
    
    
    #category selection
    category_select_button = driver.find_element_by_xpath(
        '//*[@id="search"]/div[2]/div/div[3]/div/button'
    )
    category_select_button.click()
    randomize_sleep(1,2)

    category_selections = driver.find_elements_by_class_name(
        "iconContainer--c9323"
    )
    select_category = options.index(category)
    category_selections[select_category].click()
    randomize_sleep(1, 2)
    
    #city, state selection
    city_state_label = driver.find_element_by_xpath(
        '//input[@class="input--13524 field-base--4deb4 body1--fd844 base--04622 ease-out--4b40a input-with-animated-label--01fe4 is-neutral--2a4f7"]'
    )
    city_state_label.send_keys(city_state)
    randomize_sleep(1,2)

    select_city_state = driver.find_element_by_xpath(
        '//li[@class="item--8670e item-base--4a1f5"]'
    )
    select_city_state.click()
    randomize_sleep(1, 2)

    search_button = driver.find_element_by_xpath(
        '//button[@class="btn--62697 btn-transitions--893d4 md--97c77 buttonM--26f25 primary--52a11 searchBtn--4cca7"]'
    )
    search_button.click()
    randomize_sleep(0.5, 1)

    try:
        vendors = driver.find_elements_by_xpath('//*[@class="click-container--48a45"]')
        randomize_sleep(1, 2)
    except:
        exit()

    randomize_sleep(1, 2)
    for vendor in vendors:
        vendor.click()
        randomize_sleep(10, 11)
        '''link = vendor.get_attribute('href')

        header = {"From": "Daniel Agapov <danielagapov1@gmail.com>", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }

        response = requests.get(link, headers=header)
        if response.status_code != 200: 
            print("Failed to get HTML:", response.status_code, response.reason)
            exit()
        
        soup = BeautifulSoup(response.text, "html5lib")

        randomize_sleep(4, 5)'''

        #find address
        address = driver.find_element_by_xpath('//p[@class="address--2d91e body1--fd844"]').text
        
        #find website
        website = driver.find_element_by_css_selector("#with-pricing-range > div > div.website-call-buttons--1ef6e > div:nth-child(1) > span > a").get_attribute('href')

        #find phone number
        phone_number = driver.find_element_by_css_selector('#navContact > div > div > div.order-md-1--7a6e1.col-sm-12--f2343.col-md-9--a303f > div.contact-info--37f24.body1--fd844')
        phone_number = phone_number.find_elements_by_tag_name('span').text
        for i in phone_number:
            if ',' not in i:
                phone_number = i

        print(address, website, phone_number)
    

    
    







#just GUI stuff past this point, has nothing to do with scraping


HEIGHT = 768
WIDTH = 1366

def main():
    #initializing module
    root = tk.Tk()
    
    global app
    #setting the current screen to start menu
    app = main_screen(root)
    
    #overall GUI loop which will run constantly, accepting input and such
    root.mainloop()


class PlaceholderEntry(ttk.Entry):
    #initializing the arguments passed in
    def __init__(self, container, placeholder, validation, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        self.insert("0", self.placeholder)
        
        #runs the appropriate method for when the user is focused in/out of the element
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
        #if this argument is given (like for the instagram password, 
        # then the entry box will hide its text with asterisks)
        self.validation = validation

    
    def _clear_placeholder(self, e):
        #deleting all text placed automatically with the placeholder
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"
        
        #editing the property of the entry box 'show' to display asterisks ,
        #instead of any of the entered characters
        if self.validation == 'password':
            self['show'] = "*"
        
    def _add_placeholder(self, e):
        #if there isn't any text entered in AND the user isn't focused in 
        #on this, then it'll add the placeholder
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"


class main_screen():
    def __init__(self, master):
        #same property adjustments as used for the weather screen
        self.master = master
        self.master.title("Wedding Scraper GUI")
        self.canvas = tk.Canvas(self.master, height=HEIGHT, width=WIDTH, bg = '#23272a')
        self.canvas.pack()
        self.master.config(bg = "#23272a")
        self.master.resizable(width=False, height=False)

        
        self.style = ttk.Style(self.master)
        self.style.configure("Placeholder.TEntry", foreground="#d5d5d5")

        global options

        options = [
            "Reception Venues", 
            "Wedding Photographers",
            "Videographers",
            "Bridal Salons",
            "Beauty",
            "DJs",
            "Wedding Bands",
            "Florists",
            "Wedding Planners",
            "Hotel Room Blocks", 
            "Jewelers",
            "Wedding Cakes",
            "Accessories",
            "Alterations & Preservation",
            "Bar Services & Beverages",
            "Bed and Breakfasts",
            "Boudoir Photographers",
            "Calligraphers",
            "Caterers",
            "Ceremony Accessories",
            "Ceremony Venues", 
            "Dance Lessons",
            "Decor",
            "Desserts",
            "Ensembles & Soloists",
            "Favors & Gifts",
            "Fitness",
            "Invitations & Paper Goods",
            "Lighting",
            "Menswear",
            "Newlywed Services",
            "Officiants & Premarital Counseling",
            "Photo Booths",
            "Registry Services",
            "Rehearsal Dinners, Bridal Showers & Parties",
            "Rentals",
            "Service Staff",
            "Technology",
            "Transportation",
            "Travel Specialists",
            "Vacation Homes & Villas",
            "Variety Acts",
            "Wedding Designers",
            "Wedding Jewelry"
        ]

        current_category = tk.StringVar(self.master)
        current_category.set(options[0])

        self.city_state_frame = tk.Frame(self.master, bg="#99aab5", bd=10)
        self.city_state_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')
        
        self.category_frame = tk.Frame(self.master, bg="#99aab5", bd=10)
        self.category_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

        self.submit_frame = tk.Frame(self.master, bg="#7289da", bd=10)
        self.submit_frame.place(relx=0.5, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
        

        global city_state_entry
        city_state_entry = PlaceholderEntry(self.city_state_frame, "City, State", "", font=('Courier', 28))
        city_state_entry.place(relheight=1, relwidth=1)

        
        global category_entry
        category_entry = tk.OptionMenu(self.category_frame, current_category, *options)
        category_entry.config(width=90, font=('Courier', 28))
        category_entry.place(relheight=1, relwidth=1)

        

        #submission button will redirect the user over to the instagram scraping screen upon being pressed
        submit = tk.Button(self.submit_frame, text="Search", font=('Courier', 28), bg='white',
            command=lambda: navigate_to(str(city_state_entry.get()), category_entry['text']))
        submit.place(relheight=1, relwidth=1)

if __name__ == '__main__':
    main()