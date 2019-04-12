from tkinter import *
import calendar
import time
import datetime
from tkinter import ttk

cal= calendar.Calendar()
day_str_var = ""
year_str_var = ""
month_str_var =""

class Calendario(ttk.Frame):
    
    def __init__(self, parent, **args):
        self.__width = args['height'] if 'height' in args else 420
        self.__height = args['width'] if 'width' in args else 340

        ttk.Frame.__init__(self, parent, width=self.__width, height=self.__height)
        self.neededVars()
        self.year_str_var = StringVar()
        self.month_str_var = StringVar()
        self.day_str_var = StringVar()

        self.__Esqueleto__()
        self.__createDaysNames__()
        self.PintaDias()
    
    def __Esqueleto__(self):
        btn1 = ttk.Button(self, text =  '<<', width = 4, command= self.previousYear).place(x=60, y=10)
        btn2 = ttk.Button(self, text =  '<', width = 4, command = self.previousMonth).place(x=90, y=10)
        btn3 = ttk.Button(self, text= ">", width=4, command = self.nextMonth).place(x=300, y=10)
        btn4 = ttk.Button(self, text=">>", width=4, command= self.nextYear).place(x=330, y=10)
       
        self.month_str_var.set(self.month)
        self.selectedmonth = ttk.Label(self, textvariable = self.month_str_var, font=("Tahoma", 14, 'bold')).place(x=130, y=10)
       
        self.year_str_var.set(self.year)
        self.selectedyear = ttk.Label(self, textvariable = self.year_str_var, font=("Tahoma", 14, 'bold')).place(x=240, y=10)
        
        self.set_date()
    
    def neededVars(self):
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
        self.set_date()

    def nextYear(self):
        current_year = int(self.year_str_var.get())+1
        self.year_str_var.set(current_year)
        self.set_date()
     
    def previousMonth(self):
        
        current_month = self._month
        previous_month = current_month -1
        
        if previous_month == 0:
            self.month_str_var.set(self.month_names[12])
        else:
            self.month_str_var.set(self.month_names[current_month - 1])
        self.set_date()
                     
    def nextMonth(self):
        current_month = self._month
        try:
            self.month_str_var.set(self.month_names[current_month + 1])
    
        except IndexError:
            self.month_str_var.set(self.month_names[1])
    
        self.set_date()
    
    def __createDaysNames__(self):
        dias = self.day_names
        for i in range(7):
            f = ttk.Frame(self, width=60, height=22)
            f.pack_propagate(0)
            ttk.Label(f, text=dias[i], font=('Tahoma', 10, 'bold'), anchor=CENTER, borderwidth=0.5, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x=i*60, y=50)
           
  
    def count_left_zeros(self, my_days):
        left_zeros = 0
        for day in my_days:
            if day == 0:
                left_zeros += 1
            else:
                break
        return left_zeros

 
    def PintaDias(self):
        
        self.all_days = [day for day in cal.itermonthdays(int(self._year), int(self._month))]
         
        left_days_count = self.count_left_zeros(self.all_days)
#        right_days_count = self.count_left_zeros(list(reversed(self.all_days)))
 
        left_days = []
        if left_days_count > 0:
            year = int(self._year)
            previous_month = int(self._month) - 1
            if previous_month == 0:
                previous_month = 12
                year -= 1
            previous_month_days = [day for day in cal.itermonthdays(year, previous_month) if day]
            left_days = previous_month_days[-left_days_count:]
 
        right_days = []
        year = int(self._year)
        next_month = int(self._month) + 1
        if next_month == 13:
            next_month = 1
            year += 1
        next_month_days = [day for day in cal.itermonthdays(year, next_month) if day]
        right_days = next_month_days
        print(right_days)
        left_current = left_days+[day for day in self.all_days if day]
        count = len(left_current)
        self.all_days = left_days + [day for day in self.all_days if day] + right_days
        print(self.all_days)
        
 
        for week in range(6):
            for dayWeek in range(7):
                color = '#000000' if dayWeek < 5 else '#FF6157'
                index = dayWeek + week * 7
                if index < left_days_count or index > count-1:
                    color = '#C2C2C2'
                f = ttk.Frame(self, width=60, height= 45)
                f.pack_propagate(0)
                ttk.Label(f, text=self.all_days[dayWeek + week*7], foreground=color, font=('Tahoma', 10), anchor=CENTER, borderwidth=0, relief='groove').pack(fill=BOTH, expand=1)
                f.place(x= dayWeek*60, y=70 + 45 * week)
                

    def set_date(self):
        self._year = int(self.year_str_var.get())
        self._month = self.month_names.index(self.month_str_var.get())
        self.m_cal = calendar.monthcalendar(self._year, self._month)
        self.PintaDias()
        
class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Tkinter")
        self.geometry("420x340")
        self.resizable(0,0)

        self.calendar = Calendario(self)
        self.calendar.place(x=0, y=0)


    def start(self):
        self.mainloop()

if __name__ == '__main__':
    ap = MainApp()
    ap.start()
