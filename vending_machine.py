from byotest import *

# Specification:
#  Given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer.
#  Our function should pay the minimum number of coins possible, and the available coin denominations are 100, 50, 20, 10, 5, 2, and 1.

usd_coins = [100, 50, 25, 10, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]


def get_change(amount, coins=eur_coins):
    change = []

    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)

    return change


# test for no change
test_are_equal(get_change(0), [])

# test for change equal to coin denominator
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])

test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])

test_are_equal(get_change(35, usd_coins), [25, 10])
test_are_equal(get_change(35), [20, 10, 5])
test_not_equal(get_change(35, usd_coins), [20, 10, 5])


print("All test pass!")
