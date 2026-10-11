from textnode import TextNode, TextType
from htmlnode import HTMLNode
from block_markdown import markdown_to_html_node
import os
import shutil
import sys



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            #item_path = item_path[:-2] + "html"
            generate_page(item_path, template_path, dest_dir_path, basepath)
        else:
            new_dist_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, new_dist_path)
def main():
    # Check if a command-line argument was provided
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    print(f"Basepath is set to: {basepath}")
    
    target_folder = "/home/anes/boots/static_site"
    
    if not os.path.exists(target_folder):
        raise Exception("path doesn t exists")
    public_folder = os.path.join(target_folder, "public")
    static_folder = os.path.join(target_folder, "static")
    
    if not os.path.exists(public_folder)  or not os.path.exists(static_folder) :
        raise Exception("static or public folder doesn t exists")
    shutil.rmtree(public_folder)
    os.mkdir(public_folder)
    static_files = os.listdir(static_folder)
    recursion(static_folder, static_files, public_folder)
    content_folder = os.path.join(target_folder, "content")
    template_path = os.path.join(target_folder,"template.html")
    generate_pages_recursive(content_folder, template_path, public_folder, basepath)
    
def recursion(target_folder, static_files, public_folder):
    for file in static_files:
        file_path = os.path.join(target_folder, file)
        dest_path = os.path.join(public_folder, file)
        
        if os.path.isfile(file_path):
            shutil.copy(file_path, public_folder)
            
        else:
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            recursion(file_path, os.listdir(file_path), dest_path)

def extract_title(markdown):
    sections = markdown.split("\n")
    
    for section in sections:
        if section.startswith("# "):
            return section[2:].strip()
    raise Exception ("there is no header")

def generate_page(from_path, template_path, dest_path, basepath):
    dest_path = os.path.join(dest_path, "index.html")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
    
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}",title)
    final_html = final_html.replace("{{ Content }}", html_content)
    final_html = final_html.replace("href="/", href="{basepath})
    final_html = final_html.replace("src="/", src="{basepath})
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(final_html)


    


if __name__ == "__main__":
    main()