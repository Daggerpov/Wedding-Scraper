import selenium
#from selenium.webdriver.common.keys import Keys

def navigate_to(city, category):
    print(city, category)







#just GUI stuff past this point, has nothing to do with scraping

import tkinter as tk
from tkinter import ttk 

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

        self.city_frame = tk.Frame(self.master, bg="#99aab5", bd=10)
        self.city_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')
        
        self.category_frame = tk.Frame(self.master, bg="#99aab5", bd=10)
        self.category_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

        self.submit_frame = tk.Frame(self.master, bg="#7289da", bd=10)
        self.submit_frame.place(relx=0.5, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
        

        global city_entry
        city_entry = PlaceholderEntry(self.city_frame, "City, State", "", font=('Courier', 28))
        city_entry.place(relheight=1, relwidth=1)

        
        global category_entry
        category_entry = tk.OptionMenu(self.category_frame, current_category, *options)
        category_entry.config(width=90, font=('Courier', 28))
        category_entry.place(relheight=1, relwidth=1)

        

        #submission button will redirect the user over to the instagram scraping screen upon being pressed
        submit = tk.Button(self.submit_frame, text="Search", font=('Courier', 28), bg='white',
            command=lambda: navigate_to(str(city_entry.get()), category_entry['text']))
        submit.place(relheight=1, relwidth=1)

if __name__ == '__main__':
    main()