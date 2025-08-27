import re
import json

# Input and output files
log_file = "logs.log"
output_file = "parsed_logs.json"

# Regex pattern for parsing
pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* "(?P<method>GET|POST) (?P<url>.*?) HTTP.*" (?P<status>\d+)'
)

parsed_logs = []

# Read logs from file
with open(log_file, "r") as f:
    for line in f:
        match = pattern.match(line.strip())
        if match:
            parsed_logs.append(match.groupdict())

# Save structured data to JSON file
with open(output_file, "w") as f:
    json.dump(parsed_logs, f, indent=2)

print(f"Parsed logs saved to {output_file}")
