from langchain import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.llms import OpenAI


def generate_band_name_and_hit_single(artists):
    llm = OpenAI(temperature=0.9)

    template = "What is a good name for a band that makes music similar to {artists}?"

    name_prompt = PromptTemplate(
        input_variables=["artists"],
        template=template,
    )

    name_chain = LLMChain(llm=llm, prompt=name_prompt)

    hit_single_prompt = PromptTemplate(
        input_variables=["band_name"],
        template="Write a catchy title for a hit single by the following band: {band_name}",
    )

    hit_single_chain = LLMChain(llm=llm, prompt=hit_single_prompt)

    # Combine the first and the second chain
    overall_chain = SimpleSequentialChain(
        chains=[name_chain, hit_single_chain], verbose=True
    )

    # Run the chain specifying only the input variable for the first chain.
    hit_single = overall_chain.run(artists)
    return hit_single
