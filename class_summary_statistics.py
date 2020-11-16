import sys
 
import traceback
 
import time
 
from math import sqrt
 
 
 
class SummaryStatistics(object):
 
   """
 
   calculate number of observations, arithmetic mean, median
 
   and sample standard deviation using standard procedures
 
   """
 
   def __init__(self):
 
       pass
 
       
 
   def calculate_number_observation(self, one_dimensional_array):        
 
       """
 
       calculate  number of observations
 
       :param one_dimensional_array: numpy one dimensional array
 
       :return number of observations value
 
       """
 
       number_observation = 0
 
       try:
 
           number_observation = one_dimensional_array.size   
 
       except Exception:
 
           self.print_exception_message()
 
       return number_observation
 
 
 
   def calculate_arithmetic_mean(self, one_dimensional_array, number_observation):    
 
       """
 
       calculate arithmetic mean
 
       :param one_dimensional_array: numpy one dimensional array
 
       :param number_observation: number of observations
 
       :return arithmetic mean value
 
       """
 
       arithmetic_mean = 0.0
 
       try:
 
           sum_result = 0.0
 
           for i in range(number_observation):       
 
               sum_result += one_dimensional_array[i]    
 
           arithmetic_mean = sum_result / number_observation
 
       except Exception:
 
           self.print_exception_message()
 
       return arithmetic_mean
 
 
 
   def calculate_median(self, one_dimensional_array, number_observation):      
 
       """
 
       calculate  median
 
       :param one_dimensional_array: numpy one dimensional array
 
       :param number_observation: number of observations
 
       :return median value
 
       """
 
       median = 0.0
 
       try:
 
           one_dimensional_array.sort()    
 
           half_position = number_observation // 2
 
           if not number_observation % 2:
 
               median = (one_dimensional_array[half_position - 1] + one_dimensional_array[half_position]) / 2.0
 
           else:
 
               median = one_dimensional_array[half_position]        
 
       except Exception:
 
           self.print_exception_message()
 
       return median
 
 
 
   def calculate_sample_standard_deviation(self, one_dimensional_array, number_observation, arithmetic_mean):    
 
       """
 
       calculate sample standard deviation
 
       :param one_dimensional_array: numpy one dimensional array
 
       :param number_observation:  number of observations
 
       :param arithmetic_mean: arithmetic mean value
 
       :return sample standard deviation value
 
       """
 
       sample_standard_deviation = 0.0
 
       try:
 
           sum_result = 0.0
 
           for i in range(number_observation):                   
 
               sum_result += pow((one_dimensional_array[i] - arithmetic_mean), 2)            
 
           sample_variance = sum_result / (number_observation - 1)            
 
           sample_standard_deviation = sqrt(sample_variance)        
 
       except Exception:
 
           self.print_exception_message()
 
       return sample_standard_deviation
 
 
 
   def print_exception_message(self, message_orientation = "horizontal"):
 
       """
 
       print full exception message
 
       :param message_orientation: horizontal or vertical
 
       :return none
 
       """
 
       try:
 
           exc_type, exc_value, exc_tb = sys.exc_info()            
 
           file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]       
 
           time_stamp = " [Time Stamp]: " + str(time.strftime("%Y-%m-%d %I:%M:%S %p"))
 
           file_name = " [File Name]: " + str(file_name)
 
           procedure_name = " [Procedure Name]: " + str(procedure_name)
 
           error_message = " [Error Message]: " + str(exc_value)        
 
           error_type = " [Error Type]: " + str(exc_type)                    
 
           line_number = " [Line Number]: " + str(line_number)                
 
           line_code = " [Line Code]: " + str(line_code)
 
           if (message_orientation == "horizontal"):
 
               print( "An error occurred:{};{};{};{};{};{};{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
 
           elif (message_orientation == "vertical"):
 
               print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
 
           else:
 
               pass                    
 
       except Exception:
 
           pass


