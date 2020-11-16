import time
 
import numpy as np
 
 
 
from class_summary_statistics import SummaryStatistics
 
 
 
def main(one_dimensional_array):
 
   
 
#     create summary statistics class object
 
   summary_statistics = SummaryStatistics()
 
   
 
#     calculate number of observation
 
   number_observation = summary_statistics.calculate_number_observation(one_dimensional_array)
 
   print("Number of Observation: {} ".format(number_observation))
 
   
 
#     calculate arithmetic mean
 
   arithmetic_mean = summary_statistics.calculate_arithmetic_mean(one_dimensional_array, number_observation)
 
   print("Arithmetic Mean: {} ".format(arithmetic_mean))
 
   
 
#     calculatte median
 
   median = summary_statistics.calculate_median(one_dimensional_array, number_observation)
 
   print("Median: {} ".format(median))
 
   
 
#     calculate sample standard deviation
 
   sample_standard_deviation = summary_statistics.calculate_sample_standard_deviation(one_dimensional_array, number_observation, arithmetic_mean)
 
   print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
 
 
 
if __name__ == '__main__':
 
   start_time = time.clock()  
 
   one_dimensional_array = np.arange(100000000, dtype=np.float64)        
 
   main(one_dimensional_array)
 
   end_time = time.clock()
 
   print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))


