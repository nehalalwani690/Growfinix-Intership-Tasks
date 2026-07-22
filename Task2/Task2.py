#Task 2: CLI Log Parser for Tour Enquiriesp

import argparse
import re

def parse_enquiries(file_path):
    # Regex patterns
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
    name_pattern = re.compile(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\b')
    destination_pattern = re.compile(r'\b(?:Paris|London|New York|Tokyo|Delhi|Sydney|Rome)\b', re.IGNORECASE)

    results = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            emails = email_pattern.findall(line)
            names = name_pattern.findall(line)
            destinations = destination_pattern.findall(line)

            if emails or names or destinations:
                results.append({
                    "names": names,
                    "emails": emails,
                    "destinations": destinations
                })

    return results

def main():
    parser = argparse.ArgumentParser(description="CLI Log Parser for Tour Enquiries")
    parser.add_argument("file", help="Path to the raw tour enquiries text file")
    args = parser.parse_args()

    parsed_data = parse_enquiries(args.file)

    print("\n--- Tour Enquiries Summary ---\n")
    for idx, entry in enumerate(parsed_data, 1):
        print(f"Entry {idx}:")
        if entry["names"]:
            print(f"  Names: {', '.join(entry['names'])}")
        if entry["emails"]:
            print(f"  Emails: {', '.join(entry['emails'])}")
        if entry["destinations"]:
            print(f"  Destinations: {', '.join(entry['destinations'])}")
        print()

if __name__ == "__main__":
    main()
