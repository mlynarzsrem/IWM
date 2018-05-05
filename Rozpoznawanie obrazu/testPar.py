import multiprocessing as mp
import time
from  joblib import Parallel,delayed
def fun(x):
    print(x)
if __name__ =="__main__":
    pnum_cores= mp.cpu_count()
    start_time = time.time()
    pool=  mp.Pool(processes=4)
    r = pool.map_async(fun,range(1000000))
    r.wait()
    print("--- %s seconds ---" % (time.time() - start_time))