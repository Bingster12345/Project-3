class Schedule:
  def __innit(self):
    self.schedule = {}

  def assign_shift(self, day, shift, caregiver):
    #Assign a caregiver to a shift
    if day not in self.schedule:
      self.schedule[day] = {'AM': None, 'PM': None}
    self.schedule[day][shift] = caregiver
    #Each shift is 6 hours, so add it
    caregiver.hours_worked += 6
