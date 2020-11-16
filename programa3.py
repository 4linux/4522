import time
 
import numpy as np
 
 
 
from class_summary_statistics_numba import SummaryStatisticsNumba
 
 
 
def main(one_dimensional_array):
 
   
 
#     create class summary statistics_numba class object
 
   class_summary_statistics_numba = SummaryStatisticsNumba()
 
   
 
#     calculate number of observation
 
   number_observation = class_summary_statistics_numba.calculate_number_observation(one_dimensional_array)
 
   print("Number of Observation: {} ".format(number_observation))
 
       
 
#     calculate arithmetic mean
 
   arithmetic_mean = class_summary_statistics_numba.calcuate_arithmetic_mean(one_dimensional_array, number_observation)
 
   print("Arithmetic Mean: {} ".format(arithmetic_mean))
 
   
 
#     calculatte median
 
   median = class_summary_statistics_numba.calculate_median(one_dimensional_array, number_observation)
 
   print("Median: {} ".format(median))
 
   
 
#     calculate sample standard deviation
 
   sample_standard_deviation = class_summary_statistics_numba.calculate_sample_standard_deviation(one_dimensional_array, number_observation, arithmetic_mean)
 
   print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
 
   
 
if __name__ == '__main__':
 
   start_time = time.clock()  
 
   one_dimensional_array = np.arange(1000000000, dtype=np.float64)        
 
   main(one_dimensional_array)
 
   end_time = time.clock()
 
   print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))


