import sys , getopt
import re
from collections import Counter
import ipdb


def count_C(file_pth):
    rule = re.compile(r"[^a-z]")
    counter = Counter()
    with open(file_pth, encoding="utf-8") as f:
        for line in f:
            line_result = rule.sub("" ,line.lower())
            counter.update(line_result)
    sum = 0 
    for charactor  in counter:
        frequency = counter[charactor]
        sum += frequency
    for charactor , frequency in counter.most_common():
        print("Charactor: {0} Times: {1} Frequency: {2} "\
            .format(charactor , frequency , frequency/sum)) 

opts , args = getopt.getopt(sys.argv[1:] ,"-h-c:")
for opt , arg in opts :
    if opt in ('-h'):
        print("help: ******** ")
        sys.exit(0)
    elif opt in ('-c'):
        count_C(arg)