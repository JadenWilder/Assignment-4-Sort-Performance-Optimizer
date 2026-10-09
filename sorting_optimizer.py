
"""
Assignment 4: Sort Performance Optimizer

Implements four sorting algorithms, tests correctness and stability,
and benchmarks their performance on generated datasets.
"""

import json
import time
import tracemalloc
from pathlib import Path


# ============================================================================
# PART 1: SORTING IMPLEMENTATIONS
# ============================================================================

def bubble_sort(arr):
    """Sort a list using Bubble Sort."""
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def selection_sort(arr):
    """Sort a list using Selection Sort."""
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(arr):
    """Sort a list using Insertion Sort."""
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    """Sort a list using Merge Sort."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Choose the left item first when values are equal.
        # This preserves the original order of equal elements.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}


# ============================================================================
# PART 2: FILE LOADING AND CORRECTNESS TESTING
# ============================================================================

def load_json_file(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def test_sorting_correctness():
    """Test all four sorting algorithms against the provided test cases."""
    test_file = Path("datasets/test_cases.json")

    if not test_file.exists():
        print(f"ERROR: Could not find {test_file}.")
        print("Make sure you run this program from the project directory.")
        return False

    try:
        test_data = load_json_file(test_file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: Could not read the test cases: {error}")
        return False

    test_cases = {}
    expected_data = {}

    if isinstance(test_data, dict):
        # The assignment may store expected results separately.
        expected_data = test_data.get("expected_sorted", {})

        for case_name, case_value in test_data.items():
            if case_name == "expected_sorted":
                continue

            if isinstance(case_value, list):
                test_cases[case_name] = case_value

            elif isinstance(case_value, dict):
                # Support test cases with an input and expected result.
                input_values = None

                for key in ("input", "array", "data", "values", "numbers"):
                    if isinstance(case_value.get(key), list):
                        input_values = case_value[key]
                        break

                if input_values is not None:
                    test_cases[case_name] = input_values

                    for expected_key in (
                        "expected_sorted", "expected", "output"
                    ):
                        if isinstance(case_value.get(expected_key), list):
                            expected_data[case_name] = case_value[
                                expected_key
                            ]
                            break

    elif isinstance(test_data, list):
        for index, case_value in enumerate(test_data):
            case_name = f"Test case {index + 1}"

            if isinstance(case_value, list):
                test_cases[case_name] = case_value

            elif isinstance(case_value, dict):
                input_values = None

                for key in ("input", "array", "data", "values", "numbers"):
                    if isinstance(case_value.get(key), list):
                        input_values = case_value[key]
                        break

                if input_values is not None:
                    test_cases[case_name] = input_values

                    for expected_key in (
                        "expected_sorted", "expected", "output"
                    ):
                        if isinstance(case_value.get(expected_key), list):
                            expected_data[case_name] = case_value[
                                expected_key
                            ]
                            break

    if not test_cases:
        print("ERROR: No valid input test cases were found.")
        print("Check the structure of datasets/test_cases.json.")
        return False

    passed = 0
    failed = 0

    print("\n" + "=" * 70)
    print("SORTING CORRECTNESS TESTS")
    print("=" * 70)

    for case_name, input_values in test_cases.items():
        if (
            isinstance(expected_data, dict)
            and case_name in expected_data
            and isinstance(expected_data[case_name], list)
        ):
            expected = expected_data[case_name]
        else:
            expected = sorted(input_values)

        for algorithm_name, algorithm in ALGORITHMS.items():
            try:
                actual = algorithm(input_values)
                success = actual == expected
            except Exception as error:
                success = False
                print(
                    f"FAIL: {case_name} - {algorithm_name}: {error}"
                )

            if success:
                passed += 1
                print(f"PASS: {case_name} - {algorithm_name}")
            else:
                failed += 1
                if "error" not in locals() or success:
                    print(f"FAIL: {case_name} - {algorithm_name}")

    # Additional edge cases make sure the algorithms handle common inputs.
    edge_cases = {
        "single_element": [7],
        "empty_list": [],
        "two_elements": [9, 2],
        "negative_numbers": [-5, 0, -2, 8, -10],
    }

    for case_name, input_values in edge_cases.items():
        expected = sorted(input_values)

        for algorithm_name, algorithm in ALGORITHMS.items():
            try:
                actual = algorithm(input_values)
                success = actual == expected
            except Exception as error:
                success = False
                print(
                    f"FAIL: {case_name} - {algorithm_name}: {error}"
                )

            if success:
                passed += 1
                print(f"PASS: {case_name} - {algorithm_name}")
            else:
                failed += 1
                if "error" not in locals() or success:
                    print(f"FAIL: {case_name} - {algorithm_name}")

    print("-" * 70)
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")

    if failed == 0:
        print("All sorting correctness tests passed!")
    else:
        print("Some sorting correctness tests failed.")

    return failed == 0


# ============================================================================
# PART 3: STABILITY DEMONSTRATION
# ============================================================================

def demonstrate_stability():
    """
    Check whether equal-price records keep their original relative order.
    """

    products = [
        {"name": "Widget A", "price": 1999, "original_position": 0},
        {"name": "Gadget B", "price": 999, "original_position": 1},
        {"name": "Widget C", "price": 1999, "original_position": 2},
        {"name": "Tool D", "price": 999, "original_position": 3},
        {"name": "Widget E", "price": 1999, "original_position": 4},
    ]

    def bubble_records(items):
        items = [item.copy() for item in items]

        for i in range(len(items)):
            swapped = False

            for j in range(len(items) - i - 1):
                if items[j]["price"] > items[j + 1]["price"]:
                    items[j], items[j + 1] = items[j + 1], items[j]
                    swapped = True

            if not swapped:
                break

        return items

    def selection_records(items):
        items = [item.copy() for item in items]

        for i in range(len(items)):
            min_index = i

            for j in range(i + 1, len(items)):
                if items[j]["price"] < items[min_index]["price"]:
                    min_index = j

            if min_index != i:
                items[i], items[min_index] = items[min_index], items[i]

        return items

    def insertion_records(items):
        items = [item.copy() for item in items]

        for i in range(1, len(items)):
            key = items[i]
            j = i - 1

            while j >= 0 and items[j]["price"] > key["price"]:
                items[j + 1] = items[j]
                j -= 1

            items[j + 1] = key

        return items

    def merge_records(items):
        if len(items) <= 1:
            return [item.copy() for item in items]

        mid = len(items) // 2
        left = merge_records(items[:mid])
        right = merge_records(items[mid:])

        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i]["price"] <= right[j]["price"]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    record_algorithms = {
        "Bubble Sort": bubble_records,
        "Selection Sort": selection_records,
        "Insertion Sort": insertion_records,
        "Merge Sort": merge_records,
    }

    results = {}

    print("\n" + "=" * 70)
    print("SORTING STABILITY DEMONSTRATION")
    print("=" * 70)

    for name, algorithm in record_algorithms.items():
        sorted_products = algorithm(products)

        stable = True

        for i in range(1, len(sorted_products)):
            previous = sorted_products[i - 1]
            current = sorted_products[i]

            if (
                previous["price"] == current["price"]
                and previous["original_position"]
                > current["original_position"]
            ):
                stable = False
                break

        results[name] = stable
        status = "STABLE" if stable else "UNSTABLE"

        print(f"\n{name}: {status}")

        for product in sorted_products:
            print(
                f"  ${product['price'] / 100:.2f} - "
                f"{product['name']}"
            )

    return results


def analyze_stability():
    """Print a summary of each algorithm's stability."""
    results = demonstrate_stability()

    print("\nStability Summary")
    print("-" * 40)

    for name, stable in results.items():
        result = "Stable" if stable else "Unstable"
        print(f"{name}: {result}")

    return results


