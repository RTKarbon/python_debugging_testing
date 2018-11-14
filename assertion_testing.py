#!/usr/bin/env python

from program_with_bugs import *

def main():
    input_l = list()
    expected_l = list()

    # Test Case 1
    input_l.append([1])
    expected_l.append([])

    # Test Case 2
    input_l.append([])
    expected_l.append([])

    # Test Case 3
    input_l.append([2])
    expected_l.append([2])

    # Test Case 4
    input_l.append([1, 2, 3])
    expected_l.append([2])

    # Test Case 5
    input_l.append([1, 2, 3, 5])
    expected_l.append([2])

    # Test Case 5
    input_l.append([1, 3, 5])
    expected_l.append([])


    test_case_num = len(input_l)
    print "Running %d test cases" % test_case_num
    for tnum in range(test_case_num):
        res_l = removeOddNumbersV2(input_l[tnum])
        assert(res_l == expected_l[tnum])
    print "All tests passed!"


if __name__ == "__main__":
    main()