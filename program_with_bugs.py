#!/usr/bin/env python


def removeOddNumbersV1(l):
    for i in range(len(l)):
        # Step 1: use print statement to debug
        # print "index: %d, list: %s" % (i, str(l))
        if l[i] % 2 != 0:
            # print "removing element %d" % l[i]
            del l[i]
    return l

def removeOddNumbersV2(l):
    for n in l:
        if n % 2 != 0:
            l.remove(n)
    return l
 
def removeOddNumbersV3(l):
    return [v for v in l if v % 2 == 0]

def main():
    numbers_l = [1, 2, 3, 4, 5, 6]
    print "Original list: %s" % str(numbers_l)
    # even_l = removeOddNumbersV1(numbers_l)
    even_l = removeOddNumbersV2(numbers_l)
    # removeOddNumbersV2(numbers_l)
    print "List with only even numbers: %s" % str(even_l)

    # Add-hoc test
    # even_l = removeOddNumbersV3(numbers_l)




if __name__ == "__main__":
    main()