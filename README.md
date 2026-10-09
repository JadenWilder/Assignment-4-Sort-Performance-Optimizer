# Assignment 4: Sort Performance Optimizer

## Setup Instructions

### 1. Clone this repository and open in VS Code

```bash
git clone <REPO_URL>
cd REPO_NAME
code .
```

### 2. Generate the test datasets

Run the data generator to create four datasets with different characteristics:

```bash
python data_generator.py
# You may need to run python3 data_generator.py
```

This will create:
- `datasets/orders.json` - 50,000 nearly sorted order records
- `datasets/products.json` - 100,000 product prices with many duplicates
- `datasets/inventory.json` - 25,000 random inventory SKUs
- `datasets/activity_log.json` - 75,000 mostly sorted customer events
- `datasets/test_cases.json` - Small test cases for verification

### 3. Implement your sorting algorithms

Open `starter_code.py` and complete the four sorting functions:
1. `bubble_sort()` - Comparison-based sort with adjacent swapping
2. `selection_sort()` - Repeatedly finds minimum element
3. `insertion_sort()` - Builds sorted array one element at a time
4. `merge_sort()` - Divide-and-conquer with merging

### 4. Complete stability demonstration

Implement the `demonstrate_stability()` function to test which algorithms preserve the relative order of equal elements.

### 5. Test and benchmark

Uncomment the test functions in the `__main__` block:

```python
if __name__ == "__main__":
    test_sorting_correctness()      # Verify implementations work
    benchmark_all_datasets()         # Compare performance on all datasets
    analyze_stability()              # Test which algorithms are stable
```

Then run:

```bash
python starter_code.py
# or python3 starter_code.py
```

## The Four Scenarios

### Dataset A: Order Processing Queue (50,000 entries, nearly sorted)
**Scenario**: E-commerce orders mostly in chronological order with occasional requeued failed payments  
**Question**: Which algorithm performs best on nearly-sorted data?

### Dataset B: Product Catalog (100,000 entries, many duplicates)
**Scenario**: Product listings with many items at identical price points ($9.99, $19.99, etc.)  
**Question**: Does stability matter when multiple products share the same price?

### Dataset C: Inventory Reconciliation (25,000 entries, random)
**Scenario**: Warehouse SKU data in random order on memory-constrained servers  
**Question**: Which algorithm offers the best time/space trade-off?

### Dataset D: Customer Activity Log (75,000 entries, mostly sorted)
**Scenario**: User events mostly chronological with random historical corrections  
**Question**: How do different "mostly sorted" characteristics affect algorithm choice?

## What to Submit

Submit two files:
1. **Your completed Python file** (rename to `sorting_optimizer.py`)
2. **Written analysis document** (Google Doc or Word) containing:
   - Performance Analysis table (complexity and benchmark results)
   - Algorithm Selection Justification section (300-350 words)
   - Sorting Algorithm Trade-offs section (100-150 words)
   - Total: 400-500 words