namespace SpriteKind {
    export const Cash = SpriteKind.create()
}
/**
 * All info om AJ
 */
/**
 * Her er oppstarten. AJ starter på Start flagget, og det er lagt inn hvordan AJ skal bevege seg.
 */
/**
 * Hvordan AJ skal bevege seg ved hopp
 */
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    AJ.vy = -150
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Cash, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeScoreBy(1)
})
/**
 * Info om tilemap og bakgrunner må inn her
 */
function Next_level () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        value.destroy()
    }
    curren_level += 1
    if (curren_level == 1) {
        tiles.setTilemap(tilemap`level2`)
        scene.setBackgroundColor(9)
    } else if (curren_level == 2) {
        tiles.setTilemap(tilemap`level1`)
        scene.setBackgroundColor(11)
        for (let index = 0; index < 18; index++) {
            Money = sprites.create(img`
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
                `, SpriteKind.Cash)
            tiles.placeOnRandomTile(Money, sprites.swamp.swampTile16)
        }
    } else {
        game.over(false)
    }
    tiles.placeOnRandomTile(AJ, assets.tile`myTile1`)
    tiles.placeOnRandomTile(AJ, assets.tile`myTile13`)
    for (let value1 of tiles.getTilesByType(sprites.dungeon.buttonPinkDepressed)) {
        Enemy1 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        tiles.placeOnTile(Enemy1, value1)
        Enemy1.follow(AJ, 30)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite, location) {
    Next_level()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile14`, function (sprite, location) {
    Next_level()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    if (AJ.bottom < otherSprite.y) {
        AJ.vy = -100
        info.changeScoreBy(1)
    } else {
        info.changeLifeBy(-1)
    }
})
let Enemy1: Sprite = null
let Money: Sprite = null
let curren_level = 0
let AJ: Sprite = null
AJ = sprites.create(img`
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
    `, SpriteKind.Player)
scene.cameraFollowSprite(AJ)
controller.moveSprite(AJ, 100, 0)
AJ.ay = 500
info.setLife(3)
Next_level()
