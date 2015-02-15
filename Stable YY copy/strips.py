from sprite_strip_anim import *

FPS = 120
frames = FPS / 12

#Movement:
	#Human Idle:
human_idle_left_strips = SpriteStripAnim('human_walking.png', (0,64,64,64), 1, -1, False, frames)
human_idle_right_strips = SpriteStripAnim('human_walking.png', (0,192,64,64), 1, -1, False, frames)
human_idle_up_strips = SpriteStripAnim('human_walking.png', (0,0,64,64), 1, -1, False, frames)
human_idle_down_strips = SpriteStripAnim('human_walking.png', (0,128,64,64), 1, -1, False, frames)

#Human Walking:
human_walking_left_strips = SpriteStripAnim('human_walking.png', (0,64,64,64), 9, -1, True, frames)
human_walking_right_strips = SpriteStripAnim('human_walking.png', (0,192,64,64), 9, -1, True, frames)
human_walking_up_strips = SpriteStripAnim('human_walking.png', (0,0,64,64), 9, -1, True, frames)
human_walking_down_strips = SpriteStripAnim('human_walking.png', (0,128,64,64), 9, -1, True, frames)

#Skeleton Idle:
skeleton_idle_left_strips = SpriteStripAnim('skeleton_walking.png', (0,64,64,64), 1, -1, False, frames)
skeleton_idle_right_strips = SpriteStripAnim('skeleton_walking.png', (0,192,64,64), 1, -1, False, frames)
skeleton_idle_up_strips = SpriteStripAnim('skeleton_walking.png', (0,0,64,64), 1, -1, False, frames)
skeleton_idle_down_strips = SpriteStripAnim('skeleton_walking.png', (0,128,64,64), 1, -1, False, frames)

#Skeleton Walking:
skeleton_walking_left_strips = SpriteStripAnim('skeleton_walking.png', (0,64,64,64), 9, -1, True, frames)
skeleton_walking_right_strips = SpriteStripAnim('skeleton_walking.png', (0,192,64,64), 9, -1, True, frames)
skeleton_walking_up_strips = SpriteStripAnim('skeleton_walking.png', (0,0,64,64), 9, -1, True, frames)
skeleton_walking_down_strips = SpriteStripAnim('skeleton_walking.png', (0,128,64,64), 9, -1, True, frames)

#Dying:
dying_strips = SpriteStripAnim('death.png', (0,0,64,64), 6, -1, False, frames)

#Blocking:
block_left_strips = SpriteStripAnim('block.png', (0,64,64,64), 7, -1, True, frames)
block_right_strips = SpriteStripAnim('block.png', (0,192,64,64), 7, -1, True, frames)
block_up_strips = SpriteStripAnim('block.png', (0,0,64,64), 7, -1, True, frames)
block_down_strips = SpriteStripAnim('block.png', (0,128,64,64), 7, -1, True, frames)


#Magic Attacks(fireball, lightning):
magic_left_strips = SpriteStripAnim('magic_attack.png', (0,64,64,64), 6, -1, True, frames)
magic_right_strips = SpriteStripAnim('magic_attack.png', (0,192,64,64), 6, -1, True, frames)
magic_up_strips = SpriteStripAnim('magic_attack.png', (0,0,64,64), 6, -1, True, frames)
magic_down_strips = SpriteStripAnim('magic_attack.png', (0,128,64,64), 6, -1, True, frames)

#Ice Arrow Magic:
ice_arrow_left_strips = SpriteStripAnim('ice_arrow.png', (0,64,64,64), 13, -1, True, frames)
ice_arrow_right_strips = SpriteStripAnim('ice_arrow.png', (0,192,64,64), 13, -1, True, frames)
ice_arrow_up_strips = SpriteStripAnim('ice_arrow.png', (0,0,64,64), 13, -1, True, frames)
ice_arrow_down_strips = SpriteStripAnim('ice_arrow.png', (0,128,64,64), 13, -1, True, frames)




#Magic Animation:
	#Fireball:
fire_left_strips = SpriteStripAnim('fireball.png', (0,0,64,64), 8, -1, True, frames)
fire_right_strips = SpriteStripAnim('fireball.png', (0,256,64,64), 8, -1, True, frames)
fire_up_strips = SpriteStripAnim('fireball.png', (0,128,64,64), 8, -1, True, frames)
fire_down_strips = SpriteStripAnim('fireball.png', (0,384,64,64), 8, -1, True, frames)
fire_UL_strips = SpriteStripAnim('fireball.png', (0,64,64,64), 8, -1, True, frames)
fire_UR_strips = SpriteStripAnim('fireball.png', (0,192,64,64), 8, -1, True, frames)
fire_BL_strips = SpriteStripAnim('fireball.png', (0,448,64,64), 8, -1, True, frames)
fire_BR_strips = SpriteStripAnim('fireball.png', (0,320,64,64), 8, -1, True, frames)

#Lightning:
lightning_left_strips = SpriteStripAnim('lightning.png', (0,0,64,64), 8, -1, True, frames)
lightning_right_strips = SpriteStripAnim('lightning.png', (0,256,64,64), 8, -1, True, frames)
lightning_up_strips = SpriteStripAnim('lightning.png', (0,128,64,64), 8, -1, True, frames)
lightning_down_strips = SpriteStripAnim('lightning.png', (0,384,64,64), 8, -1, True, frames)
lightning_UL_strips = SpriteStripAnim('lightning.png', (0,64,64,64), 8, -1, True, frames)
lightning_UR_strips = SpriteStripAnim('lightning.png', (0,192,64,64), 8, -1, True, frames)
lightning_BL_strips = SpriteStripAnim('lightning.png', (0,448,64,64), 8, -1, True, frames)
lightning_BR_strips = SpriteStripAnim('lightning.png', (0,320,64,64), 8, -1, True, frames)



