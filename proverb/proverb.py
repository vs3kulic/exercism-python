"""This module demonstrates a solution for the Proverb exercise."""

def proverb(*item: str, qualifier=None) -> list[str]:
    """Return a proverb as a list of strings.
    
    param item: a variable number of string arguments representing items in the proverb.
    param qualifier: an optional string to qualify the first item in the final line.
    return: a list of strings representing the lines of the proverb.
    """
    lines = [f"For want of a {a} the {b} was lost." for a, b in zip(item, item[1:])]

    if len(item) != 0:
        last = item[0] if qualifier is None else f"{qualifier} {item[0]}"
        lines.append(f"And all for the want of a {last}.")

    return lines

def main():
    """Main function to demonstrate the proverb function."""
    items = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
    my_proverb = proverb(*items, qualifier="horseshoe")
    print("\n".join(my_proverb))

if __name__ == "__main__":
    main()
