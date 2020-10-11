
import sys, itertools
sys.stdin = open('1.txt', 'r')

def main():
    global x, d, n, resh
    a = []
    x = input()
    x = x.lower()
    n = len(x)
    d = {}
    for i in x:
        if 'a'<= i <= 'z':
            d[i] = 0
    col = 2 ** len(d)
    d_k = sorted(d)
    form = []
    for i in range(n):
        form.append(x[i])

    m = int(input())

    for i in range(m):
        a.append([x for x in input().split()])
    kol = 0
    for i in a:
        for j in i:
            if j == '#':
                kol += 1


    for d_k in itertools.permutations(''.join(d), len(d)):
        k = 0
        for numb in range(2 ** kol):
            numb = bin(numb)[2:]
            numb += '0' * (kol - len(numb))
            form_a = reverse(a, numb)
            #print(form_a)
            for i in range(len(a)):
                for j in range(len(form)):
                    if x[j] in d_k:
                        form[j] = form_a[i][d_k.index(x[j])]


                resh = ''
                for mkd in form:
                    resh += str(mkd)

                if (ev()) != int(a[i][-1]):
                    break
                else:
                    k += 1
            if k == m:
                print(d_k)
                exit()

def ev():
    return int(eval(resh.replace('*', ' and ').replace('+', ' or ').replace('-', 'not ')))

def reverse(a, numb):
    form_a = [[]]
    k = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '#':
                form_a[i].append(numb[k])
            else:
                form_a[i].append(a[i][j])
        form_a.append([])
    return form_a



main()