import streamlit as st
from ai_module_ibm import EdututorAIIBM
import streamlit as st

def main():
    st.title("EduTutor AI - Personalized Learning Assistant")

    menu = ["Student", "Teacher"]
    choice = st.sidebar.selectbox("Select User Type", menu)

    edututor_ai = EdututorAIIBM()

    if choice == "Student":
        st.header("Student Interface")
        question = st.text_input("Ask your question or request learning content:")
        if st.button("Get Response"):
            if question:
                response = edututor_ai.get_student_response(question)
                st.write(response)
            else:
                st.warning("Please enter a question or request.")
    else:
        st.header("Teacher Interface")
        st.write("Upload assignments and get automated grading and feedback.")
        uploaded_file = st.file_uploader("Upload student assignment (text file)", type=["txt"])
        if uploaded_file is not None:
            content = uploaded_file.read().decode("utf-8")
            grade, feedback = edututor_ai.grade_assignment(content)
            st.write(f"Grade: {grade}")
            st.write(f"Feedback: {feedback}")

if __name__ == "__main__":
    main()
