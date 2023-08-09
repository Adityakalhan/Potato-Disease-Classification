# Potato Disease Classification

- Using CNNs to create a model that helps in identifying potato diseases, namely Early Blight, Late Blight, and also to see if the Potato plant is healthy or not.

- 2 Models were trained with different EPOCHS and Architecture, both the models got a very high score of 97.41 % and 96.12 % respectively.

- There was a training dataset(70%),testing datset(20%) and a validation dataset(10%)

- Models are hosted on using tf-serving on localhost 8501 on my local machine from which the FastAPI fetches the predictions.




### Commands to run docker 
- `docker run -it -v "C:\Users\Aditya Kalhan\OneDrive - Thapar University\College\Projects\potato-disease:/potato-disease" -p 8501:8501 --entrypoint /bin/bash tensorflow/serving`

- tensorflow_model_server --rest_api_port=8501 --model_name=potato_model --model_base_path=/potato-disease/saved_models/

- tensorflow_model_server --rest_api_port=8501 --model_config_file="/potato-disease/models.config"

