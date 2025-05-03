"""
Assignment Overview:

You are building a Dog Image Browser using the Dog CEO REST API.

The app should allow users to:
- View a list of all available dog breeds
- Get a random image of a breed
- Get a random image of a sub-breed

You will be using the Dog CEO API: https://dog.ceo/dog-api/

Your app should display a main menu with the following options:
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

The system should handle the following errors:
- Handling errors when a user enters an invalid menu option
- Handling errors when a user enters a breed that does not exist
- Handling errors when a user enters a sub-breed that does not exist
- Handling connection errors when calling the API

If there is an error you should print your own custom error message to the user and allow them to try again.
- Hint: you can use a while loop + try / except blocks to handle this

You should use try / except blocks to handle these errors.

You can either use the should use the requests library or the http.client library to make your requests

"""


import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return {}

def get_random_image(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("message")
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching image for breed '{breed}': {e}")
        return None

    """GET request to fetch a random image from a breed."""
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/images/random
    # TODO: Return the image URL or handle errors
pass

def get_random_sub_breed_image(breed, sub_breed):
    url = f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("message")
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching image for sub-breed '{sub_breed}' of breed '{breed}': {e}")
        return None

    """GET request to fetch a random image from a sub-breed."""
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random
    # TODO: Return the image URL or handle errors
pass

def show_breeds(breeds_dict):
    if not isinstance(breeds_dict, dict):
        print("Invalid data format.")
        return

    all_breeds = list(breeds_dict.keys())
    all_breeds.sort()

    for i in range(0, len(all_breeds), 5):
        print(", ".join(all_breeds[i:i+5]))

    """Prints all available breeds 5 per line."""
    # TODO: Print all breeds (sorted), 5 per line
pass

def main():
     while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            breeds = get_all_breeds()
            show_breeds(breeds)

        elif choice == "2":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()

            if breed in breeds:
                image_url = get_random_image(breed)
                print(f"Random image of {breed}: {image_url}")
            else:
                print(f"Breed '{breed}' not found.")

        elif choice == "3":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()

            if breed in breeds and breeds[breed]:
                sub_breeds = breeds[breed]
                print(f"Available sub-breeds for {breed}: {', '.join(sub_breeds)}")
                sub_breed = input("Enter sub-breed name: ").strip().lower()

                if sub_breed in sub_breeds:
                    image_url = get_random_sub_breed_image(breed, sub_breed)   #lines 129 through 134 i got from chatgpt
                    print(f"Random image of {sub_breed} {breed}: {image_url}")
                else:
                    print(f"Sub-breed '{sub_breed}' not found for breed '{breed}'.")
            else:
                print(f"Breed '{breed}' not found or has no sub-breeds.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
