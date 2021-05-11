def continousToBinary(data, column_name):
  average = data[column_name].mean()
  binary_column_name = "binary_"+column_name
  binary_column =(data[column_name] >= average).astype(int)
  data[binary_column_name] = binary_column
  return data
