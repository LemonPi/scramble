import time
#before = open("/proc/self/status")
begin_time = time.time()
#print("Before: {}".format(before.readlines()[11]))
import scrambler
scrambler.scramble("original.txt", "scrambled.txt")
import descrambler
descrambler.descramble("scrambled.txt", "descrambled.txt")
#after = open("/proc/self/status")
process_time = time.time() - begin_time
#print("After: {}".format(after.readlines()[11]))
print("Took {}s".format(process_time)) 
import filecmp
if filecmp.cmp("original.txt", "descrambled.txt"):
    print("Descrambler succeded")
else:
    print("Descrambler failed")
