from Vehicle import Vehicle as V

class Car(V):
    """A car for sale"""

    base_sale_price = 8800
    wheels = 4

    def vehicle_type(self):
        """Return a string representing the type fo vehicle"""
        return 'car'


