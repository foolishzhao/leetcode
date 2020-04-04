class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.lastZero = -1

    def add(self, num: int) -> None:
        if num:
            self.products.append(num * self.products[-1])
        else:
            self.products.append(1)
            self.lastZero = len(self.products)

    def getProduct(self, k: int) -> int:
        if self.lastZero > len(self.products) - k:
            return 0

        return self.products[-1] // self.products[-(k + 1)]


if __name__ == '__main__':
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
    obj.add(8)
    print(obj.getProduct(2))
