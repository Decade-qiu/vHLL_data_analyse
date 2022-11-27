

pkt = [55.2396, 32.6223, 23.8228, 18.8094, 16.8121, 13.5889, 11.8804, 10.5555, 9.51766, 8.441]

elem = [27.416, 20.5525, 17.3998, 14.7123, 12.4634, 11.4325, 10.3262, 9.35439, 8.50448, 8.441]

p_ = [(i-pkt[9])/pkt[9] for i in pkt]

e_ = [(i-elem[9])/elem[9] for i in elem]

for i in pkt:
    print("%.2f" % i, end='\t')
print()

for i in elem:
    print("%.2f" % i, end='\t')
print()

for i in p_:
    print("%.2f%%" % (i*100), end='\t')
print()

for i in e_:
    print("%.2f%%" % (i*100), end='\t')
print()

for i in range(1, 11):
    print(i/10, end=', ')
