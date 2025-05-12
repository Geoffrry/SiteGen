import subprocess
import os
import zipfile

def prompt_llm(business_name, business_type):
    prompt = (
        f"Generate a complete and well-structured responsive website for a {business_type} named '{business_name}'. "
        "The site must include a hero section, services, about section, and contact form. "
        "Use TailwindCSS for styling and write only clean HTML code in one file (index.html). "
        "Ensure semantic HTML, modern UX practices, and accessible layout. Do not include explanations—only raw HTML code."
    )
    result = subprocess.run(
        ["ollama", "run", "deepseek-coder", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def generate_website(name, btype, output_path):
    content = prompt_llm(name, btype)
    folder = output_path.replace(".zip", "")
    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/index.html", "w") as f:
        f.write(content)

    with zipfile.ZipFile(output_path, "w") as zipf:
        zipf.write(f"{folder}/index.html", arcname="index.html")