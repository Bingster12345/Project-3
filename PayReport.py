class PayReport:
    def __init__(self, caregivers):
        self.caregivers = caregivers

    def generate_report(self):
        """Generate a text report of weekly pay."""
        report = "Weekly Pay Report\n"
        report += "-" * 20 + "\n"
        total_pay = 0
        for caregiver in self.caregivers:
            pay = caregiver.calculate_pay()
            total_pay += pay
            # Using string concatenation
            report += caregiver.name + ": $" + str(round(pay, 2)) + "\n"
          
        report += "-" * 20 + "\n"
        report += "Total Weekly Pay: $" + str(round(total_pay, 2)) + "\n"
        return report
