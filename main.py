from caregivers import Caregiver
from schedule import Schedule
from pay_report import PayReport

# Create caregivers
caregivers = [
    Caregiver("Alice", "555-1234", "alice@example.com"),
    Caregiver("Bob", "555-5678", "bob@example.com"),
]

# Set availability
caregivers[0].set_availability(1, 'AM', 'preferred')
caregivers[1].set_availability(1, 'PM', 'preferred')

# Create a schedule
schedule = Schedule(2024, 11)
schedule.assign_shift(1, 'AM', caregivers[0])
schedule.assign_shift(1, 'PM', caregivers[1])

# Generate pay report
pay_report = PayReport(caregivers)
print(pay_report.generate_report())
