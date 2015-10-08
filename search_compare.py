#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 Algorithms 1 of 2 weeks, Search + Sort"""
import time
import random


def sequential_search(a_list, item):
    """
    Args:
        start (float) : Time of start.
        end (float) : Time of end.
        found (bool) : Default False
        a_list (list) : List to operate on.
        item (int) : Number to find in list.

    Returns:
        found (bool) : True if item found.
        end-start (float): Process time.

    Examples:
        >>> sequential_search([1,2,3,4], 1)
        >>> (True, 1.9073486328125e-06)
    """
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    return found, end-start


def ordered_sequential_search(a_list, item):
    """
    Args:
        start (float) : Time of start.
        end (float) : Time of end.
        a_list (list) : List to operate on.
        item (int) : Number to find on list.
        stop (bool) : Default False.
        found (bool) : Default False.

    Returns:
        found (bool) : True if item found.
        end-start (float): Process time.

    Examples:
        >>> ordered_sequential_search([1,3,4,5,6,7], 2)
        >>> (False, 4.0531158447265625e-06)
    """
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    end = time.time()
    return found, end-start


def binary_search_iterative(a_list, item):
    """
    Args:
         start (float) : Time of start.
         end (float) : Time of end.
         first (int) : Indexed interger.
         last (int) : Indexed interger.
         found (bool) : Default False

    Returns:
        found (bool) : True if item found.
        end-start (float) : Process time.

    Examples:
        >>> binary_search_iterative([2,3,4,5,6,7,1], 1)
        >>> (True, 5.9604644775390625e-06)
    """
    start = time.time()
    a_list.sort()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end-start


def binary_search_recursive(a_list, item):
    """
    Args:
        start (float) : Time of start.
        end (float) : Time of end.
        a_list (list): List to process.
        item (int): Interger to find on list.
        found (bool): Default 0.

    Returns:
        found (bool): True if item found.
        end-start (float): Process time.

    Examples:
        >>> binary_search_recursive([1,2,3,6,7,8,0], 0)
        >>> (True, 2.86102294921875e-06)
    """
    start = time.time()
    a_list.sort()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_iterative(a_list[:midpoint], item)
            else:
                return binary_search_iterative(a_list[midpoint + 1:], item)

    end = time.time()
    return found, end-start


def random_gen(value):
    """
    Args:
        random_list (list) : Values generated by random range of value.

    Returns:
        random_list (list) : Creates list of random values fast.

    Examples:
        >>> random_gen(15)
            [11, 2, 4, 3, 12, 1, 13, 14, 10, 5, 0, 6, 9, 7, 8]
    """
    random_list = random.sample(range(0, value), value)
    return random_list


def main():
    """
    Args:
        tests (dict) : Dictionary of tests to run.
        random_list (list) : List of random numbers.
        max (int) : Max count of iterations to process.
        output (dict) : Saved results of time outputs.

    Returns:
        None

    Examples:
        >>> main()
        >>> List of 500 length the test timed:
            Sequential took  0.0087013 seconds to run on average
            Ordered Seq took  0.0000653 seconds to run on average
            Binary Iter took  0.0013690 seconds to run on average
            Binary Recur took  0.0006678 seconds to run on average


            List of 10000 length the test timed:
            Sequential took  0.1583154 seconds to run on average
            Ordered Seq took  0.0000701 seconds to run on average
            Binary Iter took  0.0229557 seconds to run on average
            Binary Recur took  0.0089798 seconds to run on average


            List of 1000 length the test timed:
            Sequential took  0.0161924 seconds to run on average
            Ordered Seq took  0.0000634 seconds to run on average
            Binary Iter took  0.0022426 seconds to run on average
            Binary Recur took  0.0011785 seconds to run on average
        >>>
    """
    tests = {'test1': 500,
             'test2': 1000,
             'test3': 10000}

    for test in tests.values():
        random_list = random_gen(test)
        iter_count = 100
        output = {'seq':0,
                  'ord_seq':0,
                  'bin_iter':0,
                  'bin_recur':0}
        while iter_count > 0:
            output['seq'] += sequential_search(random_list, -1)[1]
            output['ord_seq'] += ordered_sequential_search(random_list, -1)[1]
            output['bin_iter'] += binary_search_iterative(random_list, -1)[1]
            output['bin_recur'] += binary_search_recursive(random_list, -1)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % test
        print "Sequential took %10.7f seconds to run on average" % (float(output['seq']/ 100))
        print "Ordered Seq took %10.7f seconds to run on average" % (float(output['ord_seq'] / 100))
        print "Binary Iter took %10.7f seconds to run on average" % (float(output['bin_iter']/ 100))
        print "Binary Recur took %10.7f seconds to run on average" % \
        (float(output['bin_recur']/ 100))
        print '\n'


if __name__ == '__main__':
    main()
