import calendar
from tkinter import *
import time
from tkinter import ttk

month_names = tuple(calendar.month_name) 
day_names = tuple(calendar.day_abbr) 
year = time.strftime("%Y") 
month = time.strftime("%B") 
year_str_var = ""
month_str_var = ""
    
class PintaCalendario(ttk.Frame):
          
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=532, width=422)
        self.pack_propagate(0)
             
        
        self.year_str_var = StringVar()
        self.month_str_var = StringVar()
        self.init_needed_vars()
        self.fill_days()
        self.year_str_var.set(self.year)
        self.selectedyear = ttk.Label(self, textvariable = self.year_str_var, width =5)
        self.selectedyear.grid(row=0, column=3)

        self.month_str_var.set(self.month)
        self.selectedmonth = ttk.Label(self, textvariable = self.month_str_var, width =10)
        self.selectedmonth.grid(row=0, column=4)

        self.botonretryyear = ttk.Button(self, text =  '<<', width=5, command= self.previousYear)
        self.botonretryyear.grid(row=0, column=1)
        self.botonretrymonth = ttk.Button(self, text =  '<', width = 5, command = self.previousMonth)
        self.botonretrymonth.grid(row=0, column=2)
        self.botonforwardmonth = ttk.Button(self, text= ">", width=5, command = self.nextMonth)
        self.botonforwardmonth.grid(row=0, column=5)
        self.botonforwardyear = ttk.Button(self, text= ">>", width = 5, command= self.nextYear)
        self.botonforwardyear.grid(row=0, column=6)
        
        self.make_calendar()
        
    def init_frames(self):
        self.frame1 = ttk.Frame(self)
        self.frame1.pack()
        
        self.frame_days = ttk.Frame(self)
        self.frame_days.pack()
        
    def init_needed_vars(self):
        self.month_names = tuple(calendar.month_name) 
        self.day_names = tuple(calendar.day_abbr) 
        self.year = time.strftime("%Y") 
        self.month = time.strftime("%B") 
      
    def previousYear(self):
        current_year = int(self.year_str_var.get())-1
        self.year_str_var.set(current_year)

        self.make_calendar()

    def nextYear(self):
        current_year = int(self.year_str_var.get())+1
        self.year_str_var.set(current_year)

        self.make_calendar()
     
    def previousMonth(self):
        current_month = self.month_names.index(self.month_str_var.get())
        previous_month = current_month -1
        if previous_month == 0:
            self.month_str_var.set(self.month_names[12])
        else:
            self.month_str_var.set(self.month_names[current_month - 1])
        
        self.make_calendar()
                     
    def nextMonth(self):
        current_month = self.month_names.index(self.month_str_var.get())
        try:
            self.month_str_var.set(self.month_names[current_month + 1])
    
        except IndexError:
            self.month_str_var.set(self.month_names[1])
            
        self.make_calendar()
        
    def fill_days(self):
        col = 0
        
        for day in self.day_names:
            self.lbl_day = ttk.Label(self, text = day)
            self.lbl_day.grid(row=2, column = col)
            col += 1
            
    def make_calendar(self):
        self.year = int(self.year_str_var.get())
        self.month = self.month_names.index(self.month_str_var.get())
        self.m_cal = calendar.monthcalendar(self.year, self.month)
        
        try:
            for dates in self.m_cal:
                for date in dates:
                    if date ==0:
                        continue
                        
                    self.delete_buttons(date)
        
        except AttributeError:
            pass
        
        for dates in self.m_cal:
            row= self.m_cal.index(dates) +1
            for date in dates:
                col = dates.index(date)
                
                if date == 0:
                    continue

    def get_date(self, clicked=None):
        
        clicked_button = clicked.widget
        self.year = self.year_str_var.get() 
        self.month = self.month_str_var.get()
        date = clicked_button['text']
        self.full_date = self.str_format % (date, month, year) 
        print(self.full_date) 
     
        try:
            self.widget.delete(0, END) 
            self.widget.insert(0, self.full_date)
            
        except AttributeError:
            pass 
                   
     
class MainApp(Tk):
    __displayCal = None
 
    def __init__(self):
        Tk.__init__(self)
        self.title("Mi calendario con Python")
        self.resizable(0, 0)
        self.__displayCal = PintaCalendario(self)
        self.__displayCal.grid(column=1, row=1)


    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()