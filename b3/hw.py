# Thực hành: OOP

# Bạn đang thiết kế chương trình quản lý đơn đặt hàng.
# Biết chương trình có các đối tượng sau:

# Item	Order	Promo
# Số lượng: quantity	Giỏ hàng: item_list	Giá trị đơn hàng: price
# Đơn giá: price	Mã người mua: customer_id	Hành động giảm giá: discount()
# 	Hành động tính tổng giá trị đơn: total()	

# Biết rằng ngoại trừ phương pháp giảm giá thông thường là Promotion, còn 02 chương trình giảm giá:

# Cho đơn đặt hàng lớn BulkOrderPromo

# Cho khách hàng thân thiết LoyaltyPromo


# ---------- Item ----------
class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    # tong gia tri cua 1 item
    def total_price(self):
        return self.quantity * self.price


# ---------- Order ----------
class Order:
    def __init__(self, customer_id, item_list, promo=None):
        self.customer_id = customer_id
        self.item_list = item_list
        self.promo = promo

    def total(self):
        return sum(item.total_price() for item in self.item_list)

    def final_price(self):
        if self.promo:
            return self.total() - self.promo.discount(self)
        return self.total()


# ---------- Promo ----------
class Promo:
    def discount(self, order):
        """Default: no discount"""
        return 0


# ---------- Bulk Order Promo ----------
class BulkOrderPromo(Promo):
    def discount(self, order):
        if order.total() >= 1000000:
            return order.total() * 0.1
        return 0


# ---------- Loyalty Promo ----------
class LoyaltyPromo(Promo):
    def discount(self, order):
        if order.customer_id < 1000:
            return order.total() * 0.05
        return 0


# ---------- Demo ----------
if __name__ == "__main__":
    items = [Item(2, 300000), Item(1, 500000)]  # Tổng = 1.1 triệu

    order1 = Order(customer_id=500, item_list=items, promo=BulkOrderPromo())
    order2 = Order(customer_id=400, item_list=items, promo=LoyaltyPromo())

    print("Tổng tiền:", order1.total())
    print("Giảm giá BulkOrder:", order1.promo.discount(order1))
    print("Phải trả:", order1.final_price())

    print("Tổng tiền:", order2.total())
    print("Giảm giá Loyalty:", order2.promo.discount(order2))
    print("Phải trả:", order2.final_price())
