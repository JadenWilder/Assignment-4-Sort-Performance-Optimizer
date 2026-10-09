"""
Small Test Cases for Sorting Algorithms
Use these test cases to verify your sorting implementations work correctly.
Uncomment the test calls at the bottom as you implement each algorithm.
"""

from starter_code import bubble_sort, selection_sort, insertion_sort, merge_sort


# ============================================================================
# TEST CASES WITH KNOWN CORRECT OUTPUTS
# ============================================================================

# Test Case 1: Random unsorted array
test_random = [64, 34, 25, 12, 22, 11, 90]
expected_random = [11, 12, 22, 25, 34, 64, 90]

# Test Case 2: Already sorted array
test_sorted = [1, 2, 3, 4, 5]
expected_sorted = [1, 2, 3, 4, 5]

# Test Case 3: Reverse sorted array
test_reverse = [5, 4, 3, 2, 1]
expected_reverse = [1, 2, 3, 4, 5]

# Test Case 4: Array with duplicates
test_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
expected_duplicates = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Test Case 5: Single element array
test_single = [42]
expected_single = [42]

# Test Case 6: Empty array
test_empty = []
expected_empty = []

# Test Case 7: Two elements (swap needed)
test_two = [7, 3]
expected_two = [3, 7]

# Test Case 8: Negative numbers
test_negative = [-5, 3, -2, 8, -1, 0]
expected_negative = [-5, -2, -1, 0, 3, 8]


# ============================================================================
# TEST FUNCTIONS
# ============================================================================

def run_test(sort_func, func_name, test_input, expected_output, test_name):
    """Run a single test and print result."""
    result = sort_func(test_input.copy())
    passed = result == expected_output
    status = "PASS" if passed else "FAIL"
    print(f"  {test_name}: {status}")
    if not passed:
        print(f"    Input:    {test_input}")
        print(f"    Expected: {expected_output}")
        print(f"    Got:      {result}")
    return passed


def test_bubble_sort():
    """Test bubble sort implementation."""
    print("\n--- Testing Bubble Sort ---")
    all_passed = True
    all_passed &= run_test(bubble_sort, "bubble_sort", test_random, expected_random, "Random array")
    all_passed &= run_test(bubble_sort, "bubble_sort", test_sorted, expected_sorted, "Already sorted")
    all_passed &= run_test(bubble_sort, "bubble_sort", test_reverse, expected_reverse, "Reverse sorted")
    all_passed &= run_test(bubble_sort, "bubble_sort", test_duplicates, expected_duplicates, "With duplicates")
    all_passed &= run_test(bubble_sort, "bubble_sort", test_single, expected_single, "Single element")
    all_passed &= run_test(bubble_sort, "bubble_sort", test_empty, expected_empty, "Empty array")
    all_passed &= run_test(bubble_sort, "bubble_sort", test_two, expected_two, "Two elements")
    all_passed &= run_test(bubble_sort, "bubble_sort", test_negative, expected_negative, "Negative numbers")
    print(f"Bubble Sort: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    return all_passed


def test_selection_sort():
    """Test selection sort implementation."""
    print("\n--- Testing Selection Sort ---")
    all_passed = True
    all_passed &= run_test(selection_sort, "selection_sort", test_random, expected_random, "Random array")
    all_passed &= run_test(selection_sort, "selection_sort", test_sorted, expected_sorted, "Already sorted")
    all_passed &= run_test(selection_sort, "selection_sort", test_reverse, expected_reverse, "Reverse sorted")
    all_passed &= run_test(selection_sort, "selection_sort", test_duplicates, expected_duplicates, "With duplicates")
    all_passed &= run_test(selection_sort, "selection_sort", test_single, expected_single, "Single element")
    all_passed &= run_test(selection_sort, "selection_sort", test_empty, expected_empty, "Empty array")
    all_passed &= run_test(selection_sort, "selection_sort", test_two, expected_two, "Two elements")
    all_passed &= run_test(selection_sort, "selection_sort", test_negative, expected_negative, "Negative numbers")
    print(f"Selection Sort: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    return all_passed


def test_insertion_sort():
    """Test insertion sort implementation."""
    print("\n--- Testing Insertion Sort ---")
    all_passed = True
    all_passed &= run_test(insertion_sort, "insertion_sort", test_random, expected_random, "Random array")
    all_passed &= run_test(insertion_sort, "insertion_sort", test_sorted, expected_sorted, "Already sorted")
    all_passed &= run_test(insertion_sort, "insertion_sort", test_reverse, expected_reverse, "Reverse sorted")
    all_passed &= run_test(insertion_sort, "insertion_sort", test_duplicates, expected_duplicates, "With duplicates")
    all_passed &= run_test(insertion_sort, "insertion_sort", test_single, expected_single, "Single element")
    all_passed &= run_test(insertion_sort, "insertion_sort", test_empty, expected_empty, "Empty array")
    all_passed &= run_test(insertion_sort, "insertion_sort", test_two, expected_two, "Two elements")
    all_passed &= run_test(insertion_sort, "insertion_sort", test_negative, expected_negative, "Negative numbers")
    print(f"Insertion Sort: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    return all_passed


def test_merge_sort():
    """Test merge sort implementation."""
    print("\n--- Testing Merge Sort ---")
    all_passed = True
    all_passed &= run_test(merge_sort, "merge_sort", test_random, expected_random, "Random array")
    all_passed &= run_test(merge_sort, "merge_sort", test_sorted, expected_sorted, "Already sorted")
    all_passed &= run_test(merge_sort, "merge_sort", test_reverse, expected_reverse, "Reverse sorted")
    all_passed &= run_test(merge_sort, "merge_sort", test_duplicates, expected_duplicates, "With duplicates")
    all_passed &= run_test(merge_sort, "merge_sort", test_single, expected_single, "Single element")
    all_passed &= run_test(merge_sort, "merge_sort", test_empty, expected_empty, "Empty array")
    all_passed &= run_test(merge_sort, "merge_sort", test_two, expected_two, "Two elements")
    all_passed &= run_test(merge_sort, "merge_sort", test_negative, expected_negative, "Negative numbers")
    print(f"Merge Sort: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    return all_passed


def test_all():
    """Run all sorting algorithm tests."""
    print("=" * 50)
    print("SMALL TEST CASES - SORTING ALGORITHM VERIFICATION")
    print("=" * 50)

    results = {
        "Bubble Sort": test_bubble_sort(),
        "Selection Sort": test_selection_sort(),
        "Insertion Sort": test_insertion_sort(),
        "Merge Sort": test_merge_sort()
    }

    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    for algo, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        print(f"  {algo}: {status}")

    all_passed = all(results.values())
    print(f"\nOverall: {'ALL ALGORITHMS WORKING' if all_passed else 'SOME ALGORITHMS NEED WORK'}")
    return all_passed


# ============================================================================
# MAIN - Uncomment tests as you implement each algorithm
# ============================================================================

if __name__ == "__main__":
    # Uncomment these one at a time as you implement each algorithm:

    # test_bubble_sort()
    # test_selection_sort()
    # test_insertion_sort()
    # test_merge_sort()

    # Or run all tests at once:
    # test_all()

    print("Uncomment the test functions above to verify your implementations!")
