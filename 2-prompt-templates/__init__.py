import os

from langchain import OpenAI
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(input_variables=["organism"], template="What is a good pet name for this {organism}?", )

formatted_prompt = prompt.format(organism='polar bear')

print(formatted_prompt)

output = llm(formatted_prompt)

print(output)
