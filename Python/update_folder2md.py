import os
import argparse

def create_folder_tree_structure(folder_path, markdown_file, existing_structure, indent=''):
    markdown_file.write(f"{indent}+ {os.path.basename(folder_path)}\n")
    indent += '   '

    for item in sorted(os.listdir(folder_path)):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            create_folder_tree_structure(item_path, markdown_file, existing_structure, indent)
        elif os.path.isfile(item_path):
            file_link = f"[{item}]({os.path.abspath(item_path)})"
            if file_link not in existing_structure:
                markdown_file.write(f"{indent}- {file_link}\n")
            existing_structure.discard(file_link)

def update_folder_tree(folder_path, md_file):
    existing_structure = set()

    # Read existing Markdown file to get current structure
    with open(md_file, 'r') as existing_md:
        lines = existing_md.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('+') or line.startswith('-'):
                existing_structure.add(line)

    with open(md_file, 'w') as markdown_file:
        create_folder_tree_structure(folder_path, markdown_file, existing_structure)

        # Write any remaining files that were removed
        for remaining_file in existing_structure:
            markdown_file.write(f"{remaining_file}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update folder tree structure in Markdown')
    parser.add_argument('folder_path', type=str, help='Path to the folder')
    parser.add_argument('md_file', type=str, help='Path to the Markdown file')
    args = parser.parse_args()

    folder_path = args.folder_path
    md_file = args.md_file

    update_folder_tree(folder_path, md_file)
