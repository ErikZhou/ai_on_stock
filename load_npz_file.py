from numpy import load

data = load('/Users/zhoueric/.keras/datasets/mnist.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
