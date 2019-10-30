#!/usr/bin/env python3

# Created by: Jacob B
# Created on: Oct 2019
# This program displays two scenes on the PyBadge

import ugame
import stage
import constants


def menu_scene():
    # this function is the menu scene on the PyBadge

    # new pallete for black filled text
    NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                   b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    # setting the background
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # a list of sprites
    sprites = []

    # text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None,
                       palette=NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    # game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # start button is pressed
        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene():
    # this function is the game scene on the PyBadge

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    # a list of sprites
    sprites = []

    # Buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Get sound ready
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create sprite
    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 75, 56)
    sprites.insert(0, ship)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)

        if keys & ugame.K_X:
            # print("A")
            pass
        if keys & ugame.K_O:
            # print("B")
            pass
        if keys & ugame.K_START:
            # print("K_START")
            pass
        if keys & ugame.K_SELECT:
            # print("K_SELECT")
            pass
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
            pass
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
            pass
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
            pass
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass

        # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # Play sound if A is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    menu_scene()
