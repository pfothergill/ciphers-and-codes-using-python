import time
import sys

blah = "This is written slowly\n"

for l in blah:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.2)