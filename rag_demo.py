import chromadb
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
import pandas as pd
import os

df = pd.read_csv('train.csv')

# Chroma client and collection
client = chromadb.Client()
collection = client.create_collection("song_lyrics")


llm = OllamaLLM(model="segmenter2_llama2")

# add song lyrics to Chroma collection 
for idx, row in df.iterrows():
    collection.add(
        documents=[row["Letra"]],
        metadatas=[{"song": row["Letra"]}],
        ids=[str(idx)],
    )

# save collection to disk
collection.persist()

# function to retrieve similar songs
def retrieve_similar_songs(input_song: str, collection, top_k=3):
    results = collection.query(query_texts=[input_song], n_results=top_k)
    return [result['document'] for result in results['documents']]

def build_few_shot_prompt(input_song: str, similar_songs: list):
    examples = []
    for song in similar_songs:
        examples.append({
            "input": song,
            "output": song 
        })
    
    example_template = """
    Input:
    {input}

    Output:
    {output}
    """

    example_prompt = PromptTemplate(
        input_variables=["input", "output"],
        template=example_template,
    )

    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="Segment the song lyrics into verses.\n\n",
        suffix="Input:\n{input}\n\nOutput:",
        input_variables=["input"],
    )

    return few_shot_prompt.format(input=input_song)

input_song = "Que rueden, que rueden, las cáscaras de huevo: las lavanderas hacen así, las planchadoras hacen así, las barrenderas hacen así"
similar_songs = retrieve_similar_songs(input_song, collection)
final_prompt = build_few_shot_prompt(input_song, similar_songs)

output = llm.invoke(final_prompt)
print("Generated Segmented Lyrics:")
print(output)
