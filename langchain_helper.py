from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


def generate_restaurant_name_and_items(cuisine: str) -> dict[str, str]:
    restaurant_name_prompt_template = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} cuisine. Suggest a good restaurant name. Response must include only the name of the restaurant.",
    )

    restaurant_name_chain = LLMChain(
        prompt=restaurant_name_prompt_template,
        llm=llm,
        output_key="restaurant_name",
        verbose=True,
    )

    food_items_prompt_template = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Provide three items as comma separated list to include in a menu for a restaurant called {restaurant_name}. Response must include only the items.",
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
