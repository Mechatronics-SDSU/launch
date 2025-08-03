import yaml
import typing

FILENAME = "profiles.yaml"

def read_profile(profile_name: list) -> list[str]:
    """
    Reads a profile from a YAML file.
    Args:
        profile_name (str): The name of the profile to read.
    Returns:
        dict: The profile data if found, otherwise None.
    """
    try:
        with open(FILENAME, 'r') as file:
            profiles = yaml.safe_load(file)
            return profiles.get(profile_name, None)
    except FileNotFoundError:
        print(f"Profile file '{FILENAME}' not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    profile_name = "all"
    profile_data = read_profile(profile_name)
    print(f"Profile '{profile_name}': {profile_data}")
    print(type(profile_data))
