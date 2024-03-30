# Physics Engine version 1.1
import math
import random

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches

bullet_max_velocity = 1800
bullet_min_velocity = 330
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
# Boolean

print("Welcome to the Physics Engine version 1.1")

while not hit_target:
    bullet_velocity = (bullet_max_velocity + bullet_min_velocity) / 2
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
        bullet_x_axis_velocity = round((math.cos(math.radians(bullet_angle))) * bullet_velocity)
        bullet_y_axis_velocity = round((math.sin(math.radians(bullet_angle))) * bullet_velocity)

        bullet_fly_time = round(((bullet_y_axis_velocity / 9.8) * 2))
        bullet_fly_distance = round(bullet_x_axis_velocity * bullet_fly_time)

        if target_distance >= bullet_fly_distance:
            print("Mermi öne düştü")
            bullet_min_velocity = bullet_velocity
        elif bullet_fly_distance >= target_distance + target_size:
            print("The bullet fell behind the target!")
            bullet_max_velocity = bullet_velocity

        shot_attempts += 1

fig, ax = plt.subplots()
square = patches.Rectangle((target_distance, 0), target_size, 200, edgecolor='red', facecolor='red')
ax.add_patch(square)

# Sınırları işaretlemelerle uyumlu hale getirin
plt.xlim(0.0, target_distance + target_size + 5000)
plt.ylim(0.0, target_distance)

plt.gca().set_aspect('equal', adjustable='box')  # Ensures equal aspect ratio

# Her 500 binde bir göster
plt.xticks(range(0, int(target_distance + target_size + 5000) + 1, 2500))
plt.yticks(range(0, int(target_distance) + 1, 2500))

plt.title('Square Plot with add_patch() - Different Scales')
plt.show()
