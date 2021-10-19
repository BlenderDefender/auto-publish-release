import argparse

import os
from os import path as p

# Process commit message.
parser = argparse.ArgumentParser()
parser.add_argument("--commit_message")
args = parser.parse_args()

# Extract the version from the commit message.
commit_message = args.commit_message
version_raw = commit_message.split("#RELEASE")[1]
print(version_raw)
# version = version_raw.replace(".", "_")

# Create a README, if it doesn't exist already.
if not "README.md" in os.listdir():
  with open("README.md", "w+") as f:
    f.write("<!-- CHANGELOG -->\n\n<!-- CHANGELOG -->")
  exit()
  
# Get the content of the README file.
with open("README.md", "r") as f:
  text = f.read()

changelog_text = text.split("<!-- CHANGELOG -->")[1]

prev_text = ""
if "CHANGELOG.md" in os.listdir():
  with open("CHANGELOG.md", "r") as f:
    prev_text = f.read()

final_text = f"""## Version {version_raw}
{changelog_text}

{prev_text}
"""

with open("CHANGELOG.md", "w+") as f:
  f.write(final_text)
  
print(final_text)
