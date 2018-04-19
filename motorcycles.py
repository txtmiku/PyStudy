motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)
motorcycle[0] = 'ducati'
print(motorcycle)
motorcycle.append('ducati')
print(motorcycle)
motorcycle.insert(1,'Gin')
print(motorcycle)
del motorcycle[1]
print(motorcycle)
poped_one = motorcycle.pop()
print(poped_one)
print(motorcycle)
motorcycle.remove('ducati')
print(motorcycle)