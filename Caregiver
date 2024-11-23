class Caregiver:
    def __init__(self, name, phone, email, pay_rate=20):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_worked = 0
        self.availability = {day: {'AM': 'available', 'PM': 'available'} for day in range(1, 32)}

    def set_availability(self, day, shift, status):
        if day in self.availability and shift in self.availability[day]:
            self.availability[day][shift] = status
        else:
            print("Invalid day or shift.")

    def calculate_weekly_pay(self):
        return self.hours_worked * self.pay_rate

    def __str__(self):
        return f"{self.name} ({self.phone}, {self.email})"
