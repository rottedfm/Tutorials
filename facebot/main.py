from utils import clear, print_banner, type_out_banner
import questionary
from questionary import Style

# Use the terminal's native blue
terminal_blue_style = Style([
    ("qmark", "fg:ansiblue bold"),
    ("question", "fg:ansiblue bold"),
    ("answer", "fg:ansiblue bold"),
    ("pointer", "fg:ansiblue bold"),
    ("highlighted", "fg:ansiblue bold"),
    ("selected", "fg:ansiblue bold"),
])

if __name__ == "__main__":
    clear()
    type_out_banner()
    print_banner()
    print()

    questionary.text("Please enter your facebook email:", style=terminal_blue_style).ask()
    
    clear()
    print_banner()
    print()

    questionary.password("Please enter your facebook password:", style=terminal_blue_style).ask()
    
    clear()
    print_banner()
    print()

    questionary.text("How many posts do you want to make?", style=terminal_blue_style).ask()
