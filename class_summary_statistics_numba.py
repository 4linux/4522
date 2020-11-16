import time
 
from numba import jit
 
import numpy as np
 
from math import sqrt
 
 
 
class SummaryStatisticsNumba(object):
 
   """
 
   calculate number of observations, arithmetic mean, median
 
   and sample standard deviation using numba library
 
   """
 
   def __init__(self):
 
       pass
 
       
 
   @jit
 
   def calculate_number_observation(self, one_dimensional_array):    
 
       """
 
       calculate  number of observations
 
       :param one_dimensional_array: numpy one dimensional array
 
       :return number of observations value
 
       """        
 
       number_observation = one_dimensional_array.size
 
       return number_observation
 
   
 
   @jit
 
   def calcuate_arithmetic_mean(self, one_dimensional_array, number_observation):    
 
       """
 
       calculate arithmetic mean
 
       :param one_dimensional_array: numpy one dimensional array
 
       :param number_observation: number of observations
 
       :return arithmetic mean value
 
       """
 
       sum_result = 0.0
 
       for i in range(number_observation):       
 
           sum_result += one_dimensional_array[i]    
 
       arithmetic_mean = sum_result / number_observation
 
       return arithmetic_mean
 
   
 
   @jit
 
   def calculate_median(self, one_dimensional_array, number_observation):      
 
       """
 
       calculate  median
 
       :param one_dimensional_array: numpy one dimensional array
 
       :param number_observation: number of observations
 
       :return median value
 
       """
 
       one_dimensional_array.sort()    
 
       half_position = number_observation // 2
 
       if not number_observation % 2:
 
           median = (one_dimensional_array[half_position - 1] + one_dimensional_array[half_position]) / 2.0
 
       else:
 
           median = one_dimensional_array[half_position]        
 
       return median
 
   
 
   @jit
 
   def calculate_sample_standard_deviation(self, one_dimensional_array, number_observation, arithmetic_mean):    
 
       """
 
       calculate sample standard deviation
 
       :param one_dimensional_array: numpy one dimensional array
 
       :param number_observation:  number of observations
 
       :param arithmetic_mean: arithmetic mean value
 
       :return sample standard deviation value
 
       """
 
       sum_result = 0.0
 
       for i in range(number_observation):                   
 
           sum_result += pow((one_dimensional_array[i] - arithmetic_mean), 2)            
 
       sample_variance = sum_result / (number_observation - 1)            
 
       sample_standard_deviation = sqrt(sample_variance)        
 
       return sample_standard_deviation


