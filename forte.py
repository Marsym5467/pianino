
running = True
while running:
    screen.fill(WHITE)

    #кнопки
    for button in buttons:
        button.draw(screen, my_font)

        #клавіші
        draw_keys(screen,key_rects, pressed_keys)

        display.flip()

        for e in event.get():
            if e.type == QUIT:
                running = False


            #кнопки
            for button in buttons:
                burron.handle_event(e)

            #клавіатура
            if e.type == KEYDOWN:
                k = key.name(e.key)
                if k in sounds:

