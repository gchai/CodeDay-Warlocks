from sprite_strip_anim import *

FPS = 120
frames = FPS / 12

#Human Idle:
human_idle_left_strips = SpriteStripAnim('human_walking.png', (0,64,64,64), 1, -1, True, frames)

human_idle_right_strips = SpriteStripAnim('human_walking.png', (0,192,64,64), 1, -1, True, frames)

human_idle_up_strips = SpriteStripAnim('human_walking.png', (0,0,64,64), 1, -1, True, frames)

human_idle_down_strips = SpriteStripAnim('human_walking.png', (0,128,64,64), 1, -1, True, frames)

#Human Walking:
human_walking_left_strips = SpriteStripAnim('human_walking.png', (0,64,64,64), 9, -1, True, frames)

human_walking_right_strips = SpriteStripAnim('human_walking.png', (0,192,64,64), 9, -1, True, frames)

human_walking_up_strips = SpriteStripAnim('human_walking.png', (0,0,64,64), 9, -1, True, frames)

human_walking_down_strips = SpriteStripAnim('human_walking.png', (0,128,64,64), 9, -1, True, frames)


#Skeleton Idle:
skeleton_idle_left_strips = SpriteStripAnim('skeleton_walking.png', (0,64,64,64), 1, -1, True, frames)

skeleton_idle_right_strips = SpriteStripAnim('skeleton_walking.png', (0,192,64,64), 1, -1, True, frames)

skeleton_idle_up_strips = SpriteStripAnim('skeleton_walking.png', (0,0,64,64), 1, -1, True, frames)

skeleton_idle_down_strips = SpriteStripAnim('skeleton_walking.png', (0,128,64,64), 1, -1, True, frames)


#Skeleton Walking:
skeleton_walking_left_strips = SpriteStripAnim('skeleton_walking.png', (0,64,64,64), 9, -1, True, frames)

skeleton_walking_right_strips = SpriteStripAnim('skeleton_walking.png', (0,192,64,64), 9, -1, True, frames)

skeleton_walking_up_strips = SpriteStripAnim('skeleton_walking.png', (0,0,64,64), 9, -1, True, frames)

skeleton_walking_down_strips = SpriteStripAnim('skeleton_walking.png', (0,128,64,64), 9, -1, True, frames)


#Dying:
dying_strips = SpriteStripAnim('death.png', (0,0,64,64), 6, -1, True, frames)



#Blocking:
block_left_strips = SpriteStripAnim('block.png', (0,64,64,64), 7, -1, True, frames)

block_right_strips = SpriteStripAnim('block.png', (0,192,64,64), 7, -1, True, frames)

block_up_strips = SpriteStripAnim('block.png', (0,0,64,64), 7, -1, True, frames)

block_down_strips = SpriteStripAnim('block.png', (0,128,64,64), 7, -1, True, frames)



#Magic Attacks(fireball, homing lightning):
magic_left_strips = SpriteStripAnim('magic_attack.png', (0,64,64,64), 6, -1, True, frames)

magic_right_strips = SpriteStripAnim('magic_attack.png', (0,192,64,64), 6, -1, True, frames)

magic_up_strips = SpriteStripAnim('magic_attack.png', (0,0,64,64), 6, -1, True, frames)

magic_down_strips = SpriteStripAnim('magic_attack.png', (0,128,64,64), 6, -1, True, frames)


#Ice Arrow Magic:
ice_arrow_left_strips = SpriteStripAnim('ice_arrow.png', (0,64,64,64), 13, -1, True, frames)

ice_arrow_right_strips = SpriteStripAnim('ice_arrow.png', (0,192,64,64), 13, -1, True, frames)

ice_arrow_up_strips = SpriteStripAnim('ice_arrow.png', (0,0,64,64), 13, -1, True, frames)

ice_arrow_down_strips = SpriteStripAnim('ice_arrow.png', (0,128,64,64), 13, -1, True, frames)



