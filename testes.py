# Fazendo programa random

n2 = int(0)
n1 = int(0)
total = int(10000)
n = []

for i in range(0, 100):
  n.append(random.randint(1, 2))

for i in range(0, 100):
  if n[i] == int(1):
    n1 += 1
  else:
    n2 += 1

print('n1 {}, n2 {}'.format(n1, n2))

# lanches = ['amburgui', 'salxixa']
# print(' '.join(lanches))
# lanches[1] = 'salamandra'
# print(' '.join(lanches))

lanches = []
i = 0
while True:
  lanche = str(input('digite um lanche: '))
  i += 1
  if lanche == 'pare':
    break
  lanches.append(lanche)

for i in lanches:
  print(i)

i = 0
while i < len(lanches):
  lanche = str(input('digite um lanche: '))
  i += 1
  if lanche == 'pare':
    break
  lanches.append(lanche)

lanches[0] = 'caveira'
for i in lanches:
  print(i)
# def print_students(students):
#   print('nome: {}', students.)
