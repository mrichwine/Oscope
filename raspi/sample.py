from i2ctest import analog_read

import time

while True:
    counts = analog_read(0)
    voltage = (counts/1024.0)*5.0
    print(counts,voltage)
    time.sleep(1.0)