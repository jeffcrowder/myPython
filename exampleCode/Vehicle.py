from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """this is an abstract class

    Attributes:
        wheels: an integer that represents the # of wheels
        miles: the # of miles driven
        make: make of vehicle as a string
        model: model of vehicle as a string
        year: the integral year
        sold_on: the date the vehicle was sold
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for the vehicle as a float"""
        if self.sold_on is not None:
            return 0.0 # already solda
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to putchase the vehicle"""
        if self.sold_on is None:
            return 0.0 # not sold yet
        return self.base_sale_price - (0.10 * self.miles)

    @abstractmethod
    def vehicle_type():
        """Return a string representing the type of vehicle this is"""
        pass
