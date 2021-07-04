from typing import List
import collections
import bisect
import heapq


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movieDict = collections.defaultdict(list)
        self.priceDict = collections.defaultdict(int)
        for shop, movie, price in entries:
            bisect.insort(self.movieDict[movie], (price, shop))
            self.priceDict[(movie, shop)] = price

        self.rented = set()
        self.rentedPQ = list()

    def search(self, movie: int) -> List[int]:
        res = list()
        for _, shop in self.movieDict[movie]:
            if (movie, shop) not in self.rented:
                res.append(shop)
                if len(res) == 5:
                    break
        return res

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((movie, shop))

        price = self.priceDict[(movie, shop)]
        heapq.heappush(self.rentedPQ, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.remove((movie, shop))

    def report(self) -> List[List[int]]:
        res = list()
        while len(res) < 5 and self.rentedPQ:
            price, shop, movie = heapq.heappop(self.rentedPQ)
            if (movie, shop) in self.rented and (price, shop, movie) not in res:
                res.append((price, shop, movie))

        for price, shop, movie in res:
            heapq.heappush(self.rentedPQ, (price, shop, movie))

        return [(shop, movie) for price, shop, movie in res]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
