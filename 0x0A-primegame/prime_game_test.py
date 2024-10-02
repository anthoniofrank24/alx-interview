#!/usr/bin/env python3

import time
isWinner = __import__('0-prime_game').isWinner

def test_isWinner():
    # Test case 1: Minimum Input Values
    assert isWinner(1, [1]) == 'Ben', "Failed on minimum input values test case"

    # Test case 2: Maximum n Value
    start_time = time.time()
    max_n = 10000
    result = isWinner(1, [max_n])
    end_time = time.time()
    assert result in ['Maria', 'Ben'], "Failed on maximum n value test case"
    assert end_time - start_time < 5, "Performance issue on maximum n value test case"

    # Test case 3: All Same n Values
    assert isWinner(3, [4, 4, 4]) == 'Ben', "Failed on all same n values test case"

    # Test case 4: Mix of Small and Large n Values
    assert isWinner(4, [2, 10, 20, 100]) is None, "Failed on mix of small and large n values test case"

    # Test case 5: No Prime Numbers
    assert isWinner(1, [1]) == 'Ben', "Failed on no prime numbers test case"

    # Test case 6: Large Number of Rounds
    rounds = [i for i in range(1, 1001)]  # 1000 rounds
    result = isWinner(1000, rounds)
    assert result in ['Maria', 'Ben'], "Failed on large number of rounds test case"

    print("All severe edge cases passed")

# Run the test cases
if __name__ == "__main__":
    test_isWinner()
