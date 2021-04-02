import sys
import task_3

try:
    task_3.foreign_currency(sys.argv[1])
except IndexError:
    print(sys.argv[0])

