from src.Tutorial_Project.utils.common import read_yaml, create_directories
from src.Tutorial_Project.constants import *
from src.Tutorial_Project.entity.config_entity import (DataIngestionConfig, BaseModelConfig,TrainingConfig)
import os

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config= self.config.Data_Ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_prepared_base_model_config(self) -> BaseModelConfig:
        config = self.config.Prepare_Base_Model
        params = self.params
        create_directories([config.root_dir])
        
        prepared_base_model_config = BaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            params_image_size=params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE,
            params_classes=params.CLASSES,
            params_weights=params.WEIGHTS,
            params_include_top=params.INCLUDE_TOP
        )
    
        return prepared_base_model_config
    
    def get_training_config(self) -> TrainingConfig:
        config = self.config
        params = self.params
        create_directories([config.Training.root_dir])
        
        training_config = TrainingConfig(
            root_dir=config.Training.root_dir,
            trained_model_path=config.Training.trained_model_path,
            updated_base_model_path=config.Prepare_Base_Model.updated_base_model_path,
            training_data=config.Training.training_data,
            testing_data=config.Training.testing_data,
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
    
        return training_config
