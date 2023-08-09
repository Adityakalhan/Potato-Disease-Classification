### Commands to run docker 
- `docker run -it -v "C:\Users\Aditya Kalhan\OneDrive - Thapar University\College\Projects\potato-disease:/potato-disease" -p 8501:8501 --entrypoint /bin/bash tensorflow/serving`

- `tensorflow_model_server --rest_api_port=8501 --model_name=potato_model --model_base_path=/potato-disease/saved_models/` use this command to use the latest version of model in saved_models

- `tensorflow_model_server --rest_api_port=8501 --model_config_file="/potato-disease/models.config"` use this to edit endpoint to eg : ` "http://localhost:8501/v1/models/potato_model/versions/1:predict" ` this will use the version 1 of the model
- 

