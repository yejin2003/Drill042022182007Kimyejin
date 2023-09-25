from pico2d import *
TUK_WIDTH, TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image("character_move.png")


def handle_events():
    global running
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                x+=10
            elif event.key==SDLK_LEFT:
                x-=10
            elif event.key==SDLK_UP:
                y+=10
            elif event.key==SDLK_DOWN:
                y-=10
            elif event.key==SDLK_ESCAPE:
                running=False

running = True
frame = 0
x,y=TUK_WIDTH // 2,TUK_HEIGHT//2
hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame * 60, 67, 60, 50, x, y, 90, 100)
    update_canvas()
    handle_events()
    frame=(frame+1)%8
    delay(0.05)


close_canvas()