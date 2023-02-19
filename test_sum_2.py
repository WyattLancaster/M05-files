# m05 - Programming Assignment - Testing
# author: WJL
# created: 2022-02-19
# program defines 'test_sum' that asserts the sum of the dictionary 1, 2, and 3 == 6 or "Should be six" if false then does the same thing only in tuple form

# define test_sum
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

# define test_sum_tuple
def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

# test if everything passed properly and print if it did
if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")