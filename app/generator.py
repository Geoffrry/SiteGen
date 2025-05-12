import subprocess
import os
import zipfile

def prompt_llm(business_name, business_type):
    prompt = (
        f"Create a modern responsive website for a {business_type} business named {business_name}. "
        "Include a hero section, services, about, and contact form and anything else necessary. Use HTML and TailwindCSS only. search for an example of the similiar succesfull website"
    )
    result = subprocess.run(
        ["ollama", "run", "deepseek-coder", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout

def generate_website(name, btype, output_path):
    content = prompt_llm(name, btype)
    folder = output_path.replace(".zip", "")
    os.makedirs(folder, exist_ok=True)

    # Save to index.html (basic, parse can be improved later)
    with open(f"{folder}/index.html", "w") as f:
        f.write(content)

    # Create zip
    with zipfile.ZipFile(output_path, "w") as zipf:
        zipf.write(f"{folder}/index.html", arcname="index.html")
