#!/usr/bin/env python3

import sys
import typing


def read_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    fragment: typing.TextIO | None = None
    try:
        fragment = open(filename, "r")
        content: str = fragment.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if fragment is not None and not fragment.closed:
            fragment.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        read_ancient_text(sys.argv[1])
