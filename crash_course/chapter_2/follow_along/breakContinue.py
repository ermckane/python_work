while True:
    print('Who are you?')
    name = input()
    if name != 'Emry':
        continue  
    while True:
        print('Hello Emry. What is the magic word?')
        password = input()
        if password != 'Starfish':
            continue
        elif password == 'Starfish':
            break
    break
print('Access Granted')
