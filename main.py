# Physics Engine version 1.1
import math
import random

import numpy as np

bullet_max_velocity = 1800
bullet_min_velocity = 330
bullet_velocity = (bullet_max_velocity + bullet_min_velocity) / 2
# Metres per second

bullet_angle = 30
# Degrees

bullet_fly_time = 0
# Seconds

bullet_fly_distance = 0
# Metres

target_distance = 20000 + (200 * random.randint(-10, 10))
# Metres in x-axis

target_size = 1000 + (100 * random.randint(-2, 2))
# Metres in x-axis

firing_point_ground_clearance = 21
# Metres in y-axis

shot_attempts = 0
# Number of shots fired

hit_target = False

print("Welcome to the Physics Engine version 1.1")

while not hit_target:
    if target_distance <= bullet_fly_distance <= target_distance + target_size:
        hit_target = True
        print("Target hit!")
        print("Number of shots fired: ", shot_attempts)
        print("Bullet velocity: ", bullet_velocity)
        print("Bullet angle: ", bullet_angle)
        print("Bullet fly time: ", bullet_fly_time)
        print("Bullet fly distance: ", bullet_fly_distance)
        print("Target distance: ", target_distance)
        print("Target size: ", target_size)
        print("Firing point ground clearance: ", firing_point_ground_clearance)
        break
    else:
        bullet_x_axis_velocity = round((math.sin(math.radians(bullet_angle))) * bullet_velocity)
        bullet_y_axis_velocity = round((math.cos(math.radians(bullet_angle))) * bullet_velocity)

        bullet_fly_time = round((bullet_y_axis_velocity / 9.8) / 2)
        bullet_fly_distance = round(bullet_x_axis_velocity * bullet_fly_time)

        if target_distance >= bullet_fly_distance:
            print("Mermi öne düştü")
            bullet_velocity = bullet_velocity + 20
        elif bullet_fly_distance >= target_distance + target_size:
            print("The bullet fell behind the target!")
            bullet_velocity = bullet_velocity - 20
        else:
            print("Something went wrong!")
        shot_attempts += 1
