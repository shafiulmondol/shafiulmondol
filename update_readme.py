import requests
import os

GITHUB_USERNAME = "shafiulmondol"
README_FILE = "README.md"

def get_top_languages():
    url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB_USERNAME}&layout=compact&langs_count=8&theme=transparent"
    return f'![Top Languages]({url})'

def update_readme():
    if not os.path.exists(README_FILE):
        print("README.md file not found!")
        return

    with open(README_FILE, "r", encoding="utf-8") as file:
        content = file.readlines()

    # Find where to update the README
    start_index = -1
    end_index = -1
    for i, line in enumerate(content):
        if "<!-- TOP_LANGUAGES_START -->" in line:
            start_index = i
        if "<!-- TOP_LANGUAGES_END -->" in line:
            end_index = i

    if start_index != -1 and end_index != -1:
        content[start_index + 1 : end_index] = [get_top_languages() + "\n"]

        with open(README_FILE, "w", encoding="utf-8") as file:
            file.writelines(content)

        print("README updated successfully!")
    else:
        print("TOP_LANGUAGES section not found in README.")

if __name__ == "__main__":
    update_readme()

