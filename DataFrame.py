import random

class DataFrame(object):
    def __init__(self, type, created_time: float):
        """
        type: ACK / data
        created_time: The time the dataframe is created
        """

        self.type = type
        self.created_time = created_time
        self.process_time = 0
        self.departure_time = 0
        self.number_of_collision = 0
        # self.channel =

        if type == "ACK":
            self.size = 64
        elif type == "data":
            self.size = random.randint(1, 1544)

    def calculate_delay(self):
        return self.departure_time - self.created_time

