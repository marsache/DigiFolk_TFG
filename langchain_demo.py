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

#llm = OllamaLLM(model="segmenter2_llama2", params={"format": "json"})
#llm = OllamaLLM(model="segmenter2_gemma3", params={"format": "json"})
#llm = OllamaLLM(model="segmenter3_deepseekr1", params={"format": "json"})
llm = OllamaLLM(model="segmenterft_llama2", params={"format": "json"})


#input_song = "Que rueden, que rueden, las cáscaras de huevo: las lavanderas hacen así, las planchadoras hacen así, las barrenderas hacen así"
#input_song = "A un campo lejos me fui por ver si así te olvidaba y mientras más lejos me iba, mucho más te recordaba. Al darte pestañas negras, Dios, sin duda, se propuso, que por las muertes que causas, ¡ay!, Soleá, Soleá, tus ojitos vistan luto. Dicen que ya no hay locura y yo digo que es verdad, pues si locura aún hubiera, loco estuviera yo ya. Entre la tierra y er sielo no hay mugeres con mas sal que las mugeres de España con su mantilla tersiá. Permita Dios donde pongas todos tus cinco sentíos que paguen a tu querer como tú has pagao er mío. Quien te llamó Petenera no ha sabido darte nombre, que te debió poner, niña de mi corazón, perdición, ¡ay! de los hombres. Señor alcalde mayor, no prenda usté a los ladrones, que tiene usté una hija, niña de mi corazón, que roba los corazones. Valor, mare, que me matan; que no me puedo valer; son dos negros asesinos los ojos de esta muger."
#input_song = "Déjame memoria triste; no me estás atormentando; se la quise o no la quise, niña de mi corazón, no me estás recordando."
#input_song = "Y al aura el gentil capullo busca al imán el acero la fuente el que tiene sed y mi corazón al tuyo Y con esto me despido adiós público del alma al que le guste mi canto mil gracias da la gitana,"
input_song = "Estaba la pájara pinta sentadita en el verde limón, con el pico recoge la hoja, con las alas recoge la flor. ¡Ay, sí! ¿Cuándo la veré yo? ¡Ay, sí! ¿Cuándo la veré yo? Me arrodillo a los pies de mi madre, fiel y constante, dame una mano, dame la otra, dame un besito que sea de tu boca."
final_prompt = few_shot_prompt.format(input=input_song)




print("FINAL PROMPT:")
print(final_prompt)

output = llm.invoke(final_prompt)

print("Output: " + output)

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
