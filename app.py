import base64
import tempfile
import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from rag import create_vector_store, generate_question
from evaluator import evaluate_answer

st.set_page_config(
    page_title="InterviewGPT",
    page_icon="🤖",
    layout="wide"
)
st.markdown(
    """
    <h1 style="text-align:center;">
        🤖 InterviewGPT
    </h1>

    <p style="text-align:center;
              font-size:20px;
              color:gray;">
        AI Interview Coach using RAG + Groq
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.header("📄 Upload Resume")

resume = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if resume is not None:

    resume_bytes = resume.getvalue()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(pdf_bytes)
        pdf_path = tmp.name
        
    with st.spinner("Parsing Resume..."):

        resume_text = extract_resume_text(
            resume_path
        )

        st.success("Resume Uploaded Successfully")

    resume_pdf = base64.b64encode(
        resume_bytes
    ).decode()

    resume_display = f"""
        <iframe
            src="data:application/pdf;base64,{resume_pdf}"
            width="100%"
            height="550"
            type="application/pdf">
        </iframe>
        """

    with st.expander(
        "📄 Resume Preview",
        expanded=True
    ):

        st.info(
            "If the preview doesn't load in your browser, click the Download Resume button below."
        )

        st.markdown(
            resume_display,
            unsafe_allow_html=True
        )

    st.download_button(
        "📥 Download Resume",
        data=resume_bytes,
        file_name=resume.name,
        mime="application/pdf",
        use_container_width=True
    )

    st.subheader("Detected Skills")

    skills = extract_skills(
        resume_text
    )

    if skills:

        st.info("### 🛠️ Skills Detected")

        cols = st.columns(2)

        for i, skill in enumerate(skills):

            with cols[i % 2]:

                st.success(
                    skill.title()
                )

    else:

        st.warning(
            "No skills detected."
        )

st.divider()
if "question" in st.session_state:

    st.header("🎤 Interview Question")

    st.info(
        st.session_state.question
    )

    answer = st.text_area(
        "Enter Your Answer",
        height=220,
        placeholder="Write your answer here..."
    )

    if st.button(
        "Evaluate Answer",
        use_container_width=True
    ):

        if answer.strip() == "":

            st.warning(
                "Please enter your answer."
            )

        else:

            with st.spinner(
                "Evaluating Answer..."
            ):

                feedback = evaluate_answer(
                    st.session_state.question,
                    answer
                )

                st.session_state.feedback = feedback

if "feedback" in st.session_state:

    st.divider()

    st.header("📊 Interview Evaluation")

    with st.expander(
        "View Detailed Feedback",
        expanded=True
    ):

        st.markdown(
            st.session_state.feedback
        )

st.divider()
st.markdown(
    """
    <style>

    div.stButton > button {
        border-radius: 12px;
        height: 3em;
        font-weight: 600;
    }

    div[data-testid="stExpander"] {
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <hr style="margin-top:40px;margin-bottom:15px;">
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:gray;
        font-size:15px;
    ">
        🤖 InterviewGPT | Resume Analysis | RAG | Groq
    </p>
    """,
    unsafe_allow_html=True
)