import os
from os import path as p

if not "README.md" in os.listdir():
  with open("README.md", "w+") as f:
    f.write("<!-- CHANGELOG -->\n\n<!-- CHANGELOG -->")
  exit()
  
with open ("README.md", "r") as f:
  text = f.read()


changelog_text = text.split("<!-- CHANGELOG -->")[1]
print(changelog_text)
