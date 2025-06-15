"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove trailing newline
            parts = line.split(',')  # Split into [subject, lecturer, number as string]
            parts[2] = int(parts[2])  # Convert number to integer
            data.append(parts)  # Add to list
    return data

main()