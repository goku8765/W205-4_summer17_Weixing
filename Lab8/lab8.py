import sys



a = 'gunbarell'
b = 'gumbarrel'

w, h = len(b)+1, len(a)+1
# set first row
mtx = [[x for x in range(w)] for y in range(h)]
for i in range(w):
    mtx[i][0] = i 

for i in range(1, w):
    for j in range(1, h):
        if a[i-1] != b[j-1]:
            cost = 1
        else:
            cost = 0
        # mtx[height][width]
        mtx[i][j] = min(mtx[i-1][j]+1, mtx[i][j-1]+1, mtx[i-1][j-1]+cost)


sys.stdout = open('log.txt', 'w')
for j in range(1,h):
    for i in range(1,w):
        print(mtx[i][j], end =',')
    print('\n', end = '')
sys.stdout.close()
