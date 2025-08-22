import numpy as np

data = np.loadtxt("iris.csv", delimiter=',', skiprows=1)
print("\nReshaping Output\n")
print("Iris Dataset Original Numpy Array Shape : "+str(data.shape))
single = data.ravel()
print("Reshape to Single Dimension Array : "+str(single.shape))
multi = np.reshape(data, (data.shape[0], data.shape[1], 1))
print("Reshape to Three Dimension Array : "+str(multi.shape))

print("\nSlicing Numpy Output\n")
slicing = data[0:100,0:3]
print("Slice first 100 Rows and 3 columns : "+str(slicing.shape))

print("\nArithmetic SUM Operations of entire Numpy ARRAY\n")
print("SUM = "+str(data.sum()))
print("AVG = "+str(data.mean()))      

print("\nAggregation Operations of Numpy ARRAY\n")
print("MIN = "+str(data.min()))
print("MAX = "+str(data.max()))
print("STD = "+str(data.std()))
