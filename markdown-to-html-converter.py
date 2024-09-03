import markdown
import sys

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)
    with open(output_file, 'w') as f:
        f.write(html)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py [input_markdown] [output_html]")
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_markdown_to_html(input_file, output_file)
    print(f"HTML content saved to {output_file}")

if __name__ == "__main__":
    main()
