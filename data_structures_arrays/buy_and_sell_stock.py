A = [550, 640, 530, 690, 350, 770, 500, 450, 700, 800, 820]


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell(A):
    max_profit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


print(buy_and_sell(A))


# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_stock(A):
    # Check if the prices array is less than 2
    if len(A) < 2:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A:
       	min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit


print(buy_and_sell_stock(A))
