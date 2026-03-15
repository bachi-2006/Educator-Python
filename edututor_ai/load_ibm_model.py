import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

model_path = "ibm-granite/granite-3.3-8b-instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

prompt = "Who are you?"
encoded = tokenizer(prompt, return_tensors="pt").to(device)

set_seed(42)
output = model.generate(
    input_ids=encoded.input_ids,
    attention_mask=encoded.attention_mask,
    max_new_tokens=100,
)

prediction = tokenizer.decode(output[0, encoded.input_ids.shape[1]:], skip_special_tokens=True)
print("Response:", prediction)
