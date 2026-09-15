#!/usr/bin/env python3

import sys
import typing


def read_ancient_text(filename: str) -> str | None:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")
    fragment: typing.TextIO | None = None
    try:
        fragment = open(filename, "r")
        content: str = fragment.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
        return content
    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
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
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    user_filename = sys.stdin.readline().strip()
    if user_filename:
        print(f"Saving data to '{user_filename}'")
        file: typing.TextIO | None = None
        try:
            file = open(user_filename, "w")
            file.write(new_content)
            file.flush()
            print(f"Data saved in file '{user_filename}'.")
        except OSError as e:
            print(f"[STDERR] Error saving file '{user_filename}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
        finally:
            if file is not None and not file.closed:
                file.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_ancient_text.py <file>\n")
    else:
        content = read_ancient_text(sys.argv[1])
        if content is not None:
            new_protocol(content)
