import sys

ans = set(sys.argv[1:])
print('有 {n1} 個不重複字串 : {set1}'.format(n1=len(ans), set1=ans))
