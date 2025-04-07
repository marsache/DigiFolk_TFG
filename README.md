# DigiFolk_TFG [WIP]

## Creación del modelo de análisis de textos
- Instalar [Ollama](https://ollama.com/)
- Comando para crear el modelo de segmentación (desde el directorio segmenter_model):
  ```
  ollama create segmenter -f ./Modelfile
  ```
- Comando para utilizar el modelo de conversación desde terminal:
  ```
  ollama run segmenter
  ```
- Comando para eliminar el modelo:
  ```
  ollama rm segmenter
  ```

## Docker
- Listar todos los contenedores de Docker
  ```
  docker container ls -a
  ```
- Detener el contenedor
  ```
  docker container stop container_id
  ```
- Eliminar el contenedor detenido
  ```
  docker container rm container_id
  ```
- Iniciar el contenedor
  ```
  sudo docker run -dp 80:5000 container_id
  ```
- Abrir Bash en el contenedor
  ```
  docker exec -it container_id bash
  ```

## Referencias
- [Ollama](https://ollama.com/)
- [OllamaTutorial](https://github.com/techwithtim/OllamaTutorial/tree/main)
- [Flask POST Request with AJAX](https://github.com/jimdevops19/codesnippets/tree/main/Flask%20POST%20Request%20with%20AJAX)
