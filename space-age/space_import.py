"""A module to demonstrate the SpaceAge class functionality."""
from space_age import SpaceAge

AGE_IN_EARTH_SECONDS = 1000000000  # Example age in seconds

def main():
    """Main function to demonstrate the SpaceAge class functionality."""
    planet_age = SpaceAge(AGE_IN_EARTH_SECONDS)

    try:
        print(f"Age on Earth: {planet_age.on_earth()} years")
        print(f"Age on Mercury: {planet_age.on_mercury()} years")
        print(f"Age on Venus: {planet_age.on_venus()} years")
        print(f"Age on Mars: {planet_age.on_mars()} years")
        print(f"Age on Jupiter: {planet_age.on_jupiter()} years")
        print(f"Age on Saturn: {planet_age.on_saturn()} years")
        print(f"Age on Uranus: {planet_age.on_uranus()} years")
        print(f"Age on Neptune: {planet_age.on_neptune()} years")
    except AttributeError as e:
        print(f"Error: {e}")

# This is the entry point of the module, also referred to as the main guard.
# It allows the module to be run as a script.
# If the module is imported, the main function will not run.
# This is useful for testing or when the module is used as part of a larger application.
if __name__ == "__main__":
    main()
