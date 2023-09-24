import collections

header = 'MARKS      CLASS      NAME       ID'
row = '92         2          Calum      1'

Student = collections.namedtuple('Student', header.split())
s = Student(*row.split())
print(s)
