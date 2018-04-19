guest_list = ['Bod','John','Jobs']
for name in guest_list:
    print('welcom {}'.format(name))
print('{} is can not come here'.format(guest_list[0]))
guest_list[0] = 'Tom'
for name in guest_list:
    print('welcom {}',format(name))
print('Now I hava a big table')
guest_list.insert(0,'Top')
guest_list.insert(2,'Mid')
guest_list.insert(-1,'Append')
for name in guest_list:
    print('welcom {}'.format(name))
print('Only Two')
guest_list.append('hah')
guest_list.append('hehe')
guest_list.append('hehe')
guest_list.append('hehe')

while len(guest_list) > 2:
    print('{}'.format(len(guest_list)))
    print('Sorry {}'.format(guest_list.pop()))

for name in guest_list:
    print('{} you can'.format(name))
    
del guest_list[1]
del guest_list[0]
print(guest_list)
print('{}'.format(len(guest_list)))