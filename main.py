# Physics Engine version 1.1
import math
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches

# Constants
g = 9.8  # acceleration due to gravity

bullet_max_velocity = 1800
bullet_min_velocity = 330
# Metres per second

bullet_angle = 30
# Degrees

bullet_fly_time = 0
# Seconds

bullet_fly_distance = 0
# Metres

target_distance = 20000 + (200 * np.random.randint(-10, 10))
# Metres in x-axis

target_size = 1000 + (100 * np.random.randint(-2, 2))
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

        bullet_fly_time = round(((bullet_y_axis_velocity / 9.8) * 2) + 0.07)
        # 0.7 is the time it takes for the bullet to leave the barrel
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


# Time points
t = np.linspace(0, bullet_fly_time, num=500)

# Calculate trajectory
bullet_velocity = (bullet_max_velocity + bullet_min_velocity) / 2
x = bullet_velocity * t * np.cos(np.radians(bullet_angle))
y = bullet_velocity * t * np.sin(np.radians(bullet_angle)) - 0.5 * g * t**2 + firing_point_ground_clearance

# Plot trajectory
plt.plot(x, y, label='Bullet trajectory')

# Add legend
plt.legend()

plt.gca().set_aspect('equal', adjustable='box')  # Ensures equal aspect ratio

# Her 500 binde bir göster
plt.xticks(range(0, int(target_distance + target_size + 5000) + 1, 2500))
plt.yticks(range(0, int(5000) + 1, 2500))

plt.title('Square Plot with add_patch() - Different Scales')
plt.show()