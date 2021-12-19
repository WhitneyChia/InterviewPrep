# """
# ## Start typing here
#
# # order id, direction, number of shares, price
# # handle("100,buy,20,15") -> null;   // no trade
# # handle("101,buy,20,11") -> null;   // no trade
# # handle("102,sell,30,9") -> ["102,100,20,15", "102,101,10,11"]
#
#
# """
#
# import heapq
#
#
# class ProcessTrades:
#     """
#     1. Nothing can happen, heap just updates
#         return None
#     2. When prices cross, update self.bids and self.offers
#         return list of what you've executed
#     """
#
#     def __init__(self):
#         self.bids = heapq.heapify([])  # max_heap
#         self.offers = heapq.heapify([])  # min_heap
#
#     def handle(self, order_id, direction, num_shares, price):
#         if direction == "buy":
#             order = [-price, [order_id, num_shares]]
#             heapq.heappush(self.bids, order)
#             result = self.__order_matching()
#         else:
#             order = [price, [order_id, num_shares]]
#             heapq.heappush(self.offers, order)
#             result = self.__order_matching()
#         return result
#
#     def __order_matching(self):
#         result = []
#
#         while True:
#
#             if not self.offers and self.bids:
#                 return result
#             # See if anything crosses, if not, return None
#             min_offers = heapq.heappop(self.offers)
#             max_bids = heapq.heappop(self.bids)
#
#             min_offer_price = min_offers[0]
#             max_bid_price = -max_bids[0]
#             min_offer_shares = min_offers[1][1]
#             max_bid_shares = max_bids[1][1]
#
#             transact_price = max_bid_price
#             shares_can_transact = min(min_offer_shares, max_bid_shares)
#
#             if min_offer_price <= max_bid_price:
#                 if shares_can_transact == min_offer_shares:
#                     max_bids[1][1] = max_bid_shares - min_offer_shares
#                     result.append([min_offers[1][0], max_bids[1][0], shares_can_transact, transact_price])
#                     heapq.heappush(self.bids, max_bids)
#
#                 elif shares_can_transact == max_bid_shares:
#                     min_offers[1][1] = min_offer_shares - max_bid_shares
#                     result.append([min_offers[1][0], max_bids[1][0], shares_can_transact, transact_price])
#                     heapq.heappush(self.offers, min_offers)
#             else:
#                 heapq.heappush(self.bids, max_bids)
#                 heapq.heappush(self.offers, min_offers)
#                 return result
#
#         return result
#
#
# if __name__ == "__main__":
#     """
#      handle("100,buy,20,15") -> null;   // no trade
#     # handle("101,buy,20,11") -> null;   // no trade
#     # handle("102,sell,30,9")
#     """
#
#     trade_processor = ProcessTrades()
#     print(trade_processor.handle(100, "buy", 20, 15))
#     print(trade_processor.handle(101, "buy", 20, 11))
#     trade_processor.handle(102, "sell", 30, 9)