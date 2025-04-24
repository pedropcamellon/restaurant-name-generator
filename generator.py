from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", convert_system_message_to_human=True, temperature=1
)


def generate_restaurant_name(cuisine: str) -> str:
    system_template = "I want to open a restaurant. Suggest a good restaurant name based on the cuisine provided by the user. Response must include only the name of the restaurant."

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "Cuisine: {cuisine}")]
    )

    prompt = prompt_template.invoke({"cuisine": cuisine})

    response = llm.invoke(prompt)

    print(f"Restaurant Name: {response.content}")

    return response.content
