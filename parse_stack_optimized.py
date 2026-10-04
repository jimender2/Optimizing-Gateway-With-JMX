import csv
import sys

def process_and_print_optimized(filename):
    """
    Optimized O(n) parser. Instead of looking backward,
    we keep track of the current nesting level in a stack.
    """
    current_stack = []

    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers

        for row in reader:
            if not row: continue

            call = row[0]
            call_strip = call.strip()

            # Skip noise
            if call_strip == "Self time" or not call_strip:
                continue

            # Clean hits/time
            try:
                # Hits is column index 3 (0-based)
                hits = row[3].replace(",", "").strip()
            except IndexError:
                continue

            # Calculate indentation level (VisualVM usually uses 2 spaces per level)
            leading_spaces = len(call) - len(call.lstrip())
            depth = leading_spaces // 2 # Adjust if your indent isn't 2 spaces

            # POP: If current stack is deeper than current row, truncate it
            current_stack = current_stack[:depth]

            # PUSH: Add current call to stack
            current_stack.append(call_strip)

            # PRINT: Output in collapsed format immediately to save memory
            if hits.isdigit() and int(hits) > 0:
                print(f"{';'.join(current_stack)} {hits}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_stack.py <path_to_csv>")
        return
    process_and_print_optimized(sys.argv[1])

if __name__ == "__main__":
    main()