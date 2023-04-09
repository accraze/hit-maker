from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

text = "What would be a good band name for a group that makes music similar to lee scratch perry and merzbow?"
print(llm(text))
