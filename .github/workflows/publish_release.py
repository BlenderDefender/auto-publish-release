import os
from os import path as p

if not "README.md" in os.listdir():
  with open("README.md", "w+") as f:
    f.write("<!-- CHANGELOG -->\n\n<!-- CHANGELOG -->")
  exit()
  
with open("README.md", "r") as f:
  text = f.read()


changelog_text = text.split("<!-- CHANGELOG -->")[1]

prev_text = ""
if "CHANGELOG.md" in os.listdir():
  with open("CHANGELOG.md", "r") as f:
    prev_text = f.read()

final_text = f"""## Version 
{changelog_text}

{prev_text}
"""

with open("CHANGELOG.md", "w+") as f:
  f.write(final_text)
  
print(final_text)
