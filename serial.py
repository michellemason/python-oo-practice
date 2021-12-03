"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """initialize self with a default start at 0 & to be the next number"""
        self.start = self.next = start

    def __repr__(self):
        return f"Start is: {self.start} Next is: {self.next}"

    def generate(self):
        """generate the next number in sequence"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """reset serial to the original start number"""
        self.next = self.start
        return self.start


