'''
class Series
Ensures all elements match the specified type
'''

# class DataType:
#   def __init__(self, data_type):
#     # check data_type

class Series:
  def __init__(self, data, data_type):
    self.data = []
    self.data_type = data_type
    # perform type check if all values conform to series type or are None
    for elm in data:
      if elm is None or isinstance(elm, data_type):
        self.data.append(elm)
      else:
        raise ValueError(str(elm), " does not match required type.")
  
  '''
  If key is a list or Series of Booleans, filter the Series based on list of Booleans.
  Key can also be int to get that index.
  Else, throw error.
  '''
  def __getitem__(self, key):
    if isinstance(key, list):
      for elm in key:
        if not isinstance(elm, bool):
          raise ValueError(f"Not all Booleans for {key} in filtering list.")
      # filter out values in series if False in that list
      return Series([d for d, k in zip(self.data, key) if k], self.data_type)
    # or it is a intger
    elif isinstance(key, int):
      if key < len(self.data):
        return self.data[key]
      else:
        raise ValueError("Key out of range.")
    # key is another series
    elif isinstance(key, Series) and key.data_type == bool:
      self.check_length(key)
      return Series([d for d, k in zip(self.data, key.data) if k], self.data_type)
    else:
      raise "Not Series indexable"

  '''
  Check if a Series and another Series are of the same length.
  '''
  def check_length(self, other):
    if len(other.data) != len(self.data):
      raise ValueError(f"Series {self.data} and {other.data} are of different lengths")
    
  '''
  Check if a Series and another Series are of the same type.
  '''
  def check_types(self, other):
    if other.data_type != self.data_type:
      raise ValueError("Series are of different types")
  
  def check_valid(self, other):
    self.check_length(other)
    self.check_types(other)

  '''
  Equality operation.
  If Series types or lengths are different, throw exception.
  Else return Boolean series.
  '''
  def __eq__(self, other):
    if isinstance(other, Series):
      self.check_valid(other)
      return Series([a == b for a, b in zip(self.data, other.data)], bool)
  
  def __add__(self, other):
    # if other is an int or a float
    if isinstance(other, (int, float)):
      
      return Series([elm + other for elm in self.data], self.data_type)
    elif isinstance(other, Series):
      # add the elements between two Series
      self.check_valid(other)
      return Series([elm + o for elm, o in zip(self.data, other.data)], self.data_type)

  # greater than operator
  def __gt__(self, other):
    if isinstance(other, (int, float)):
      return Series([elm > other for elm in self.data], bool)
    elif isinstance(other, Series):
      self.check_valid(other)
      return Series([d > o for d, o in zip(self.data, other.data)], bool)

  # less than operator
  def __lt__(self, other):
    if isinstance(other, (int, float)):
      return Series([elm < other for elm in self.data], bool)
    elif isinstance(other, Series):
      self.check_valid(other)
      return Series([d < o for d, o in zip(self.data, other.data)], bool)

  # ~ operator
  def __invert__(self):
    return Series([not elm for elm in self.data], bool)
  
  '''
  Using the word ''and'' between two series.
  '''
  def __and__(self, other):
    if isinstance(other, Series):
      return Series([a and b for a, b in zip(self.data, other.data)], bool)
    else:
      raise ValueError("Unsupported and operation for types")
  
  def __str__(self):
    return ', '.join(str(elm) for elm in self.data)

'''
class DataFrame
Create a dataframe that supports many types of operations.
Input data is a dictionary with the key as the name of the series, and the 
value as the Series
'''
class DataFrame:
  def __init__(self, data):
    self.columns = {}
    for key, series in data.items():
      if not isinstance(series, Series):
        raise ValueError(f"Column {key} is not a Series instance")
      if key in self.columns:
          raise ValueError(f"Column {key} already exists in the DataFrame")
      self.columns[key] = series
    self.check_valid()

  def check_valid(self):
    lengths = []
    for series in self.columns.values():
      lengths.append(len(series.data))
    if len(set(lengths)) > 1:
      raise ValueError("All columns in the DataFrame must have the same length")
  
  def __getitem__(self, key):
    # if key is a string (we just want to get that column)
    if isinstance(key, str):
      return self.columns[key]
    # if key is a Series
    elif isinstance(key, Series):
      if key.data_type is bool:
        return DataFrame({k: v[key.data] for k, v in self.columns.items()})
  
  def __str__(self):
    if len(self.columns) == 0:
      return ""
    column_names = list(self.columns.keys())
    header = ', '.join(column_names)
    rows = []
    for i in range(len(next(iter(self.columns.values())).data)):
        row_values = []
        for col in column_names:
            row_values.append(str(self.columns[col].data[i]))
        row = ', '.join(row_values)
        rows.append(row)
    return header + "\n" + "\n".join(rows)
