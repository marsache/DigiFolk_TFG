## ISSUES

### Formato de la salida de versos
El modelo no siempre devuelve los versos segmentados con el mismo formato. Posibles salidas:

- Separación de versos con \n 
    - Con el formato actual utilizado para mostrar los versos en el servicio web, esto no supone un problema, ya que el \n formatea los versos para escribirlos en líneas distintas.
    - Solución propuesta: modificar el prompt para que siempre se devuelva con este formato.
- Versos entrecomillados y separados por comas
    - Este formato podría procesarse, pero no de forma genérica, por lo que afectaría a cómo se procesan el resto de formatos.
    - Solución propuesta: tratar de obtener la salida con el primero formato mencionado.

### Número de versos y número de elementos en el array de sílabas

Normalmente, el conteo de sílabas que proporciona el modelo tras el análisis no es fiel, ya que el número de "versos que cuenta" es mayor que el número de versos que segmenta realmente.

Solución propuesta: uso de reflexión para modificar la respuesta definitiva del modelo.

## Ideas a implementar y otras tareas pendientes

- Reflexión
- Comparación de canciones