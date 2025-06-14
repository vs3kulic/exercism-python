"""A module to calculate age on different planets based on Earth seconds."""

class SpaceAge:
    """This class represents a person's age in seconds and calculate their age on different planets."""
    EARTH_YEAR_IN_SECONDS = 31557600  # Average year length in seconds
    PLANET_YEARS = {
        'earth': 1,
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
        }

    def __init__(self, seconds):
        """Initialize the SpaceAge with the given seconds."""
        self.seconds = seconds
    
    def on_earth(self):
        """Calculate the age on Earth."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        return round(earth_years, 2)

    def on_mercury(self):
        """Calculate the age on Mercury."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        mercury_age = earth_years / self.PLANET_YEARS['mercury']
        return round(mercury_age, 2)

    def on_venus(self):
        """Calculate the age on Venus."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        venus_age = earth_years / self.PLANET_YEARS['venus']
        return round(venus_age, 2)

    def on_mars(self):
        """Calculate the age on Mars."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        mars_age = earth_years / self.PLANET_YEARS['mars']
        return round(mars_age, 2)

    def on_jupiter(self):
        """Calculate the age on Jupiter."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        jupiter_age = earth_years / self.PLANET_YEARS['jupiter']
        return round(jupiter_age, 2)

    def on_saturn(self):
        """Calculate the age on Saturn."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        saturn_age = earth_years / self.PLANET_YEARS['saturn']
        return round(saturn_age, 2)

    def on_uranus(self):
        """Calculate the age on Uranus."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        uranus_age = earth_years / self.PLANET_YEARS['uranus']
        return round(uranus_age, 2)

    def on_neptune(self):
        """Calculate the age on Neptune."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        neptune_age = earth_years / self.PLANET_YEARS['neptune']
        return round(neptune_age, 2)
