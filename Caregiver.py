class Caregiver:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.hours_worked = 0
        self.availability = {}  # Day and shift availability

    def set_availability(self, day, shift, status):
        """Set the availability for a day and shift"""
        if day not in self.availability:
            self.availability[day] = {}
        self.availability[day][shift] = status

    def calculate_pay(self, hourly_rate=20):
        """Calculate pay based on hours worked"""
        return self.hours_worked * hourly_rate
