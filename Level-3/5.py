class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + (total_minutes // 60)
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        print("{} hr and {} min".format(self.hours,self.minutes))

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print("Total minutes: {}".format(total_minutes))
time1 = Time(2, 50)
time2 = Time(1, 20)

added_time = time1.addTime(time2)  
added_time.displayTime()           
added_time.displayMinute()