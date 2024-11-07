class CarBSTnode:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None

    def insert(self, price):
        if price < self.price:
            if self.left is None:
                self.left = CarBSTnode(price)
            else:
                self.left.insert(price)
        elif price > self.price:
            if self.right is None:
                self.right = CarBSTnode(price)
            else:
                self.right.insert(price)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.price)
        if self.right is not None:
            self.right.inorder()

    def remove(self, price):
        if price < self.price:
            if self.left is not None:
                self.left = self.left.remove(price)
        elif price > self.price:
            if self.right is not None:
                self.right = self.right.remove(price)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.price = self.right.min()
                self.right = self.right.remove(self.price)
        return self

    def min(self):
        if self.left is None:
            return self.price
        else:
            return self.left.min()

    def buyCar(self, budjet): # finds the most expensive car that the customer can afford
        print("budjet:", budjet, "price:", self.price)
        if self.price == budjet:
            return self.price
        elif self.price < budjet:
            if self.right is not None:
                if self.right.price <= budjet:
                    return self.right.buyCar(budjet)
            else:
                return self.price
        else:
            if self.left is not None:
                return self.left.buyCar(budjet)
            else:
                return False


class CarBST:
    def __init__(self):
        self.root = None

    def insert(self, price):
        if self.root is None:
            self.root = CarBSTnode(price)
        else:
            self.root.insert(price)

    def buyCar(self, price):
        if self.root is None:
            return False
        else:
            if self.root.buyCar(price):
                self.root = self.root.remove(self.root.buyCar(price))
                return True
            else:
                return False

    
    def inorder(self):
        print("Inorder:")
        self.root.inorder()
    
def sales(cars, customers):
    bst = CarBST()
    numberOfSales = 0
    for car in cars:
        bst.insert(car)
    for customer in customers:
        if bst.buyCar(customer):
            numberOfSales += 1
            print("Customer bought a car")
            bst.inorder()
        else:
            continue
    return numberOfSales

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))
    print()
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))
    print()
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))
    print()
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))
