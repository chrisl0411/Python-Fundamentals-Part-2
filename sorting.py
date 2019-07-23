def permute (a, lo, hi):
  if (lo == hi):
    print (a)
  else:
    for i in range (lo, hi):
      a[i], a[lo] = a[lo], a[i]
      permute (a, lo + 1, hi)
      a[i], a[lo] = a[lo], a[i]

def sub_sets (a, b, idx):
  if (idx == len(a)):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[idx])
    sub_sets (a, b, idx + 1)
    sub_sets (a, c, idx + 1)


def seq_search (a, x):
  for i in range (len(a)):
    if (a[i] == x):
      return i
  return -1

def seq_search_2 (a, x):
  count = 0
  for i in range (len(a)):
    if (a[i] == x):
      count += 1
  return count

def binary_search (a, x):
  lo = 0
  hi = len(a) - 1
  while (lo <= hi):
    mid = (lo + hi) // 2
    if (x > a[mid]):
      lo = mid + 1
    elif (x < a[mid]):
      hi = mid - 1
    else:
      return mid
  return -1

def selection_sort (a):
  for i in range (len(a) - 1):
    # find the minimum
    min_num = a[i]
    min_idx = i
    for j in range (i + 1, len(a)):
      if (a[j] < min_num):
        min_num = a[j]
        min_idx = j

    # swap the minimum element with the element at the ith place
    a[min_idx] = a[i]
    a[i] = min_num


def main ():
  
  a = ['A', 'B', 'C', 'D']
  b = []

  # test all subsets
  print ("Testing All Subsets")
  sub_sets (a, b, 0)
  print()

  # test all permutations
  print ("Testing All Permutations")
  permute (a, 0, len(a))
  print()

main()