from Post import Post


class SalePost(Post):
    def __init__(self, user, item: str, price: int, region: str):
        super().__init__(user)
        self._item = item
        self._price = price
        self._region = region
        self._available = True

    def __str__(self):
        status = "For sale" if self._available else "Sold"
        return f"{self._user.get_name()} posted a product for sale:\n{status}! {self._item}, price: {self._price}, pickup from: {self._region}\n"

        # return (f"{self._user.get_name()} posted a product for sale:\n"
        #         f"{"For sale" if self._available else "Sold"}! {self._item}, price: "
        #         f"{self._price}, pickup from: {self._region}\n")

    def sold(self, password: str):
        if self._user.check_password(password):
            self._available = False
            print(f"{self._user.get_name()}'s product is sold")
            return True
        return False

    def discount(self, percent, password):
        if self._user.check_password(password):
            if self._available:
                self._price -= self._price * (percent / 100)
                print(f"Discount on {self._user.get_name()} product! the new price is: {self._price}")
                return True
        return False
