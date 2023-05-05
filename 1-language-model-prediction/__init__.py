from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0.9)

text = "What would be a good pet name for this cat?"
print(llm(text))
