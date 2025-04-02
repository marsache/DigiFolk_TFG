import ollama

def segmenter(song_lyrics: str, model_name: str):

    # Initialize the Ollama client
    client = ollama.Client()

    # Define the model and the input prompt
    model = model_name  # Model name
    song = song_lyrics # Replace with song lyrics
    prompt = "Segment the following song in verses: " + song

    # Sends the query to the model
    response = client.generate(model=model, prompt=prompt)

    # Response from the model
    # print("Response from analyst:")
    # print(response.response)

    return response.response