import markdown
import json
import argparse
import os
import re



def markdown_to_json(md_content):
    """
    Converts Markdown content to JSON with specific fields.

    Args:
        md_content (str): The Markdown content as a string.

    Returns:
        dict: A JSON representation of the Markdown content with specific fields.
    """
    # Split lines and remove markdown tags
    lines = md_content.splitlines()

# Check if there are at least 3 lines
    if len(lines) < 3:
        raise ValueError("The Markdown file must contain at least three lines for the titles.")

    # Extract titles using regex to remove Markdown heading tags
    titles = [re.sub(r'^#+\s*', '', line) for line in lines[:3]]
    ainu_title, jap_title, title = titles

    # Convert remaining lines to HTML
    content_lines = lines[3:] if len(lines) > 3 else []
    content_html = markdown.markdown("\n".join(content_lines))

    # Remove extra spaces before <br/> and </p> tags
    content_html = re.sub(r'\s+(<br\s*/>|</p>)', r'\1', content_html)

    # Create a JSON structure
    json_output = {
        "ainu_title": ainu_title,
        "jap_title": jap_title,
        "title": title,
        "content": content_html
    }

    return json_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to JSON with structured fields.")
    parser.add_argument("input_file", type=str, help="Path to the input Markdown file.")
    parser.add_argument("--output_file", type=str, help="Optional path to the output JSON file.")
    args = parser.parse_args()

    input_file = args.input_file
    if not os.path.isfile(input_file):
        print(f"Error: File {input_file} does not exist.")
        exit(1)

    output_file = args.output_file if args.output_file else os.path.splitext(input_file)[0] + ".json"

    with open(input_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    try:
        json_result = markdown_to_json(md_content)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_result, f, ensure_ascii=False, indent=4)

    print(f"Converted {input_file} to {output_file} with structured fields and HTML content")