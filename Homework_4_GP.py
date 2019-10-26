#!/usr/bin/env python
# coding: utf-8

# # Homework 4: Gaussian Process

# In[ ]:


# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)


# ### Question 1: Write down the Gaussian Kernal

# In[ ]:


# Define the Gaussian Kernal
def Kernel(x, y, variance, length_scale):
    Kernel =                              # Write the Kernal Function Here
    return Kernel


# *This is an intentional gap!*

# In[ ]:


# Define the parameters
num_functions_to_sample  = 5
num_samples_per_function = 20
noisy_std                = 0.05 # To match the note this is "sigma_n"
variance                 = 0.05 # To match the note this is "sigma_f"
length_scale             = 0.5  # To match the note this is "l"


# In[ ]:


# Random Data (Training Data)
# To match the note this is the "X" and "y" 
x = np.linspace(0, 2, 50)
y = np.linspace(0, 2, 50) + np.random.random([50,])


# In[ ]:


# sample locations
# To match the note this is "X*"
sample_points = np.linspace(0, 2, num_samples_per_function)


# In[ ]:


# Check the Joint Distribution
sns.jointplot(x=x, y=y,kind="kde");


# ### Question 2: Write the Equation for mean_condition 
# Hint: Check the Equation on Lecture 8, Page 6 (Equation $\bar{f_*}$)

# In[ ]:


# compute the mean conditioned on the data points
mean_cond =     # Write the Equation  


# *This is an intentional gap!*

# ### Question 3: Write the Equation for covariance
# Hint: Check the Equation on Lecture 8, Page 6 (Equation $cov(\bar{f_*})$)

# In[ ]:


# compute the covariance conditioned on the data points
cov_cond =       # Write the Equation  


# *This is an intentional gap!*

# In[ ]:


# draw sample functions and plot them
f = np.random.multivariate_normal(mean_cond, cov_cond, num_functions_to_sample)


# In[ ]:


# Check the sampled Equation
plt.figure(figsize=(16,8))
for i in range(num_functions_to_sample):
    plt.plot(sample_points, f[i,:],'x-', label = 'Sampled_Function' + str(i+1))

# plot data points
plt.plot(x, y, 'ko',label = 'Provided Points' )
plt.legend()

# plot uncertainty region
std = np.sqrt(cov_cond.diagonal())
plt.fill_between(sample_points, mean_cond - 2 * std, mean_cond + 2 * std,
               facecolor='lightgray')
plt.grid()
plt.title('Gaussian Process')

