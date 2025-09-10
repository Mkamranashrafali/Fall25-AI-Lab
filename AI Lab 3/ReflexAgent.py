class ReflexAgent:
    def __init__(self, temp):
        self.temp = temp
        self.action = None 

    def perceive(self, temperature):
        if temperature >= self.temp:
            if self.action != "Turn ON AC":
                self.action = "Turn ON AC"
                return self.action
            else:
                return "AC is already ON"
        else:
            if self.action != "Turn OFF AC":
                self.action = "Turn OFF AC"
                return self.action
            else:
                return "AC is already OFF"


rooms = {
    "Hamza Room": 21,
    "Parents Room": 21, 
    "Drawing Room": 21,
    "Gaming Room": 26,
    "Brother's Room": 24
}

ai_model = ReflexAgent(22)
for key, value in rooms.items():
    action = ai_model.perceive(value)
    print(f"{key} temperature is {value}°C => {action}")
