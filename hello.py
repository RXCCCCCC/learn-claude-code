"""Hello World module.

A simple module that demonstrates basic Python structure with type hints,
docstrings, and proper module initialization.
"""


def greet() -> None:
    """Print a greeting message to the console.

    This function outputs a simple "Hello, World!" message.
    """
    print("Hello, World!")


def main() -> None:
    """Entry point for the script when run directly.

    Calls the greet function to display the greeting.
    """
    greet()


if __name__ == "__main__":
    main()
