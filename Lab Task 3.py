class thermostat:
    def __init__(self, desired_temperature):
        self.current_temperature = 20  
        self.desired_temperature = desired_temperature

    def adjust_temperature(self):
        if self.current_temperature < self.desired_temperature:
            self.heater_on()
        elif self.current_temperature > self.desired_temperature:
            self.air_conditioner_on()
        else:
            self.maintain_temperature()

    def heater_on(self):
        print("Heater is ON. Increasing temperature.")
        self.current_temperature += 1 
        self.adjust_temperature()

    def air_conditioner_on(self):
        print("Air Conditioner is ON. Decreasing temperature.")
        self.current_temperature -= 1  
        self.adjust_temperature()

    def maintain_temperature(self):
        print("Temperature is stable at", self.current_temperature)


obj1 = thermostat(desired_temperature=22)
obj1.adjust_temperature()
