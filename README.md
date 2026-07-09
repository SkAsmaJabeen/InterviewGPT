# InterviewGPT

InterviewGPT is an AI-powered interview preparation application that helps users practice technical interviews in an interactive way. It analyzes a candidate's resume, identifies technical skills, generates interview questions using Retrieval-Augmented Generation (RAG), and evaluates responses using a Large Language Model (LLM).

Building this project gave me hands-on experience with Retrieval-Augmented Generation (RAG), vector databases, prompt engineering, and integrating Large Language Models into a real-world application. It also strengthened my understanding of LangChain, ChromaDB, Streamlit, and AI-powered application development.

This project was developed as part of my **Gen AI with Prompt Engineering Internship** conducted by **Datavalley India Pvt. Ltd.** in collaboration with **APSCHE**.

---

## Features

- Upload and preview resumes
- Extract technical skills from resumes
- Upload an interview questions PDF
- Generate interview questions using Retrieval-Augmented Generation (RAG)
- Evaluate answers using Groq LLM
- Receive detailed feedback, strengths, weaknesses, and suggestions for improvement
- Simple and responsive Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Groq (Llama 3.3)
- PDFPlumber

---

## Project Structure

```
InterviewGPT/
│── app.py
│── rag.py
│── evaluator.py
│── resume_parser.py
│── skill_extractor.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SkAsmaJabeen/InterviewGPT.git
cd InterviewGPT
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## How It Works

1. Upload a resume in PDF format.
2. The application extracts the resume text and identifies technical skills.
3. Upload an interview questions PDF.
4. The RAG pipeline retrieves relevant interview questions.
5. Answer the generated interview question.
6. The application evaluates the answer using Groq LLM and provides detailed feedback.

---

## Future Improvements

- Generate interview questions directly from detected resume skills
- Support multiple interview domains
- Store interview history and performance
- Add voice-based interview practice
- Deploy the application online

---

## Acknowledgements

This project was developed as part of the **Gen AI with Prompt Engineering Internship** organized by **Datavalley India Pvt. Ltd.** in collaboration with **APSCHE**.

Special thanks to the teams behind:

- Streamlit
- LangChain
- ChromaDB
- Hugging Face
- Groq

---

## License

This project is intended for learning and educational purposes.