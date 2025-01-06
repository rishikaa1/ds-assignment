class VectorClock:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.clock = [0] * num_processes

    def increment(self):
        """ Increment the vector clock for this process. """
        self.clock[self.process_id] += 1

    def send_event(self):
        """ Simulate sending a message by incrementing the clock. """
        self.increment()
        return list(self.clock)

    def receive_event(self, received_clock):
        """ Update the vector clock on receiving a message. """
        self.clock = [max(self.clock[i], received_clock[i]) for i in range(len(self.clock))]
        self.increment()

    def __str__(self):
        return f"Process {self.process_id} Clock: {self.clock}"


# Example usage
if __name__ == "__main__":
    num_processes = 2
    process1 = VectorClock(0, num_processes)
    process2 = VectorClock(1, num_processes)

    print("Process 1 performs an event.")
    process1.increment()
    print(process1)

    print("\nProcess 1 sends a message to Process 2.")
    sent_clock = process1.send_event()
    print(f"Process 1 clock after sending: {process1}")

    print("\nProcess 2 receives the message from Process 1.")
    process2.receive_event(sent_clock)
    print(f"Process 2 clock after receiving: {process2}")
