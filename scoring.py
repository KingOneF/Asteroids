from constants import ASTEROID_SMALL_POINTS, ASTEROID_MEDIUM_POINTS, ASTEROID_LARGE_POINTS, ASTEROID_MIN_RADIUS


class ScoreManager:
    def __init__(self):
        self.score = 0

    def add_points(self, asteroid):
        """Add points based on asteroid size"""
        points = self.get_points_for_asteroid(asteroid)
        self.score += points
        return points

    def reset(self):
        """Reset score to 0"""
        self.score = 0

    @staticmethod
    def get_points_for_asteroid(asteroid):
        """Calculate points based on asteroid size"""
        if asteroid.radius <= ASTEROID_MIN_RADIUS:
            return ASTEROID_SMALL_POINTS
        elif asteroid.radius <= ASTEROID_MIN_RADIUS * 2:
            return ASTEROID_MEDIUM_POINTS
        else:
            return ASTEROID_LARGE_POINTS
