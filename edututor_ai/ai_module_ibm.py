import pandas as pd
import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed

class EdututorAIIBM:
    def __init__(self):
        model_path = "ibm-granite/granite-3.3-8b-instruct"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        try:
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                device_map=self.device,
                torch_dtype=torch.bfloat16 if self.device == "cuda" else torch.float32,
            )
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        except Exception as e:
            print(f"Error loading model or tokenizer: {e}")
            self.model = None
            self.tokenizer = None

    def generate_response(self, prompt: str) -> str:
        if self.model is None or self.tokenizer is None:
            return "Model or tokenizer not loaded properly."

        try:
            # Tokenize with attention mask to fix warning
            encoded = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(self.device)
            input_ids = encoded.input_ids
            attention_mask = encoded.attention_mask

            set_seed(42)
            output = self.model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_new_tokens=8192,
            )
            prediction = self.tokenizer.decode(output[0, input_ids.shape[1]:], skip_special_tokens=True)
            return prediction
        except Exception as e:
            return f"Error during generation: {e}"

    def get_student_response(self, query: str) -> str:
        prompt = f"Provide a personalized educational response to the following student query:\n{query}"
        return self.generate_response(prompt)

    def grade_assignment(self, assignment_text: str) -> (str, str):
        prompt = f"Grade the following student assignment and provide constructive feedback:\n{assignment_text}"
        feedback = self.generate_response(prompt)
        grade = "A" if "excellent" in feedback.lower() else "B"
        return grade, feedback
