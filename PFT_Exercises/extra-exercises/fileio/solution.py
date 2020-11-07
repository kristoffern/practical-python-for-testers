import sys
import os.path


def get_nonblank_lines(filename):
    """Read and return all nonblank lines from the file 
    identified by filename"""

    with open(filename, "rt") as source:
        lines = []
        for line in source:
            if line.strip():
                lines.append(line)
        return "".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Need a filename to load")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("%s does not exist" % (filename,))
        sys.exit(1)

    print(get_nonblank_lines(filename))
