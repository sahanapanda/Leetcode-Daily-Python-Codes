class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        # Sort the asteroids in ascending order
        asteroids.sort()
        
        # Greedily collide with each asteroid from smallest to largest
        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
                
        return True
        
