text = "acá hay texto -"
""" Falta " y ' y \ """
alfabeto = ['!', '#', '$', '%', '&', '(', ')', '*','+', ',', '-', '.', '/', 
            '0','1','2','3','4','5','6','7','8','9',
            ':',';','<','=','>','?','@',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z',
            '[',']','^','_','`',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z',
            '{','|','}','~', ' ','\\'
            'Á','É','Í','Ó','Ú','Ñ',
            'á','é','í','ó','ú','ñ', 
            ]

data={}
done = {}
routes = {}
encodedText=""
id = 107

print('a' in alfabeto)

for i in text:
  if i not in alfabeto:
    print("El valor ", i, " no esta en el alfabeto")
    exit()
  if i in alfabeto and i not in data:
    id -= 1
    data[i]={'peso':1, 'id': id}
  
  if i in data:
    data[i]['peso'] +=1
  

print(data)

sorted_keys = sorted(data, key=lambda x: data[x]['peso'], reverse=True)

print(sorted_keys)

while len(sorted_keys) >1:
  ak = sorted_keys.pop()
  bk = sorted_keys.pop()
  akpeso = data[ak]['peso']
  bkpeso = data[ak]['peso']
  totalpeso = akpeso + bkpeso
  done[ak], done[bk] = data[ak], data[bk]
  del data[ak], data[bk]
  data[str(ak+bk)] = {'peso': totalpeso, 'left': ak, 'right': bk }
  sorted_keys = sorted(data, key= lambda x: data[x]['peso'], reverse=True)
  done[list(data.keys())[0]] = list(data.values())[0]
  print('\n', sorted_keys)

print("done")

def trace(currentNode, char, route):
  if 'left' in done[currentNode]:
    if char in done[currentNode]['left']:
      newRoute = route + '0'
      trace(done[currentNode['left']], char, newRoute)
  if 'right' in done[currentNode]:
    if char in done[currentNode]['right']:
      newRoute = route + '1'
      trace(done[currentNode['right']], char, newRoute)
  if 'left' not in done[currentNode]:
    if 'right' not in done[currentNode]:
      routes[char] = route

rootNode = list(data.keys())[0]
for i in rootNode:
  trace(rootNode, i , '')

for i in text:
  encodedText+= routes[i]

print('\n\nRoutes: ', routes)
print('\n',encodedText)