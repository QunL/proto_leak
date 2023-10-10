import psutil
import os
import datetime
from schema_pb2 import value_test_topic

process = psutil.Process(os.getpid())

def get_rss_MB():
    return (process.memory_full_info().rss / 1024) / 1024

print("Memory consumed at the beginning", get_rss_MB())

lst = value_test_topic()
while(1):
    for _ in range(1000000):
        event_dt = datetime.datetime.utcnow()
        lst.myField1 = 1234567
        lst.myField2 = event_dt.timestamp()
        lst.myField3 = "abc " * 100
        abc = b'abc' + lst.SerializeToString()
        msg = {}
        msg['event'] = abc

    print("Memory consumed after parsed", get_rss_MB())

    #lst = None
    print("Memory consumed after deallocating", get_rss_MB())
    time.sleep(1)
