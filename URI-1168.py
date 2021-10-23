n_testes = int(input())
for i in range(n_testes):
    n = 0
    leds = input()
    for i in range(0, len(leds)):
        if leds[i] == '1':
            n = n + 2
        if leds[i] == '2':
            n = n + 5
        if leds[i] == '3':
            n = n + 5
        if leds[i] == '4':
            n = n + 4
        if leds[i] == '5':
            n = n + 5
        if leds[i] == '6':
            n = n + 6
        if leds[i] == '7':
            n = n + 3
        if leds[i] == '8':
            n = n + 7
        if leds[i] == '9':
            n = n + 6
        if leds[i] == '0':
            n = n + 6
    print('%d leds' %n)