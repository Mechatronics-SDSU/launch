import yaml
import typing

FILENAME = "profiles.yaml"

def read_profile(profile_name: list) -> list[str]:
    """
    Reads a profile from a YAML file.
    Args:
        profile_name (str): The name of the profile to read.
    Returns:
        list: The profile data if found, otherwise None.
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

def get_profile_names() -> list[str]:
    """
    Returns a list of all profile names available in the YAML file.
    Returns:
        list: A list of profile names.
    """
    try:
        with open(FILENAME, 'r') as file:
            profiles = yaml.safe_load(file)
            return list(profiles.keys())
    except FileNotFoundError:
        print(f"Profile file '{FILENAME}' not found.")
        return []
    except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    profile_name = "all"
    profile_data = read_profile(profile_name)
    print(f"Profile '{profile_name}': {profile_data}")
    print(type(profile_data))

    # Get all profile names
    all_profiles = get_profile_names()
    print(f"Available profiles: {all_profiles}")
    print(type(all_profiles))
