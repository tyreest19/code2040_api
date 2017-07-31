"""
Description:
    A simple python module used to analyze user data from RescueTime
Author:
    Darian Nwankwo
Date:
    July 29, 2017
"""
import ast
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import requests
import tkinter as tk
import pandas

LARGE_FONT = ("Verdana", 12)
# key = "B63YZfkGbuvB7oMUZ9U7pUSEifl9VihJj3AAcFJu"

class SaveMeTime(object):
    """
    Summary of class here

    Attributes:
        api_key:
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.daily_activity_array = self.get_daily_summary_feed()
        self.daily_activity_data_frame = self.get_categories_data()
        # self.categories = self.get_categories_data()
        self.tmp_plot()

    def get_daily_summary_feed(self):
        """ Provides a high level rollup of the the time a user has logged for
        a full 24 hour period (defined by the user’s selected time zone) """
        # array of json objects
        activity_array = requests.get(
            "https://www.rescuetime.com/anapi/daily_summary_feed?key=" +
            self.api_key
        )
        activity_array = activity_array.text # Grabs data from request as str
        activity_array = ast.literal_eval(activity_array)
        return activity_array # an array of dictionaries

    def get_categories_data(self):
        """Converts daily activities into a data frame with days as the index and the activities as columns."""
        categories = pandas.DataFrame(self.daily_activity_array)
        return categories

    def tmp_plot(self):
        self.daily_activity_data_frame.plot.line(x=self.daily_activity_data_frame.index, figsize=(12, 3),
            y='productivity_pulse')
        plt.xlabel('Days')
        plt.ylabel('Productive hours')
        plt.show()

class SaveMeTimeApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)
        # Creating our application's main frame for other content views
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Used to store the frames of our application
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        """ Used to bring a frame to the top for the user to see. """
        frame = self.frames[cont]
        frame.tkraise()

def qf(quick_print):
    print(quick_print)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne)
        )
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne)
        )
        button2.pack()

# def help():
#     print("Helping you out!")
