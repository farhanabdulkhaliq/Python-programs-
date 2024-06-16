command = ''
started = False

while True:
    command = input('> ').lower()
    if command == 'help':
        print('start - to start type start')
        print('stop - to stop type stop')
        print('quit - to exit type quit')
    elif command == 'start':
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car started... Ready to go')
    elif command == 'stop':
        if not started  :
            print('Car is already stopped')
        else:
            started = False
            print('Car stopped')
    elif command == 'quit':
        break
    else :
        print("Sorry, I don't understand that")
