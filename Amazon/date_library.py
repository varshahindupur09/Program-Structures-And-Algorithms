from calendar import monthcalendar

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def getDateInDefaultFormat(self):
        return f"{self.month}/{self.day}/{self.year}"

    def get_days_in_month(self):
        days_in_month_list = [day for day in monthcalendar(self.year, self.month)] # if day[0] != 0]
        # print("days_in_month ", days_in_month_list)
        # days_in_month  [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 0, 0, 0]]
        days_in_month = days_in_month_list[-1]
        # print(days_in_month) o/p: [26, 27, 28, 29, 0, 0, 0]
        for days in days_in_month:
            if days != 0:
                total_days = days  
        return total_days
    
    def validateDate(self):
        if self.month < 1 or self.month > 12:
            print("month ", self.month)
            return False

        days_in_month = self.get_days_in_month()
        
        if self.day < 1 or self.day > days_in_month:
            print("day ", self.day)
            return False
        return True

    def add_days(self, days: int):
        while days > 0:
            days_in_current_month = self.get_days_in_month()
            if (self.day + days) <= days_in_current_month:
                self.day += days
                break
            else:
                days -= (days_in_current_month - self.day + 1)
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.month = 1
                    self.year += 1
        return self.getDateInDefaultFormat()

    def substract_days(self, days: int):
        while days > 0:
            if self.day > days:
                # print("if ", self.day, days)
                self.day -= days
                break
            else:
                # print("else ",  days, self.day, self.month, self.year)
                days -= self.day
                self.month -= 1
                if self.month < 1:
                    self.month = 12
                    self.year -= 1
                self.day = self.get_days_in_month()
        return self.getDateInDefaultFormat()
                
        

dayInput = 1
monthInput = 2
yearInput = 2024
dateInstance = Date(dayInput, monthInput, yearInput)
# print(dateInstance.getDateInDefaultFormat())
print(dateInstance.validateDate())
days_added = 25
print(dateInstance.add_days(days_added)) #2/26/2024
days_substract = 90
dateInstance = Date(dayInput, monthInput, yearInput)
print(dateInstance.substract_days(days_substract)) #11/3/2023
