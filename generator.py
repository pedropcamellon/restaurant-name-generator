from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import ValidationError

load_dotenv()


def get_llm_instance():
    llm = None

    try:
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1)

    except Exception as e:
        if "Your default credentials were not found" in str(e):
            print("Error: Please set the GOOGLE_API_KEY environment variable.")

    if llm is not None:
        return llm


def generate_restaurant_name(cuisine: str) -> str:
    llm = get_llm_instance()

    if llm is None:
        return "Error: Please set the GOOGLE_API_KEY environment variable."

    system_template = "I want to open a restaurant. Suggest a good restaurant name based on the cuisine provided by the user. Response must include only the name of the restaurant."

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "Cuisine: {cuisine}")]
    )

    prompt = prompt_template.invoke({"cuisine": cuisine})

    try:
        response = llm.invoke(prompt)

    except ValidationError as e:
        # If api key is invalid or missing tell the user
        # Get e message
        if "GOOGLE_API_KEY" in str(e):
            return "Error: Please set the GOOGLE_API_KEY environment variable."

    print(f"Restaurant Name: {response.content}")

    return response.content
