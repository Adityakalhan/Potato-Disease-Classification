### Commands to run docker 
- `docker run -it -v "C:\Users\Aditya Kalhan\OneDrive - Thapar University\College\Projects\potato-disease:/potato-disease" -p 8501:8501 --entrypoint /bin/bash tensorflow/serving`

- tensorflow_model_server --rest_api_port=8501 --model_name=potato_model --model_base_path=/potato-disease/saved_models/

- tensorflow_model_server --rest_api_port=8501 --model_config_file="/potato-disease/models.config"

