import os
import argparse

def create_folder_tree_structure(folder_path, markdown_file, indent=''):
    markdown_file.write(f"{indent}+ {os.path.basename(folder_path)}\n")
    indent += '   '

    for item in sorted(os.listdir(folder_path)):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            create_folder_tree_structure(item_path, markdown_file, indent)
        elif os.path.isfile(item_path):
            markdown_file.write(f"{indent}- [{item}]({os.path.abspath(item_path)})\n")

def generate_folder_tree(folder_path):
    with open('folder_tree.md', 'w') as markdown_file:
        create_folder_tree_structure(folder_path, markdown_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create folder tree structure in Markdown')
    parser.add_argument('folder_path', type=str, help='Path to the folder')
    args = parser.parse_args()

    folder_path = args.folder_path
    generate_folder_tree(folder_path)
