from tkinter import *
import calendar
import time
import datetime
from tkinter import ttk
 
_heightBtn = 30
_widthBtn = 30
 
cal= calendar.Calendar()
day_str_var = ""
year_str_var = ""
month_str_var = ""
   
class MyButton(ttk.Frame):
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
 
class  MiCalendario(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Tkinter")
        self.geometry("420x295")
        self.resizable(0,0)
        self.neededVars()
       
        self.year_str_var = StringVar()
        self.month_str_var = StringVar()
        self.day_str_var = StringVar()
        
        self.__Esqueleto__()
        self.__createDaysNames__()
        self.PintaDias()
 
    def __Esqueleto__(self):
             
        MyButton(self, text = '<<', cWidth=1, command= self.previousYear).place(x=60, y=10)
        MyButton(self, text =  '<', cWidth=1, command = self.previousMonth).place(x=90, y=10)
        MyButton(self, text= ">", cwidth=1, command = self.nextMonth).place(x=300, y=10)
        MyButton(self, text=">>", cwidth=1, command= self.nextYear).place(x=330, y=10)
       
        self.month_str_var.set(self.month)
        self.selectedmonth = ttk.Label(self, textvariable = self.month_str_var, font=("Tahoma", 14, 'bold')).place(x=130, y=10)
       
        self.year_str_var.set(self.year)
        self.selectedyear = ttk.Label(self, textvariable = self.year_str_var, font=("Tahoma", 14, 'bold')).place(x=240, y=10)
 
    def __createDaysNames__(self):
        dias = self.day_names
        for i in range(7):
            f = ttk.Frame(self, width=60, height=25)
            f.pack_propagate(0)
            ttk.Label(f, text=dias[i], font=('Tahoma', 10, 'bold'), anchor=CENTER, borderwidth=0.5, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x=i*60, y=50)
   
    def PintaDias(self):
       
        self.all_days = [day if day else '' for day in cal.itermonthdays(int(self._year), int(self._month))]
       
        for i in range(5):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=70)

        for i in range(5,7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove', foreground = '#C00D1E').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=70)

     
        for i in range(5):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 7], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=115)
            
        for i in range(5, 7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 7], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove', foreground = '#C00D1E').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=115)
           
        for i in range(7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 14], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=160)
            
        for i in range(5, 7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 14], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove', foreground = '#C00D1E').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=160)
            
        for i in range(7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 21], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=205)

        for i in range(5,7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 21], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove', foreground = '#C00D1E').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=205)
            
        for i in range(7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 28], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=250)

        for i in range(5,7):
            f = ttk.Frame(self, width=60, height= 45)
            f.pack_propagate(0)
            ttk.Label(f, text=self.all_days[i + 28], font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove', foreground = '#C00D1E').pack(fill=BOTH, expand=1)
            f.place(x= i*60, y=250)
          
    def neededVars (self):
        self.month_names = tuple(calendar.month_name)
        self.day_names = tuple(calendar.day_abbr)
        self.year = time.strftime("%Y")
        self.month = time.strftime("%B")
        self.day = time.strftime("%d")
        self.month_number = time.strftime("%m")
        self.cal= calendar.Calendar()
        self._year = datetime.date.today().year
        self._month = datetime.date.today().month
       
    
    def previousYear(self):
        current_year = int(self.year_str_var.get())-1
        self.year_str_var.set(current_year)
        self.make_calendar()
 
    def nextYear(self):
        current_year = int(self.year_str_var.get())+1
        self.year_str_var.set(current_year)

        self.make_calendar()
     
    def previousMonth(self):
        current_month = self._month
        previous_month = current_month -1
       
        if previous_month == 0:
            self.month_str_var.set(self.month_names[12])
        else:
            self.month_str_var.set(self.month_names[current_month - 1])
     
        self.make_calendar()
                     
    def nextMonth(self):
        current_month = self._month
        try:
            self.month_str_var.set(self.month_names[current_month + 1])
   
        except IndexError:
            self.month_str_var.set(self.month_names[1])
           
        self.make_calendar()
 
    def make_calendar(self):
        self._year = int(self.year_str_var.get())
        self._month = self.month_names.index(self.month_str_var.get())
        self.m_cal = calendar.monthcalendar(self._year, self._month)
        self.PintaDias()
       
    def start(self):
        self.mainloop()
 
if __name__ == '__main__':
    app = MiCalendario()
    app.start()
