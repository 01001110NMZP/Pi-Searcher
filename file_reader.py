import sys
from pathlib import Path
from colorama import Fore

# ------------- colors
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
reset = Fore.RESET
# ------------- colors

path: Path = Path("one-million.txt")

contents: str = Path.read_text(path).strip()


def date_checker():
    try:

        date: str = input('Enter your birth date in mmddyy format:\n')

        # its -1 because at the beginning of the iteration it will be incremented
        # by 1 then we use that 0 for index purposes
        counter: int = -1

        # initializing our string that we want to be matched with date
        match_count: str = ''

        if date in contents:
            print("Yes, hold on I'm getting the digit")

            while True:

                if date == match_count:

                    print(f"\n\n {green}--- MATCHING DIGITS FOUND ---{reset}\n")
                    print(f"Starting digit: {counter - 5}\n"
                          f"Ending digit: {counter}\n"
                          f"Number: "
                          f"{contents[counter - 11: counter - 6]}"
                          f"{red}{contents[counter - 5: counter + 1]}{reset}"
                          f"{contents[counter + 1: counter + 6]}")

                    break
                else:

                    # checking that the length of match_count is always => 6
                    if len(match_count) == 6:
                        match_count = match_count[1:]

                    # adding 1 to counter for iteration
                    counter += 1

                    # adding the current digit to match_count for to check the string
                    match_count += contents[counter]
        else:
            print("nah")
    except IndexError:
        print("the proper format consists of a 6-digit number, dont input else than that")


seperator: str = '\n----------------------------------\n'


def main():
    while True:
        date_checker()
        while True:
            choice = input(f"{seperator}Want to try another date/number? ").lower()
            if "y" in choice:
                print(seperator.lstrip())
                main()
            elif "n" in choice:
                print('ok then, take care')
                sys.exit()
            else:
                print("I didn't understand, what did you say?")


if __name__ == '__main__':
    main()