# ============================================================================
# PART 4: PERFORMANCE BENCHMARKING
# ============================================================================

def extract_values(data):
    """
    Extract numeric values from a JSON dataset.

    Supports lists of numbers, dictionaries containing lists, and lists
    of records with common numeric fields.
    """
    if isinstance(data, list):
        values = data

    elif isinstance(data, dict):
        possible_keys = (
            "data", "values", "items", "numbers",
            "array", "records", "dataset"
        )

        values = None

        for key in possible_keys:
            if key in data and isinstance(data[key], list):
                values = data[key]
                break

        if values is None:
            # Avoid accidentally treating named test cases as one dataset.
            values = list(data.values())

    else:
        raise ValueError("Unsupported dataset format.")

    if values and isinstance(values[0], dict):
        possible_fields = (
            "price", "amount", "value", "id",
            "quantity", "timestamp"
        )

        selected_field = None

        for field in possible_fields:
            if all(field in item for item in values):
                if all(
                    isinstance(item[field], (int, float))
                    and not isinstance(item[field], bool)
                    for item in values
                ):
                    selected_field = field
                    break

        if selected_field is None:
            raise ValueError(
                "Could not find a numeric field in the dataset records."
            )

        values = [item[selected_field] for item in values]

    if not all(
        isinstance(value, (int, float)) and not isinstance(value, bool)
        for value in values
    ):
        raise ValueError("Dataset must contain numeric values.")

    return values


