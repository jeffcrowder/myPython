from Vehicle import Vehicle as V

class Motorcycle(V):
    """A Motorcycle for sale"""

    base_sale_price = 5000
    wheels = 2

    def vehicle_type(self):
        """Return a string representing the type of vehicle this is"""
        return 'motorcycle'
