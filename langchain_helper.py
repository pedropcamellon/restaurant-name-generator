from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from typing import Dict

load_dotenv()

llm = HuggingFaceHub(repo_id="google/flan-t5-xxl")


def generate_restaurant_name_and_items(cuisine: str) -> Dict[str, str]:
    restaurant_name_prompt_template = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} cuisine. Suggest a good restaurant name.",
    )

    restaurant_name_chain = LLMChain(
        prompt=restaurant_name_prompt_template,
        llm=llm,
        output_key="restaurant_name",
        verbose=True,
    )

    food_items_prompt_template = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest three items to include in a menu for a restaurant called {restaurant_name}. Return the items as comma separated list",
    )

    food_items_chain = LLMChain(
        llm=llm,
        output_key="food_items",
        prompt=food_items_prompt_template,
        verbose=True,
    )

    seq_chain = SequentialChain(
        chains=[restaurant_name_chain, food_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "food_items"],
        verbose=True,
    )

    response = seq_chain({"cuisine": cuisine})

    return response
