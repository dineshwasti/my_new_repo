import time
import os
import pandas
if os.path.exists("temp.csv"):
    data=pandas.read_csv("temp.csv")
    print(data.mean()["st2"])
else:
    print ("data does not exists")
    time.sleep(10)
