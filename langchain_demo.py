import json
import re
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
        "input": "Ni la fuente más risueña ni el canario más sonoro ni la tórtola en su breña cantarán como yo lloro gotas de sangre por ella",
        "output": "Ni la fuente más risueña\nni el canario más sonoro\nni la tórtola en su breña\ncantarán como yo lloro\ngotas de sangre por ella"
    }
    # {
    #     "input": "Me dices que era un gato el que entró por tu ventana. En la vida he visto yo, serrano de mi querer, un gato negro y con sotana.",
    #     "output": "Me dices que era un gato\nel que entró por tu ventana.\nEn la vida he visto yo,\nserrano de mi querer,\nun gato negro y con sotana."
    # }
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

#llm = OllamaLLM(model="segmenter2_llama2", params={"format": "json"})
#llm = OllamaLLM(model="segmenter2_gemma3", params={"format": "json"})
#llm = OllamaLLM(model="segmenter3_deepseekr1", params={"format": "json"})
llm = OllamaLLM(model="segmenterstablelm2", params={"format": "json"})


#input_song = "Que rueden, que rueden, las cáscaras de huevo: las lavanderas hacen así, las planchadoras hacen así, las barrenderas hacen así"
#input_song = "Déjame memoria triste; no me estás atormentando; se la quise o no la quise, niña de mi corazón, no me estás recordando."
#input_song = "Y al aura el gentil capullo busca al imán el acero la fuente el que tiene sed y mi corazón al tuyo Y con esto me despido adiós público del alma al que le guste mi canto mil gracias da la gitana,"
#input_song = "Estaba la pájara pinta sentadita en el verde limón, con el pico recoge la hoja, con las alas recoge la flor. ¡Ay, sí! ¿Cuándo la veré yo? ¡Ay, sí! ¿Cuándo la veré yo? Me arrodillo a los pies de mi madre, fiel y constante, dame una mano, dame la otra, dame un besito que sea de tu boca."
#input_song = "Duérmete, mi niño con todo y tambache, tu madre la zorra, tu padre el tlacuache. Duérmete, niñita, que ahí viene el viejo, a llevarte viene con todo y pellejo. Duérmete, niñito, que ahí viene el coyote, a llevarte viene y a comerte al monte. Duérmete, mi niño, que estás en cajón; tu madre la zorra, tu padre el tejón. Duérmete, niñito, no venga el caucón, te quite la vida y a mí el corazón."
input_song = "Me dices que era un gato el que entró por tu ventana. En la vida he visto yo, serrano de mi querer, un gato negro y con sotana."
final_prompt = few_shot_prompt.format(input=input_song)




# print("FINAL PROMPT:")
# print(final_prompt)

# output = llm.invoke(final_prompt)

# print("Output: " + output)


for x in range (10):
    output = llm.invoke(final_prompt)

    print("Output " + str(x) + ": " + output)

# match = re.search(r'\{.*\}', output)

# if match:
#     # Extract the JSON string and load it into a Python dictionary
#     output_cleaned = match.group(0)  # This will get the JSON portion
#     response_json = json.loads(output_cleaned)
#     print("Cleaned JSON response:")
#     print(response_json)
# else:
#     print("No JSON found in the output.")
    
# output_cleaned = output.replace('```json', '').replace('```', '').strip()
# response_json = json.loads(output_cleaned)

#print("JSON Output: " + response_json)
