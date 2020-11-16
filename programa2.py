import time
 
import numpy as np
 
 
 
from class_summary_statistics_asyncio import SummaryStatisticsAsyncio
 
 
 
def main(one_dimensional_array):
 
   
 
#     create summary statistics asyncio class object
 
   summary_statistics_asyncio = SummaryStatisticsAsyncio()
 
 
 
#     call main method
 
   summary_statistics_asyncio.main(one_dimensional_array)
 
 
 
if __name__ == '__main__':
 
   start_time = time.clock()  
 
   one_dimensional_array = np.arange(1000000000, dtype=np.float64)        
 
   main(one_dimensional_array)
 
   end_time = time.clock()
 
   print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))


