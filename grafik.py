
import matplotlib.pyplot as plt
import numpy as np
import math

def grafik_sqrt():	
	# 100 linearly spaced numbers
	x = np.linspace(-5,5,100)

	# the function, which is y = x^2 here
	# y = x**2 + x -12
	y = np.sqrt(2*x+3)
	y1=x

	# setting the axes at the centre
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	# plot the function
	plt.plot(x,y, 'r')
	plt.plot(x,y1, 'g')

	# show the plot
	plt.show()

def grafik_kuadrat():	
	# 100 linearly spaced numbers
	x = np.linspace(-5,5,100)

	# the function, which is y = x^2 here
	y = x**2 + x -12

	# setting the axes at the centre
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	# plot the function
	plt.plot(x,y, 'r')

	# show the plot
	plt.show()


def grafik_pangkat3():	
	# 100 linearly spaced numbers
	x = np.linspace(-5,5,100)

	# the function, which is y = x^3 here
	y = x**3

	# setting the axes at the centre
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	# plot the function
	plt.plot(x,y, 'g')

	# show the plot
	plt.show()

def grafik_sinus():
	# 100 linearly spaced numbers
	x = np.linspace(-np.pi,np.pi,100)

	# the function, which is y = sin(x) here
	y = np.sin(x)

	# setting the axes at the centre
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	# plot the function
	plt.plot(x,y, 'b')

	# show the plot
	plt.show()

def grafik_multi_sinus():
	# 100 linearly spaced numbers
	x = np.linspace(-np.pi,np.pi,100)

	# the function, which is y = sin(x) here
	y = np.sin(x)

	# setting the axes at the centre
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	# plot the functions
	plt.plot(x,y, 'b', label='y=sin(x)')
	plt.plot(x,2*y, 'c', label='y=2sin(x)')
	plt.plot(x,3*y, 'r', label='y=3sin(x)')

	plt.legend(loc='upper left')

	# show the plot
	plt.show()

def grafik_geser_sinus():
	# 100 linearly spaced numbers
	x = np.linspace(-np.pi,np.pi,100)

	# the functions, which are y = sin(x) and z = cos(x) here
	y = np.sin(x)
	z = np.cos(x)

	# setting the axes at the centre
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	# plot the functions
	plt.plot(x,y, 'c', label='y=sin(x)')
	plt.plot(x,z, 'm', label='y=cos(x)')

	plt.legend(loc='upper left')

	# show the plot
	plt.show()

def grafik_exponential():
	# 100 linearly spaced numbers
	x = np.linspace(-2,2,100)

	# the function, which is y = e^x here
	y = np.exp(x)

	# setting the axes at the centre
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	# plot the function
	plt.plot(x,y, 'y', label='y=e^x')
	plt.legend(loc='upper left')

	# show the plot
	plt.show()

grafik_sqrt()
# grafik_kuadrat()
# grafik_pangkat3()
# grafik_sinus()
# grafik_multi_sinus()
# grafik_geser_sinus()
# grafik_exponential()

