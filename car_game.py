import pygame

command = ''
started = False

pygame.init()
pygame.mixer.init()

bye_sfx = pygame.mixer.Sound('Car_game/bye.wav')
start_sfx = pygame.mixer.Sound('Car_game/car_start.mp3')
engine_sfx = pygame.mixer.Sound('Car_game/car_rev.mp3')
car_stop_sfx = pygame.mixer.Sound('Car_game/car_stop.wav')

while True:
    command = input('> ').lower()
    if command == 'help':
        print('start - to start type start')
        print('stop - to stop type stop')
        print('quit - to exit type quit')
        print('rev engine - to rev engine type rev engine')
    elif command == 'start':
        if started:
            print('Car is already started')
        else:
            started = True
            start_sfx.play()
            print('Car started... Ready to go')             
    elif command == 'stop':
        if not started  :
            print('Car is already stopped')
        else:
            started = False
            print('Car stopped')
            engine_sfx.stop()
            start_sfx.stop()
            car_stop_sfx.play()
    elif command == 'rev engine' and not started:
        print('Car is not started!')
    elif command == 'rev engine' and started:
        print('Vroom! Vroom!')
        engine_sfx.play()
       
    elif command == 'quit':
        engine_sfx.stop()
        car_stop_sfx.stop()
        engine_sfx.stop()
        bye_sfx.play()
        break
    
    else :
        print("Sorry, I don't understand that")

pygame.mixer.quit()
pygame.quit()

