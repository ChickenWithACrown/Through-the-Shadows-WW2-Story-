import time
from colorama import Fore, Style, init

def print_intro():
    print(Fore.GREEN + Style.BRIGHT + "Welcome to Through the Shadows - A WWII Story\n")
    print(Fore.YELLOW + Style.BRIGHT + "Loading the story...\n" + Style.RESET_ALL)

def read_story(file_path):
    try:
        with open(file_path, 'r') as file:
            story_content = file.read()
            type_out_with_color(story_content)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: The file {file_path} was not found.{Style.RESET_ALL}")

def type_out_with_color(text):
    init()  # Initialize colorama
    print(Fore.CYAN + Style.BRIGHT)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)  # Adjust the sleep time for typing speed
    print(Style.RESET_ALL + "\n")

# Replace 'your_story.txt' with the actual file path of your story.
def main():
    print_intro()
    read_story('read_story.txt')

if __name__ == "__main__":
    main()
