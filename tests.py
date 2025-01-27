from datastructures import Series, DataFrame

# Test 1: Series of integers
int_series = Series([1, 2, 3], int)
print("Test 1:", int_series)
assert str(int_series) == "1, 2, 3", "Test 1 failed"

# Test 2: Series of floats
float_series = Series([1.5, 2.5, 3.5], float)
print("Test 2:", float_series)
assert str(float_series) == "1.5, 2.5, 3.5", "Test 2 failed"

# Test 3: Series with None
mixed_series = Series([1, None, 3], int)
print("Test 3:", mixed_series)
assert str(mixed_series) == "1, None, 3", "Test 3 failed"

# Test 4: Series with invalid type (should raise ValueError)
try:
    invalid_series = Series(["a", "b", 1], str)
except ValueError as exception:
    print("Test 4:", exception)

# Test 5: Add Series of the same type
sum_series = int_series + Series([4, 3, 2], int)
print("Test 5:", sum_series)
assert str(sum_series) == "5, 5, 5", "Test 5 failed"

# Test 6: Compare two Series
equal_series = int_series == Series([1, 2, 3], int)
print("Test 6:", equal_series)
assert str(equal_series) == "True, True, True", "Test 6 failed"

# Test 7: Filter Series using Booleans
filtered_series = int_series[int_series > 2]
print("Test 7:", filtered_series)
assert str(filtered_series) == "3", "Test 7 failed"

# Test 8: Invert a boolean Series
bool_series = Series([True, False, True], bool)
inverted_series = ~bool_series
print("Test 8:", inverted_series)
assert str(inverted_series) == "False, True, False", "Test 8 failed"

# Test 9: Logical AND between two boolean Series
logical_and_series = bool_series & Series([False, True, True], bool)
print("Test 9:", logical_and_series)
assert str(logical_and_series) == "False, False, True", "Test 9 failed"

# Test 10: Test DataFrame
df = DataFrame({
    "Integers": int_series,
    "Floats": float_series,
    "Booleans": bool_series
})
print("Test 10:")
print(str(df))

# Test 11: Access a column in df
df_column = df["Integers"]
print("Test 11:", df_column)
assert str(df_column) == "1, 2, 3", "Test 11 failed"

# Test 12: Filter df using Bools
filtered_df = df[df["Integers"] > 2]
print("Test 12:")
print(filtered_df)
print(df["Integers"] > 2)
# print(df[(df['Integers'] == 2) & (df['Integers'] < 1000)])

# Test 13: Arithmetic
df_addition = df["Floats"] + 5.0
print(f"Test 13: {df_addition}")
assert str(df["Floats"]) == "1.5, 2.5, 3.5", "Test 11 failed"

# Test 14: Comparison
df_comparison = df["Floats"] > 2.0
print("Test 14:", df_comparison)

# Test 15: Mismatched length columns (should raise ValueError)
try:
    invalid_df = DataFrame({"Integers": int_series, "Invalid": Series([1, 2], int)})
except ValueError as exception:
    print("Test 15:", exception)

# Test 16: Access DataFrame with boolean index
df_boolean_index = df[df["Booleans"]]
print("Test 16:")
print(df_boolean_index)

# Test 17: Perform addition for Series
series_add_scalar = int_series + 10
print("Test 17:", series_add_scalar)
assert str(series_add_scalar) == "11, 12, 13", "Test 17 failed"

# Test 18: Greater than comparison for Series
series_gt_scalar = float_series > 2.0
print("Test 18:", series_gt_scalar)
assert str(series_gt_scalar) == "False, True, True", "Test 18 failed"

# Test 19: Less than comparison for Series
series_lt_scalar = int_series < 3
print("Test 19:", series_lt_scalar)
assert str(series_lt_scalar) == "True, True, False", "Test 19 failed"

# Test 20: Perform and operation between two Series
bool_series_and = Series([True, False, True], bool) & Series([True, True, False], bool)
print("Test 20:", bool_series_and)
assert str(bool_series_and) == "True, False, False", "Test 20 failed"

# Test 21: Provided test example from writeup
sku_series = Series(["X4E", "T3B", "F8D", "C7X"], str)
price_series = Series([7.0, 3.5, 8.0, 6.0], float)
sales_series = Series([5, 3, 1, 10], int)
tax_series = Series([False, False, True, False], bool)

df = DataFrame({
    "SKU": sku_series,
    "price": price_series,
    "sales": sales_series,
    "taxed": tax_series
})

result = df[(df["price"] + 5.0 > 10.0) & (df["sales"] > 3) & ~df["taxed"]]["SKU"]
print("Test 21: ", result)
assert(str(result) == "X4E, C7X")
