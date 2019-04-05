import calendar
from tkinter import *
import time
import datetime
from tkinter import ttk

_heightBtn = 30
_widthBtn = 30

month_names = tuple(calendar.month_name) 
day_names = tuple(calendar.day_abbr)
day = time.strftime("%d")
year = time.strftime("%Y") 
month = time.strftime("%B")
cal= calendar.Calendar()
month_number = time.strftime("%m")
#all_days = tuple(cal.itermonthdays(int(year), int(month_number)))
all_days = []
print(all_days)
day_str_var = ""
year_str_var = ""
month_str_var = ""
day_var = []

class CalButton(ttk.Frame):
    __initProperties = None
    
    def __init__(self, parent, **args):
        self.__initProperties = args
        
        ttk.Frame.__init__(self, parent, height=_heightBtn * self.__getArg("cHeight", 1), width=_widthBtn * self.__getArg("cWidth", 1))
        self.pack_propagate(0)
        
        self.__btn = ttk.Button(self, text=args["text"], command=self.__getArg("command"))
        self.__btn.pack(fill=BOTH, expand=1)

    def __getArg(self, nameArg, default=None):
        if nameArg in self.__initProperties:
            return self.__initProperties[nameArg]
        else:
            return default


class mydates(ttk.Frame):
    __initProperties = None
    
    def __init__(self, parent, **args):
        self.__initProperties = args
        
        ttk.Frame.__init__(self, parent)
        self.pack_propagate(0)
        
        self.__lbl = ttk.Label(self, text=args["text"])
        self.__lbl.pack(fill=BOTH, expand=1)


class MainApp(Tk):
    day_var = []

    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        self.geometry("420x240")
        self.resizable(0, 0)
        
        self.init_frames()
        self.year_str_var = StringVar()
        self.month_str_var = StringVar()
        self.day_str_var = StringVar()
        self.init_needed_vars()
        
        
        
        CalButton(self, text =  '<<', cWidth=1, command= self.previousYear).place(x=60, y=10)
        CalButton(self, text =  '<', cWidth=1, command = self.previousMonth).place(x=90, y=10)
        CalButton(self, text= ">", cwidth=1, command = self.nextMonth).place(x=300, y=10)
        CalButton(self, text=">>", cwidth=1, command= self.nextYear).place(x=330, y=10)
       
        self.month_str_var.set(self.month)
        self.selectedmonth = ttk.Label(self, textvariable = self.month_str_var, font=("Tahoma", 14, 'bold')).place(x=130, y=10)
       
        self.year_str_var.set(self.year)
        self.selectedyear = ttk.Label(self, textvariable = self.year_str_var, font=("Tahoma", 14, 'bold')).place(x=240, y=10)
        
        
        self.l1 = ttk.Label(text=self.day_names[0], font=("Tahoma", 10, 'bold')).place(x=30, y=40)
        self.l2 = ttk.Label(text=self.day_names[1], font=("Tahoma", 10, 'bold')).place(x=85, y=40)
        self.l3 = ttk.Label(text=self.day_names[2], font=("Tahoma", 10, 'bold')).place(x=140, y=40)
        self.l4 = ttk.Label(text=self.day_names[3], font=("Tahoma", 10, 'bold')).place(x=195, y=40)
        self.l5 = ttk.Label(text=self.day_names[4], font=("Tahoma", 10, 'bold')).place(x=250, y=40)
        self.l6 = ttk.Label(text=self.day_names[5], font=("Tahoma", 10, 'bold')).place(x=305, y=40)
        self.l7 = ttk.Label(text=self.day_names[6], font=("Tahoma", 10, 'bold')).place(x=360, y=40)
        
        
        mydates(self, text = self.all_days[0], font= ("Tahoma", 10)).place(x=30,y=60)
        self.d1 = ttk.Label(text = self.all_days[1], font= ("Tahoma", 10)).place(x=85,y=60)
        self.d1 = ttk.Label(text = self.all_days[2], font= ("Tahoma", 10)).place(x=140,y=60)
        self.d1 = ttk.Label(text = self.all_days[3], font= ("Tahoma", 10)).place(x=195,y=60)
        self.d1 = ttk.Label(text = self.all_days[4], font= ("Tahoma", 10)).place(x=250,y=60)
        self.d1 = ttk.Label(text = self.all_days[5], font= ("Tahoma", 10)).place(x=305,y=60)
        self.d1 = ttk.Label(text = self.all_days[6], font= ("Tahoma", 10)).place(x=360,y=60)
        self.d1 = ttk.Label(text = self.all_days[7], font= ("Tahoma", 10)).place(x=30,y=100)
        
        self.make_calendar()
    
    def days_of_month(self):
        self.day_var = ""
        self.month_var = ""
        dimeunmes = self.month_str_var.set(self.month)
        dimeunano = self.year_str_var.set(self.year)
        estosanos = int(dimeunano)
        diasdelmes = self.month_str_var.index(dimeunmes)
        all_days = tuple(cal.itermonthdays(estosanos, int(diasdelmes)))
    
      
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
        self.day = time.strftime("%d")
        self.month_number = time.strftime("%m")
        self.cal= calendar.Calendar()
        self.all_days = tuple(cal.itermonthdays(int(self.year), int(self.month_number)))
        '''self.all_days = tuple(self.cal.itermonthdays(self.year, self.month_names.index))'''
    
      
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
    
     
       
    def make_calendar(self):
        self.year = int(self.year_str_var.get())
        self.month = self.month_names.index(self.month_str_var.get())
        self.m_cal = calendar.monthcalendar(self.year, self.month)
        

    def start(self):
        self.mainloop()

       
if __name__ == '__main__':
    calc = MainApp()
    calc.start()
