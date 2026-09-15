#!/usr/bin/env python3

import sys
import typing


def read_ancient_text(filename: str) -> str | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    fragment: typing.TextIO | None = None
    try:
        fragment = open(filename, "r")
        content: str = fragment.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
        return content
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    finally:
        if fragment is not None and not fragment.closed:
            fragment.close()
            print(f"File '{filename}' closed.")


def new_protocol(content: str) -> None:
    print("\nTransform data:")
    lines = content.splitlines()
    format_lines = [line + "#" for line in lines]
    new_content = "\n".join(format_lines) + "\n"
    print("---")
    print(new_content, end="")
    print("---")
    user_filename = input("Enter new file name (or empty): ")
    if user_filename:
        print(f"Saving data to '{user_filename}'")
        file: typing.TextIO | None = None
        try:
            file = open(user_filename, "w")
            file.write(new_content)
            print(f"Data saved in file '{user_filename}'.")
        except OSError as e:
            print(f"Error saving file '{user_filename}': {e}")
        finally:
            if file is not None and not file.closed:
                file.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        content = read_ancient_text(sys.argv[1])
        if content is not None:
            new_protocol(content)
