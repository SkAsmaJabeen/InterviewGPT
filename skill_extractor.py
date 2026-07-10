SKILLS = [
    "Python", "Java", "C", "C++", "C#", "Go", "Rust", "JavaScript", "TypeScript",
    "HTML", "CSS", "Bootstrap", "React", "Angular", "Vue.js", "Node.js",
    "Express.js", "Django", "Flask", "FastAPI", "Spring Boot",

    "SQL", "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle", "Redis",

    "Git", "GitHub", "GitLab", "Linux", "Ubuntu", "Windows Server",
    "Docker", "Kubernetes", "Jenkins", "CI/CD"k, "DevOps",

    "AWS", "Azure", "Google Cloud", "Cloud Computing",

    "REST API", "GraphQL", "Microservices",

    "Data Structures", "Algorithms", "Object Oriented Programming", "OOP",
    "Operating Systems", "Computer Networks", "DBMS", "Software Engineering",

    "Machine Learning", "Deep Learning", "Artificial Intelligence",
    "Generative AI", "LLM", "Prompt Engineering",
    "LangChain", "RAG", "Vector Database", "ChromaDB",
    "TensorFlow", "PyTorch", "Scikit-learn",
    "OpenCV", "NLP", "Computer Vision",
    "Pandas", "NumPy", "Matplotlib", "Power BI", "Tableau",

    "Cybersecurity", "Ethical Hacking", "Penetration Testing",
    "Network Security", "Cryptography", "Digital Forensics",
    "OWASP", "Wireshark", "Burp Suite", "Nmap",
    "Metasploit", "Kali Linux",

    "Embedded Systems", "Microcontrollers", "Arduino",
    "Raspberry Pi", "FPGA", "VLSI", "Verilog", "VHDL",
    "8051", "ARM", "IoT", "PCB Design",
    "Digital Electronics", "Analog Electronics",
    "Signal Processing", "Communication Systems",

    "Power Systems", "Power Electronics",
    "Electrical Machines", "Control Systems",
    "PLC", "SCADA", "Industrial Automation",
    "Renewable Energy", "Motor Drives",

    "AutoCAD", "SolidWorks", "CATIA", "Fusion 360",
    "ANSYS", "MATLAB", "Simulink",
    "Machine Design", "Manufacturing",
    "Fluid Mechanics", "Thermodynamics",
    "Heat Transfer", "Robotics", "CNC",
    "HVAC", "Finite Element Analysis", "GD&T",

    "STAAD Pro", "ETABS", "Revit",
    "Structural Analysis", "Construction Management",
    "Surveying", "Quantity Surveying",
    "Concrete Technology", "Geotechnical Engineering",
    "Transportation Engineering", "Building Design",

    "Chemical Process Design", "Aspen Plus",
    "HYSYS", "Reaction Engineering",
    "Mass Transfer", "Process Control",
    "Plant Design",

    "Molecular Biology", "Genetics", "PCR",
    "Cell Culture", "Bioinformatics",
    "DNA Sequencing", "Protein Engineering",
    "CRISPR", "Microbiology", "Biochemistry",

    "Biomedical Instrumentation",
    "Medical Imaging", "Medical Devices",
    "Healthcare Analytics",

    "Anatomy", "Physiology", "Pathology",
    "Pharmacology", "General Medicine",
    "General Surgery", "Pediatrics",
    "Gynecology", "Obstetrics",
    "Cardiology", "Neurology",
    "Orthopedics", "Dermatology",
    "Radiology", "Psychiatry",
    "Emergency Medicine",
    "Clinical Research", "Patient Care",
    "Medical Ethics",

    "Clinical Nursing", "Critical Care",
    "ICU", "Emergency Care",
    "Medication Administration",
    "Vital Signs Monitoring",
    "Infection Control", "First Aid",
    "BLS", "ACLS",

    "Clinical Pharmacy", "Hospital Pharmacy",
    "Drug Formulation",
    "Medicinal Chemistry",
    "Pharmaceutical Analysis",
    "Quality Assurance",
    "Quality Control",
    "Regulatory Affairs",
    "Pharmacovigilance",

    "Oral Surgery", "Endodontics",
    "Orthodontics", "Periodontics",
    "Prosthodontics", "Oral Medicine",
    "Dental Radiology",
    "Restorative Dentistry",
    "Pediatric Dentistry"
]

import re

def extract_skills(text):

    found = []

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    for skill in SKILLS:

        if skill.lower() in text:

            found.append(skill)

    return sorted(set(found))