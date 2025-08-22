import os
import shutil
import re
import requests

def move_jpg_files():
    source_folder = input("Enter source folder path: ")
    destination_folder = input("Enter destination folder path: ")

    os.makedirs(destination_folder, exist_ok=True)

    count = 0
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):
            shutil.move(os.path.join(source_folder, file_name),
                        os.path.join(destination_folder, file_name))
            count += 1
    print(f"✅ {count} JPG files moved successfully!")


def extract_emails():
    input_file = input("Enter path of .txt file: ")
    output_file = input("Enter output file name (e.g., emails.txt): ")

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}', text)

    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"✅ {len(emails)} emails extracted and saved to {output_file}")


def scrape_webpage_title():
    url = input("Enter webpage URL: ")
    output_file = input("Enter output file name (e.g., title.txt): ")

    response = requests.get(url)
    html_content = response.text

    match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(title)
        print(f"✅ Title saved to {output_file}: {title}")
    else:
        print("❌ No title found on the webpage.")


def main():
    print("\n=== Python Task Automation ===")
    print("1. Move all .jpg files from one folder to another")
    print("2. Extract all emails from a .txt file")
    print("3. Scrape the title of a webpage")
    choice = input("Choose a task (1/2/3): ")

    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        scrape_webpage_title()
    else:
        print("❌ Invalid choice!")


if __name__ == "_main_":
    main()