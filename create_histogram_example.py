
def create_histogram(arr):
  histogram = {}
  for i in range(0, len(arr), 1):
    k = arr[i]
    if k not in histogram:
      histogram[k] = 0
    histogram[k] += 1
  return histogram



numbers = [1,1,2,2,2,2,3,5,3,2,1,1,1,5,3]
hg = create_histogram(numbers)
print(numbers)
print(hg)
