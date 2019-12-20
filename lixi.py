import numpy as np

def qiankuan_n(n, benjin, benjin_lilv, lixi, lixi_lilv, qiankuan, huanqian):
    benjin_lixi = benjin * benjin_lilv
    lixi_sum = 0
    for i in range(len(lixi)):
        lixi_sum = lixi_sum + lixi[i]
    lixi_lixi = lixi_sum * lixi_lilv
    lixi.append(benjin_lixi + lixi_lixi)
    qiankuan.append(qiankuan[n-1] + lixi[n] - huanqian)
    return lixi, qiankuan
def jisuanqiankuan(N):
    benjin = 30
    lixi_n1 = 4.236777
    benjin_lilv = 0.007027
    lixi_lilv = 0.004684
    lixi = []
    qiankuan = []
    for n in range(N):
        if n == 0:
            lixi.append(lixi_n1)
            qiankuan.append(benjin + lixi_n1)
        elif n == 8:
            benjin = benjin - 10
            lixi, qiankuan = qiankuan_n(n, benjin, benjin_lilv, lixi, lixi_lilv, qiankuan, 10)
        elif n == 12:
            print("lixi[12]:",lixi)
            lixi[n-1] = lixi[n-1] - 5
            lixi, qiankuan = qiankuan_n(n, benjin, benjin_lilv, lixi, lixi_lilv, qiankuan, 5)
        else:
            lixi, qiankuan = qiankuan_n(n, benjin, benjin_lilv, lixi, lixi_lilv, qiankuan, 0)
    return qiankuan

def print_qiankuan(qiankuan):
    for i in range(len(qiankuan)):
        #print(i+1)
        print(qiankuan[i])

qiankuan = jisuanqiankuan(25)
print_qiankuan(qiankuan)

