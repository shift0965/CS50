class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add(self, name):
        if(len(self.passenger) <= self.capacity-1):
            self.passenger.append(name)
            print("{} is successfully added".format(name))
        else:
            print("sorry, the flight is fully booked")
