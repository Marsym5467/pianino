from pygame import Rect, transform, image
from effects import draw_key_effect, spawn_flying_note, update_and_draw_flying_notes

KEY_UNPRESSED = transform.scale(image.load('assets/image/key_unpressed.png'), (100, 250))

NOTE_BY_INDEX = {
    0:'C',
    1:'D',
    2:'E',
    3:'F',
    4:'G',
}

_PREV_PRESSED= set ()