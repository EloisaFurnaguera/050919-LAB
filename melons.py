"""Classes for melon orders."""

class AbstracMelonOrder():
    def __init__(self, species, qty, tax, order_type, country_code = ""):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type
        self.country_code = country_code


    def get_total(self, base_price = 5.0):
        """Calculate price, including tax."""
        
        total = (1 + self.tax) * self.qty * base_price


        if self.species == "Chrismas Melons":
        	total = base_price * 1.5
        	

        if self.order_type	== "international"and self.qty < 10:
        	total = total + 3

        return total



    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstracMelonOrder):
    """A melon order within the USA."""

    # order_type = "domestic"

    def __init__(self, species, qty, tax):
        super().__init__(species, qty, tax, 'domestic', 'us')


class InternationalMelonOrder(AbstracMelonOrder):
    # order_type = "international"
    # self.country_code = country_code

    def __init__(self, species, qty, tax, country_code):
        super().__init__(species, qty, tax, 'international', country_code)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code




order1 = DomesticMelonOrder ("Chrismas Melons", 5, 0.12)
print(order1.species, order1.qty, order1.order_type, order1.get_total())

print()

order2 = InternationalMelonOrder ("Chrismas Melons", 5, 0.17, "UK")
print(order2.species, order2.qty, order2.order_type, 
	  order2.get_total(), order2.get_country_code())











    #"""An international (non-US) melon order."""

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.country_code = country_code
    #     self.shipped = False
    #     self.order_type = "international"
    #     self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code
