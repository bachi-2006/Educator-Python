from google import genai

class EdututorAIGemini:
    def __init__(self):
        self.client = genai.Client(api_key="AIzaSyBgl-L1XzFr62P4L_XYAn1qcSVPhOoV-ms")

    def generate_response(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )
        return response.text

    def get_student_response(self, query: str) -> str:
        prompt = f"Provide a personalized educational response to the following student query:\n{query}"
        return self.generate_response(prompt)

    def grade_assignment(self, assignment_text: str) -> (str, str):
        prompt = f"Grade the following student assignment and provide constructive feedback:\n{assignment_text}"
        feedback = self.generate_response(prompt)
        grade = "A" if "excellent" in feedback.lower() else "B"
        return grade, feedback
