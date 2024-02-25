# Physics Engine version 1.0
# This is a simple physics engine that calculates the angle and velocity of a rocket to hit a ship
# Oblique Projectile Motion

import math

rocketLaunchAngle = 0
rocketLaunchVelocity = 0
rocketXAxisLocation = 10

rocketLaunchFlyTime = 0
rocketLaunchTryTime = 0

gravity = 9.8

doesRocketHitTheShip = True

print("Welcome to the Physics Engine version 1.0")
shipXAxisLocation = int(input("Please enter the location of the ship in x-axis between 0 and 1000 "))

while doesRocketHitTheShip:
    if (shipXAxisLocation - 50) < rocketXAxisLocation < (shipXAxisLocation + 50):
        print("You hit the ship! Congratulations!")
        print("Physics Engine Details: ")
        print("Rocket Angle: " + str(rocketLaunchAngle))
        print("Rocket Velocity: " + str(rocketLaunchVelocity))
        print("Rocket Fly Time: " + str(rocketLaunchFlyTime))
        print("Rocket Max height: " + str(round(rocketLaunchYAxisVelocity ** 2 / (2 * gravity))))
        print("Rocket X-Axis Location: " + str(rocketXAxisLocation))
        print("Try Time: " + str(rocketLaunchTryTime))

        doesRocketHitTheShip = False
    else:
        rocketLaunchTryTime += 1
        rocketLaunchAngle = round(int(input("Please enter the angle of the rocket between 1 and 89 ")))
        rocketLaunchVelocity = round(int(input("Please enter the velocity of the rocket NO LIMIT ")))

        rocketLaunchYAxisVelocity = round((math.sin(math.radians(rocketLaunchAngle))) * rocketLaunchVelocity)
        rocketLaunchXAxisVelocity = round((math.cos(math.radians(rocketLaunchAngle))) * rocketLaunchVelocity)

        rocketLaunchFlyTime = round((rocketLaunchYAxisVelocity / gravity) * 2)
        rocketXAxisLocation = round(rocketLaunchXAxisVelocity * rocketLaunchFlyTime)

        if rocketXAxisLocation > (shipXAxisLocation + 50):
            print("You missed the ship! Try again!")

            print("The rocket fell +" + str(rocketXAxisLocation - (shipXAxisLocation + 50)) + "m away from the ship")
        else:
            if (shipXAxisLocation - 50) < rocketXAxisLocation < (shipXAxisLocation + 50):
                pass
            else:
                print("You missed the ship! Try again!")

                print("The rocket fell -" + str((shipXAxisLocation - 50) - rocketXAxisLocation) + "m away from the ship")