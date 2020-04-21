class AsteroidCollision:

    def asteroidColliding(self, asteroids):

        while 1:

            result = []
            i = 0
            length = len(asteroids)

            while i < length:
                current_asteroid = asteroids[i]
                if i == length - 1:
                    next_asteroid = 0
                else:
                    next_asteroid = asteroids[i + 1]

                # if current asteroid in moving right and next asteroid is moving left than it will collide
                if next_asteroid < 0 < current_asteroid:
                    next_size = abs(next_asteroid)
                    # if right moving asteroid is bigger
                    if current_asteroid > next_size:
                        result.append(current_asteroid)
                    # if left moving asteroid is bigger
                    elif current_asteroid < next_size:
                        result.append(next_asteroid)
                    # if both asteroids are of same size than they destroy each other
                    i = i + 2
                else:
                    result.append(current_asteroid)
                    i = i + 1

            if not result or result == asteroids:
                break

            asteroids = result

        return result


object = AsteroidCollision()
asteroids = [5, 10, -5]
print(object.asteroidColliding(asteroids))