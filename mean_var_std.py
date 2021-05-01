import numpy as np

def calculate(list):
  flattened = np.array(list)
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  a = np.array([list[0:3], list[3:6], list[6:9]])

  print(a.mean(axis=0))

  obj = {'mean': [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), flattened.mean()], 
  'variance': [a.var(axis=0).tolist(), a.var(axis=1).tolist(), flattened.var()], 
  'standard deviation': [a.std(axis=0).tolist(), a.std(axis=1).tolist(), flattened.std()], 
  'max': [a.max(axis=0).tolist(), a.max(axis=1).tolist(), flattened.max()], 
  'min':[a.min(axis=0).tolist(), a.min(axis=1).tolist(), flattened.min()], 
  'sum':[a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), flattened.sum()]}
  
  return obj