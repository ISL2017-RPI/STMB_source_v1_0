import scipy.io 
import numpy as np 
import STMBv1_0


class STMBFeatSelector:
	"""
	This class implements a feature selection method:
	
	It automatically select features that best fit the labels

	Input:

	A: Collection of vectors in high dimensional space. 
	Concretely, inputs are doubly-indexable numbers that can be called as A[i,j].
	Rows i are samples and columns j are features. 
	The entries can be interger, continuous values or categorical values, 
	but should be expressed in a numerical form.

	B: The corresponding labels as a vector in a numerical form. This should be a 
	row vector, and the length should be identifcal to the number of raw in A

	Output:

	W: Dimensionality reduced vectors, it is a numpy matrix with one row per vector.
	"""

	is_feature_selection = True
	hyperparameters = {}


	def __init__(self):
		return None


	def fit_transform(self, A, B):

    		scipy.io.savemat('datamat.mat', mdict={'traindata': A, 'traintargets': B})

    		my_stmb = STMBv1_0.initialize()
    		k = np.array(my_stmb.STMB_binsearch(), dtype=np.int16)
		print k.shape
    		m, n = k.shape
    		k = np.reshape(k, [m, ])

    		return A[:, k - 1]


    	fit_transform.__annotations__ = {'A': 'NumpyArray(m, n)', 'B': 'NumpyArray(m, )', 'return': 'NumpyArray(m, k)'}



""" usage example """

if __name__ == "__main__":

	import STMBFeatSelector as fs
	
	stmb = fs.STMBFeatSelector()
	
	W = stmb.fit_transform(A, B)
