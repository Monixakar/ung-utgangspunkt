@namespace
class SpriteKind:
    Cash = SpriteKind.create()
# Info om tilemap og bakgrunner må inn her
def Next_level():
    global curren_level, Money, Enemy1
    for value in sprites.all_of_kind(SpriteKind.enemy):
        value.destroy()
    curren_level += 1
    if curren_level == 1:
        tiles.set_tilemap(tilemap("""
            level2
        """))
        scene.set_background_color(9)
    elif curren_level == 2:
        tiles.set_tilemap(tilemap("""
            level1
        """))
        scene.set_background_color(11)
        for index in range(18):
            Money = sprites.create(img("""
                    . . b b b . . . . . . . 
                                    . b 5 5 5 b . . . . . . 
                                    b 5 5 5 5 5 b . . . . . 
                                    b 5 3 5 1 5 b . . . . . 
                                    b 5 3 5 1 d b . . . . . 
                                    b 5 d 1 3 3 b . . . . . 
                                    b 5 3 d 3 5 b . . . . . 
                                    c 5 5 5 5 5 c . . . . . 
                                    c 5 5 5 5 5 c . . . . . 
                                    . f 5 5 5 f . . . . . . 
                                    . . f f f . . . . . . . 
                                    . . . . . . . . . . . .
                """),
                SpriteKind.Cash)
            tiles.place_on_random_tile(Money, sprites.swamp.swamp_tile16)
    else:
        game.over(False)
    tiles.place_on_random_tile(AJ, assets.tile("""
        myTile1
    """))
    tiles.place_on_random_tile(AJ, assets.tile("""
        myTile13
    """))
    for value1 in tiles.get_tiles_by_type(sprites.dungeon.button_pink_depressed):
        Enemy1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . f f 7 7 7 7 f f . . . . 
                            . . . 2 f 2 f 7 7 f 2 f 2 . . . 
                            . . . 2 7 1 f 8 8 f 1 7 2 . . . 
                            . . . 2 f 8 8 8 8 8 8 f 2 . . . 
                            . . . . f f 7 7 7 7 f f . . . . 
                            . . . . f 5 2 2 2 2 5 f . . . . 
                            . . . 5 7 2 2 2 2 2 2 7 5 . . . 
                            . . . . 7 . 7 . 7 . 7 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        tiles.place_on_tile(Enemy1, value1)
        Enemy1.follow(AJ, 30)
"""

All info om AJ

"""
"""

Her er oppstarten. AJ starter på Start flagget, og det er lagt inn hvordan AJ skal bevege seg.

"""
# Hvordan AJ skal bevege seg ved hopp

def on_up_pressed():
    AJ.vy = -150
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Cash, on_on_overlap)

def on_overlap_tile(sprite, location):
    Next_level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    Next_level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile14
    """),
    on_overlap_tile2)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    if AJ.bottom < otherSprite.y:
        AJ.vy = -100
        info.change_score_by(1)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Enemy1: Sprite = None
Money: Sprite = None
curren_level = 0
AJ: Sprite = None
AJ = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f . . . . . 
            . . . . f f f f f f f f . . . . 
            . . . f 5 e 4 4 4 4 e 5 f . . . 
            . . f 5 5 5 5 5 5 5 5 5 5 f . . 
            . . f 5 e 6 5 e e 5 6 e 5 f . . 
            . . f 5 f f e e e e f f 5 f . . 
            . . f 6 f 6 f e e f 6 f 6 f . . 
            . f f 6 e 1 f 4 4 f 1 e 6 f f . 
            . . . 6 f 4 4 4 4 4 4 f 6 . . . 
            . . 6 f f f e e e e f f f 6 . . 
            . . e e f 6 9 9 9 9 6 f e e . . 
            . . e 4 8 9 9 9 9 9 9 8 4 e . . 
            . . e f 6 9 6 9 6 9 6 6 f e . . 
            . . . f f 1 d 1 d 1 d f f . . . 
            . . . . . f f 6 6 f f . . . . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(AJ)
controller.move_sprite(AJ, 100, 0)
AJ.ay = 500
info.set_life(3)
Next_level()