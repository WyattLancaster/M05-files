# m05 - Programming Assignment - Testing
# author: WJL
# created: 2022-02-19
# program defines 'test_sum' that asserts the sum of 1, 2, and 3 == 6 or "Should be six" if false

# define test_sum
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

# test if everything passed properly and print if it did
if __name__ == "__main__":
    test_sum()
    print("Everything passed")