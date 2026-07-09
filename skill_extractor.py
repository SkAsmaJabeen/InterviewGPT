SKILLS = [
    "python",
    "c programming"
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "langchain",
    "rag",
    "openai",
    "java",
    "streamlit",
    "chromadb",
    "huggingface",
    "docker",
    "git",
    "github",
    "linux",
    "networking",
    "cybersecurity",
    "flask",
    "fastapi",
    "redis",
    "mongodb",
    "mysql",
    "postgresql",
    "aws",
    "azure"
]

def extract_skills(text):

    found = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))