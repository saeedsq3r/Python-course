def disc_print():
    pass
def calculate_discount(price: float, rate: float)-> float:
    """ 
        Calculate the final price after applying the discount.
        Args:
            price (float): Original Product Price.
            rate (float): Discount Rate as number (e.g 20 for 20%).
        Returns:
            final_price (float): Final Price after applying the discount. 
    """
    final_price = price - (price * rate / 100)
    return (final_price)

def DiscPrint(p, r):
    print("calculating discount...")
    p = p - (p * r/100)
    print(p)

DiscPrint(80, 20)
help(calculate_discount)