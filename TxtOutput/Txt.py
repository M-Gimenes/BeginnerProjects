def calculateMean(list):
  return sum(list) / len(list)


def calculateVar(list, mean):
  x = 0
  for i in range(len(list)):
    x += (list[i] - mean)**2
  x /= len(list)
  return x


def calculateSD(var):
  return var**0.5


def calculateHist(list, hist):
  for i in list:
    if i // 10 == 10:
      ind = 9
    else:
      ind = i // 10
    try:
      hist[ind] += 1
    except:
      hist.insert(ind, 1)


def calculateMode(list):
  count = []
  for i in list:
    count.append(list.count(i))
  dic1 = dict(zip(list, count))
  dic2 = {str(j) for (j, k) in dic1.items() if k == max(count)}
  return dic2


ord = ["First", "Second", "Third", "Fourth", "Fifth"]
modal = ["unimodal", "bimodal", "multimodal"]

result = open("texts/histogram.txt", "w")

for i in range(5):
  try:
    arq = open(f"texts/arquivo_teste_{i+1}.txt", "r")
  except:
    print("File not found")
    continue

  nums = arq.readlines()
  list = []
  hist = []
  list.extend([int(num.strip()) for num in nums])
  list.pop(0)
  arq.close()

  mean = calculateMean(list)
  var = calculateVar(list, mean)
  sd = calculateSD(var)
  mode = calculateMode(list)
  calculateHist(list, hist)

  result.write("_" * 30 + "\n")
  result.write(f"{ord[i]} archive".center(30) + "\n")

  result.write("-" * 30 + "\n")
  result.write("Mean".ljust(10) + "=".center(10) + f"{mean:.2f}".rjust(10) +
               "\n")

  result.write("-" * 30 + "\n")
  result.write("Variance".ljust(10) + "=".center(10) + f"{var:.2f}".rjust(10) +
               "\n")

  result.write("-" * 30 + "\n")
  result.write("Std".ljust(10) + "=".center(10) + f"{sd:.2f}".rjust(10) + "\n")

  result.write("-" * 30 + "\n")
  result.write("Mode".ljust(10) + "=".center(10) + (", ".join(mode)).rjust(10) + "\n")
  
  try:
    result.write(f"Sampling is {modal[len(mode)-1]}".center(30)+"\n")
  except:
    result.write(f"Sampling is {modal[2]}".center(30)+"\n")
  
  result.write("-" * 30 + "\n")
  result.write("Histogram".center(30) + "\n")

  for j in range(10):
    if j != 9:
      result.write(f"{0+j*10:>2} - {9+j*10:>3}".ljust(10))
    else:
      result.write(f"{0+j*10:>2} - {10+j*10:>3}".ljust(10))
    result.write("=".center(10))
    try:
      result.write(f"{hist[j]}".rjust(10))
    except:
      result.write("0".rjust(10))
    result.write("\n")

  result.write("_" * 30 + "\n")
  result.write("\n")

result.close()
