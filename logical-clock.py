class LamportClock:
    def __init__(self):
        self.time = 0

    def increment(self):
        """ Increment the logical clock. """
        self.time += 1

    def send_event(self):
        """ Simulate sending a message by incrementing the clock. """
        self.increment()
        return self.time

    def receive_event(self, received_time):
        """ Update the clock when receiving a message. """
        self.time = max(self.time, received_time) + 1

    def __str__(self):
        return f"Logical Clock: {self.time}"


# Example usage
if __name__ == "__main__":
    process1 = LamportClock()
    process2 = LamportClock()

    print("Process 1 performs an event.")
    process1.increment()
    print(process1)

    print("\nProcess 1 sends a message to Process 2.")
    sent_time = process1.send_event()
    print(f"Process 1 clock after sending: {process1}")

    print("\nProcess 2 receives the message from Process 1.")
    process2.receive_event(sent_time)
    print(f"Process 2 clock after receiving : {process2}")
