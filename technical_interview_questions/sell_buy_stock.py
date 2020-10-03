A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


# def bu_sell_stock(A):

#     max_profit = 0

#     for i in range(len(A) - 1):
#         for j in range(i+1 , len(A)):
#             if A[j] - A[i] > max_profit:
#                 max_profit = A[j] - A[i]
#     return max_profit

# print(bu_sell_stock(A))


def optimum_stock(A):
    max_profit = 0
    min_price = A[0]
    for price in A:
        min_price = min(min_price, price)

        compare_profit = price - min_price

        max_profit = max(max_profit, compare_profit)

    return max_profit


print(optimum_stock(A))