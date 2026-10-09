"""
Data Generator for Sorting Assignment
Generates four datasets with different characteristics for sorting algorithm analysis.
"""

import random
import json
import os

def generate_datasets():
    """Generate four datasets representing different sorting scenarios."""
    
    # Create datasets directory
    if not os.path.exists("datasets"):
        os.makedirs("datasets")
    
    print("Generating sorting datasets...\n")
    
    # ========================================================================
    # Dataset A: Order Processing Queue (50,000 entries)
    # Scenario: E-commerce orders mostly in chronological order with requeued failed payments
    # ========================================================================
    print("Dataset A: Order Processing Queue")
    print("  Scenario: E-commerce order processing")
    print("  Size: 50,000 entries")
    print("  Characteristics: Nearly sorted (95% in order, 5% out of place)")
    
    # Generate mostly sorted data
    orders = list(range(100000, 150000))
    
    # Randomly swap 5% of adjacent pairs to simulate requeued orders
    num_swaps = len(orders) // 20
    for _ in range(num_swaps):
        i = random.randint(0, len(orders) - 2)
        orders[i], orders[i + 1] = orders[i + 1], orders[i]
    
    with open("datasets/orders.json", "w") as f:
        json.dump(orders, f)
    
    print("  ✓ Generated: datasets/orders.json\n")
    
    # ========================================================================
    # Dataset B: Product Catalog (100,000 entries)
    # Scenario: E-commerce products with many duplicate prices
    # ========================================================================
    print("Dataset B: Product Catalog")
    print("  Scenario: E-commerce product sorting by price")
    print("  Size: 100,000 entries")
    print("  Characteristics: Many duplicates (common price points like $9.99, $19.99)")
    
    # Generate products with clustering around common price points
    common_prices = [999, 1999, 2999, 4999, 9999, 14999, 19999]  # Prices in cents
    products = []
    
    for _ in range(100000):
        if random.random() < 0.7:  # 70% are common prices
            price = random.choice(common_prices)
        else:  # 30% are random prices
            price = random.randint(100, 50000)
        products.append(price)
    
    random.shuffle(products)
    
    with open("datasets/products.json", "w") as f:
        json.dump(products, f)
    
    print("  ✓ Generated: datasets/products.json\n")
    
    # ========================================================================
    # Dataset C: Inventory Reconciliation (25,000 entries)
    # Scenario: Warehouse SKU data in random order, memory-constrained environment
    # ========================================================================
    print("Dataset C: Inventory Reconciliation")
    print("  Scenario: Warehouse inventory system")
    print("  Size: 25,000 entries")
    print("  Characteristics: Random order, wide value range")
    
    inventory = [random.randint(1000000, 9999999) for _ in range(25000)]
    
    with open("datasets/inventory.json", "w") as f:
        json.dump(inventory, f)
    
    print("  ✓ Generated: datasets/inventory.json\n")
    
    # ========================================================================
    # Dataset D: Customer Activity Log (75,000 entries)
    # Scenario: User events mostly chronological with historical corrections
    # ========================================================================
    print("Dataset D: Customer Activity Log")
    print("  Scenario: User activity tracking")
    print("  Size: 75,000 entries")
    print("  Characteristics: Mostly sorted with random historical inserts (90% sorted)")
    
    # Generate mostly sorted timestamps
    activity_log = list(range(1000000, 1075000))
    
    # Insert 10% random historical corrections
    num_inserts = len(activity_log) // 10
    for _ in range(num_inserts):
        i = random.randint(1, len(activity_log) - 1)
        # Insert an older timestamp at a random position
        historical_value = random.randint(1000000, activity_log[i])
        activity_log.insert(i, historical_value)
    
    # Trim to exactly 75,000
    activity_log = activity_log[:75000]
    
    with open("datasets/activity_log.json", "w") as f:
        json.dump(activity_log, f)
    
    print("  ✓ Generated: datasets/activity_log.json\n")
    
    # ========================================================================
    # Generate Small Test Cases for Verification
    # ========================================================================
    print("="*70)
    print("GENERATING TEST CASES")
    print("="*70 + "\n")
    
    test_cases = {
        "small_random": [64, 34, 25, 12, 22, 11, 90],
        "small_sorted": [1, 2, 3, 4, 5, 6, 7],
        "small_reverse": [7, 6, 5, 4, 3, 2, 1],
        "small_duplicates": [5, 2, 8, 2, 9, 1, 5, 8],
        "expected_sorted": {
            "small_random": [11, 12, 22, 25, 34, 64, 90],
            "small_sorted": [1, 2, 3, 4, 5, 6, 7],
            "small_reverse": [1, 2, 3, 4, 5, 6, 7],
            "small_duplicates": [1, 2, 2, 5, 5, 8, 8, 9]
        }
    }
    
    with open("datasets/test_cases.json", "w") as f:
        json.dump(test_cases, f, indent=2)
    
    print("✓ Test cases generated: datasets/test_cases.json")
    print("\nDataset generation complete!")
    print("\nYou can now implement your sorting algorithms in starter_code.py")
    print("and use these datasets to benchmark performance.\n")

if __name__ == "__main__":
    generate_datasets()