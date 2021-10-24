
phonebook = {}

while True :
    action = input('Enter an action: ')

    if action == 'show':
        for phone, name in phonebook.items():
            print(name, ':', phone)

    elif action == 'Add':


            phone = input ('Enter a phone number: ')
            name = input('Enter a name: ')
            print('Added!')
            phonebook[phone] = name

    elif action == 'get':
            phone = input('Enter a phone number: ' )
            print('Name:', phonebook.get(phone,'undefined'))



