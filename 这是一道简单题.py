# 题目描述
#
# 小红最近又遇到了个棘手的问题，他有一个字符串里面有括号（‘(’）和（‘)’）还有大小写英文字母他想知道在括号里的小写字母有几个，你能帮帮他么？
#
# （提示不会出现括号内包含括号的现象如：abcd（abcd（abcd））
# 输入
# 输入数据首先包含一个整数n(1&lt;=n&lt;=100)，表示测试实例的个数，然后是n行数据，每行包含一个字符串，（字符串的长度小于1000）
# 输出
# 对于每组字符串输出括号内小写字母的个数；
# 样例输入
#
# 1
# AbcdB(abcABC)efg
#
# 样例输出
#
# 3

a=int(input())
while 1:
    l=[x for x in input()]
    i=0
    s=0
    while l[i]!="\0":
        if l[i]=="(":
            j=i+1
            while l[j]!="\0":
                if l[j]==")":
                    k=i+1
                    while k<j:
                        if l[k]>="a" and l[k]<="z":
                            s=s+1
                    k=k+1
                i=j
                break
                 j=j+1
        i=i+1
    print("%d\n"%(s))
    a=a-1
































