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
    type=["pdf"],
    key="resume_pdf"
)

if resume is not None:

    resume_bytes = resume.getvalue()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(resume_bytes)
        resume_path = tmp.name

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
            "If the preview doesn't load in your browser, use the Download Resume button below."
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

st.header("📚 Upload Interview Questions PDF")
interview_pdf = st.file_uploader(
    "Upload Interview Questions PDF",
    type=["pdf"],
    key="interview_pdf"
)

if interview_pdf is not None:

    pdf_bytes = interview_pdf.getvalue()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(pdf_bytes)
        pdf_path = tmp.name

    st.success(
        "Interview Questions PDF Uploaded Successfully"
    )

    questions_pdf = base64.b64encode(
        pdf_bytes
    ).decode()

    questions_display = f"""
    <iframe
        src="data:application/pdf;base64,{questions_pdf}"
        width="100%"
        height="550"
        type="application/pdf">
    </iframe>
    """

    with st.expander(
        "📖 Interview Questions Preview",
        expanded=False
    ):

        st.info(
            "If the preview doesn't load in your browser, use the Download button below."
        )

        st.markdown(
            questions_display,
            unsafe_allow_html=True
        )

    st.download_button(
        "📥 Download Interview Questions PDF",
        data=pdf_bytes,
        file_name=interview_pdf.name,
        mime="application/pdf",
        use_container_width=True
    )

    if st.button(
        "Generate Interview Question",
        use_container_width=True
    ):

        with st.spinner(
            "Generating Interview Question..."
        ):

            vectordb = create_vector_store(
                pdf_path
            )

            question = generate_question(
                vectordb
            )

            st.session_state.question = question

        st.success(
            "Interview Question Generated Successfully!"
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

    col1, col2 = st.columns([3, 1])

    with col1:

        evaluate = st.button(
            "Evaluate Answer",
            use_container_width=True
        )

    with col2:

        clear = st.button(
            "Clear",
            use_container_width=True
        )

    if clear:

        st.session_state.pop("question", None)
        st.session_state.pop("feedback", None)
        st.rerun()

    if evaluate:

        if not answer.strip():

            st.warning(
                "Please enter your answer before evaluation."
            )

        else:

            with st.spinner(
                "Evaluating your answer..."
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

st.markdown(
    """
    <div style="text-align:center;
                color:gray;
                font-size:15px;
                padding-top:20px;
                padding-bottom:10px;">
        InterviewGPT | Resume Analysis | RAG | Groq
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

st.markdown(
    """
    <style>

    div.stButton > button {
        border-radius: 10px;
        height: 3em;
        font-size: 16px;
        font-weight: 600;
    }

    div[data-testid="stExpander"] {
        border-radius: 10px;
    }

    textarea {
        border-radius: 10px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)
