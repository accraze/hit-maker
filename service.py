from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

template = "What is a good name for a band that makes music similar to {artists} and is influenced by {influences}?"

name_prompt = PromptTemplate(
    input_variables=["artists", "influences"],
    template=template,
)

name_chain = LLMChain(llm=llm, prompt=name_prompt)

name = name_chain.run(
    artists="lee scratch perry meets merzbow with the velvet underground",
    influences="the movie metropolis",
)


print(name)
