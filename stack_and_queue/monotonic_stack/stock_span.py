### O(n^2)
# class StockSpanner:

#     def __init__(self):
#         self.stocklst = []
#         # self.stockSpan = []
#         self.stocklen = 0

#     def next(self, price: int) -> int:
#         val = None
#         if self.stocklen == 0 or self.stocklst[-1] > price:
#             # self.stockSpan.append(1)
#             val = 1
#         else:
#             stock_len = 1
#             i = self.stocklen-1
#             while i>= 0 and self.stocklst[i] <= price:
#                 stock_len += 1
#                 i -= 1
#             # self.stockSpan.append(stock_len)
#             val = stock_len


#         self.stocklst.append(price)
#         self.stocklen += 1

#         return val


class StockSpanner:

    def __init__(self):
        self.stocklst = []

    def next(self, price: int) -> int:
        val = 0

        if len(self.stocklst) == 0:
            val = 1
        else:
            i = 1
            stockStack = self.stocklst.copy()
            while len(stockStack) > 0 and stockStack[-1] <= price:
                stockStack.pop()
                i += 1
            val = i
        
        self.stocklst.append(price)

        return val

obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))


## O(n)
class StockSpanner:

    def __init__(self):
        self.stockSpan = []

    def next(self, price: int) -> int:
        val = 1
        while self.stockSpan and self.stockSpan[-1][0] <= price:
            val += self.stockSpan.pop()[1]
        self.stockSpan.append((price,val))
        return val