def benchmark_algorithm(algorithm, values):
    """Measure execution time and peak traced memory usage."""
    tracemalloc.start()

    try:
        start_time = time.perf_counter()
        result = algorithm(values)
        elapsed_time = time.perf_counter() - start_time

        _, peak_memory = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()

    correct = result == sorted(values)

    return {
        "time_seconds": elapsed_time,
        "memory_kb": peak_memory / 1024,
        "correct": correct,
    }


def benchmark_all_datasets():
    """Run each sorting algorithm on each generated dataset."""
    dataset_dir = Path("datasets")

    dataset_files = [
        ("Orders (Nearly Sorted)", dataset_dir / "orders.json"),
        ("Products (Duplicate Prices)", dataset_dir / "products.json"),
        ("Inventory (Random)", dataset_dir / "inventory.json"),
        ("Activity Log (Mostly Sorted)", dataset_dir / "activity_log.json"),
    ]

    sample_size = 5000
    all_results = {}

    print("\n" + "=" * 70)
    print("SORTING PERFORMANCE BENCHMARKS")
    print("=" * 70)
    print(f"Maximum sample size per dataset: {sample_size:,}")
    print("Bubble Sort and Selection Sort may take longer on large samples.")

    for dataset_name, file_path in dataset_files:
        if not file_path.exists():
            print(f"\nSkipping {dataset_name}: {file_path} not found.")
            continue

        try:
            data = load_json_file(file_path)
            values = extract_values(data)
        except (OSError, json.JSONDecodeError, ValueError) as error:
            print(f"\nSkipping {dataset_name}: {error}")
            continue

        sample = values[:sample_size]
        all_results[dataset_name] = {}

        print(f"\nDataset: {dataset_name}")
        print(f"Values tested: {len(sample):,}")
        print("-" * 70)
        print(
            f"{'Algorithm':<18} {'Time (sec)':>14} "
            f"{'Peak Memory (KB)':>20} {'Correct':>10}"
        )

        for algorithm_name, algorithm in ALGORITHMS.items():
            try:
                result = benchmark_algorithm(algorithm, sample)
                all_results[dataset_name][algorithm_name] = result

                print(
                    f"{algorithm_name:<18} "
                    f"{result['time_seconds']:>14.6f} "
                    f"{result['memory_kb']:>20.2f} "
                    f"{str(result['correct']):>10}"
                )

            except (MemoryError, RecursionError) as error:
                print(f"{algorithm_name} could not complete: {error}")

    return all_results


# ============================================================================
# PART 5: MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    test_sorting_correctness()
    analyze_stability()
    benchmark_all_datasets()
