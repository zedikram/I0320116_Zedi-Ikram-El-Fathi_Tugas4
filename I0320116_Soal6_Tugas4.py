a = 4
b = 11
c = 0
print('nilai:',a,', binary :', format(a,'08b'))
print('nilai :',b,', binary :', format(b,'08b'))

c = a | b;
print('line 1 - value of c is ',c,', binary :',format (c,'08b'))

c = 4 >> 11;
print('line 3 - value of c is ',c,', binary :', format(c,'08b'))

c = 4 ^ 11;
print('line 3 - value of c is ',c,', binary :', format(c, '08b'))

c = ~4;
print('line 4 - value of c is ',c,', binary :', format(c,'08b'))

c= 11 & 4;
print('line 5 - value of c is ',c,', binary:', format(c,'08b'))