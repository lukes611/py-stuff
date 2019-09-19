
def create_histogram(arr):
  histogram = {}
  for i in arr:
    if i not in histogram:
      histogram[i] = 0
    histogram[i] += 1
  return histogram



numbers = [1,1,2,2,2,2,3,5,3,2,1,1,1,5,3]
hg = create_histogram(numbers)
print(numbers)
print(hg)
