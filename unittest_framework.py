#!/usr/bin/env python

from program_with_bugs import *
import dbglib as dbg

def main():
    input_l = list()
    expected_l = list()

    # Test Case 1
    input_l.append([1])
    expected_l.append([])

    # Test Case 2
    input_l.append([1, 2])
    expected_l.append([2])

    # Test Case 3
    input_l.append([1, 2, 3])
    expected_l.append([2])

    # Test Case 4
    input_l.append([1, 2, 4, 3])
    expected_l.append([2, 4])

    # Test Case 5
    input_l.append([1, 3, 2, 4])
    expected_l.append([2, 4])


    test_case_num = len(input_l)
    dbg.print_info("Running %d test cases" % test_case_num)
    for tnum in range(test_case_num):
        res_l = removeOddNumbersV2(input_l[tnum])
        assert(res_l == expected_l[tnum])
    dbg.print_success("All tests passed!")


if __name__ == "__main__":
    main()