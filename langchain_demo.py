from langchain.prompts import PromptTemplate, FewShotPromptTemplate
import pandas as pd
from langchain_ollama import OllamaLLM

df = pd.read_csv('train.csv')

example_template = """
Input:
{input}

Output:
{output}
"""

# examples = [
#     {"input": row["Letra"], "output": row["Versos"]}
#     for _, row in df.sample(3).iterrows()  # randomly pick 3 examples
# ]

examples = [
    {
        "input": "El que quiera saber de qué color son las penas siente plaza de soldado y auséntese de su tierra",
        "output": "El que quiera saber\nde qué color son las penas\nsiente plaza de soldado\ny auséntese de su tierra"
    },
    {
        "input": "Me dices que era un gato el que entró por tu ventana. En la vida he visto yo, serrano de mi querer, un gato negro y con sotana.",
        "output": "Me dices que era un gato\nel que entró por tu ventana.\nEn la vida he visto yo,\nserrano de mi querer,\nun gato negro y con sotana."
    }
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template=example_template,
)

# few_shot_prompt = FewShotPromptTemplate(
#     examples=examples,
#     example_prompt=example_prompt,

#     prefix = """You are a lyrics segmenter. Your task is to take unformatted song lyrics and divide them into meaningful verses.

#     Each verse should be separated by **one newline**.
#     Keep the original wording — do not invent lyrics.
#     """
    
#     suffix = """Input:
#     {input}

#     Output (verses separated by one newline):"""

#     input_variables=["input"],
# )

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="""You are a lyrics segmenter. Your task is to take unformatted song lyrics and divide them into meaningful verses.

    Each verse should be separated by **one newline**.
    Keep the original wording — do not invent lyrics.
    Here are some examples:""",
    suffix="""Now segment the following song:
    
    Input:
    {input}

    Output (verses separated by one newline):""",
    input_variables=["input"],
)

llm = OllamaLLM(model="segmenter2_llama2")


input_song = "Que rueden, que rueden, las cáscaras de huevo: las lavanderas hacen así, las planchadoras hacen así, las barrenderas hacen así"
final_prompt = few_shot_prompt.format(input=input_song)

print("FINAL PROMPT:")
print(final_prompt)

output = llm.invoke(final_prompt)

print(output)
