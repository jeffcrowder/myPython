from Vehicle import Vehicle as V

class Truck(V):
    """A truck for sale"""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """Return a string representing the type of vehicle"""
        return 'truck'



