#!/usr/bin/env python3

def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
                print("
            return (True, data)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "'Content successfully written to file'")
        return (False, f"Invalid action '{action}'. Use 'read' or 'write'.")
    except OSError as e:
        return (False, str(e))



if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    no_result = secure_archive("/not/existing/file", "read")
    print(no_result)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    inaccessible_result = secure_archive("/etc/master.passwd", "read")
    print(inaccessible_result)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    ok_result = secure_archive("ancient_fragment.txt", "read")
    print(ok_result)
    print()
    if ok_result[0]:
        print("Using 'secure_archive' to write previous content to a new"
              "file:")
        write_result = secure_archive("backup_fragment.txt", "write",
                                      ok_result[1])
        print(write_result)
