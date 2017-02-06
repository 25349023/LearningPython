import sys

searchStr = sys.argv[1]
ans = sys.argv[2:]
print('{s1} 出現了 {n1} 次'.format(s1=searchStr, n1=ans.count(searchStr)))
