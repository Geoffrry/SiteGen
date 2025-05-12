import subprocess
import os
import zipfile

def prompt_llm(business_name, business_type):
    prompt = f"""
    You are a frontend web developer.

    Generate a complete and well-structured one-page responsive website for a {business_type} called "{business_name}" using only pure HTML with TailwindCSS. 

    The site should include:
    - A hero section with heading and CTA
    - Services or features section
    - About us section
    - Contact form

    Requirements:
    - Use semantic HTML5
    - Use only TailwindCSS utility classes (no inline styles or other frameworks)
    - Output only raw HTML without triple backticks, markdown, or explanation.
    - Do not mention that you are an AI or that you're limited.
    - Your response should be fully usable as `index.html`.

    Respond with HTML only.
    """
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
    
    return content