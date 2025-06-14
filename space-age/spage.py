"""A module to demonstrate the SpaceAge class functionality."""
from space_age import SpaceAge

def main():
    """Main function to demonstrate the SpaceAge class functionality."""
    age = SpaceAge(1000000000)

    try:
        print(f"Age on Earth: {age.on_earth()} years")
        print(f"Age on Mercury: {age.on_mercury()} years")
        print(f"Age on Venus: {age.on_venus()} years")
        print(f"Age on Mars: {age.on_mars()} years")
        print(f"Age on Jupiter: {age.on_jupiter()} years")
        print(f"Age on Saturn: {age.on_saturn()} years")
        print(f"Age on Uranus: {age.on_uranus()} years")
        print(f"Age on Neptune: {age.on_neptune()} years")
    except AttributeError as e:
        print(f"Error: {e}")

# This is the entry point of the module, also referred to as the main guard.
# It allows the module to be run as a script.
# If the module is imported, the main function will not run.
# This is useful for testing or when the module is used as part of a larger application.
if __name__ == "__main__":
    main()
