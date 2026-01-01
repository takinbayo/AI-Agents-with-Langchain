from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
    Elon Musk is a visionary entrepreneur and business magnate who has made a significant impact on various industries, including technology, transportation, and energy. He is the CEO and CTO of SpaceX, the CEO and product architect of Tesla, Inc., and the CEO of Neuralink and The Boring Company. Musk's contributions have revolutionized the electric vehicle industry through Tesla, Inc., which has become one of the leading manufacturers of electric cars globally. He has also played a crucial role in advancing space exploration through SpaceX, with its successful launches and landings of rockets. Musk's vision for a sustainable future extends to renewable energy, with Tesla, Inc. leading the charge in electric power solutions. Additionally, he has been a pioneer in the field of artificial intelligence with Neuralink, aiming to enhance human cognition through brain-machine interfaces. Musk's innovative spirit and leadership have made him a prominent figure in the world of technology and entrepreneurship.
    """

    summary_template = """
    given the information {information} about a person, I want you to create:
    1. A short summary
    2. twwo interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    # llm = ChatOllama(temprature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
