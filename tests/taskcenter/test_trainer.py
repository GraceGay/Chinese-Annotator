from chi_annotator.task_center.config import AnnotatorConfig
from chi_annotator.task_center.data_loader import load_local_data
from chi_annotator.task_center.model import Trainer
from tests.utils.txt_to_json import create_tmp_test_file, rm_tmp_file


class TestTrainer(object):
    """
    test Trainer and Interpreter
    """
    def test_load_local_data(self):
        """
        test load local json format data
        :return:
        """
        tmp_path = create_tmp_test_file("tmp.json")
        train_data = load_local_data(tmp_path)
        rm_tmp_file("tmp.json")
        assert train_data is not None
        assert len(train_data.training_examples) == 1000
        assert "text" not in train_data.training_examples[0].data
        assert "label" in train_data.training_examples[0].data

    def test_load_config(self):
        """
        test load config
        :return:
        """
        config = AnnotatorConfig(\
            filename="chi_annotator/user_instance/examples/classify/spam_email_classify_config.json")
        assert config["name"] == "email_spam_classification"

    def test_load_default_config(self):
        """
        test load default config
        :return:
        """
        config = AnnotatorConfig()
        assert config["config"] == "config.json"

    def test_trainer_init(self):
        """
        test trainer
        :return:
        """
        test_config = "tests/data/test_config.json"
        config = AnnotatorConfig(test_config)

        trainer = Trainer(config)
        assert len(trainer.pipeline) == 1
        # char_tokenizer component should been created
        assert trainer.pipeline[0] is not None

    def test_pipeline_flow(self):
        """
        test trainer's train func for pipeline
        :return:
        """
        test_config = "tests/data/test_config.json"
        config = AnnotatorConfig(test_config)

        trainer = Trainer(config)
        assert len(trainer.pipeline) == 1
        # char_tokenizer component should been created
        assert trainer.pipeline[0] is not None
        # create tmp train set
        tmp_path = create_tmp_test_file("tmp.json")
        train_data = load_local_data(tmp_path)
        # rm tmp train set
        rm_tmp_file("tmp.json")

        interpreter = trainer.train(train_data)
        assert interpreter is not None
        # TODO because only char_tokenizer now.

    def test_trainer_persist(self):
        """
        test pipeline persist
        :return:
        """
        # TODO because only char_tokenizer now. nothing to be persist
        pass

    def test_train_model_empty_pipeline(self):
        pass

    def test_train_named_model(self):
        pass

    def test_handles_pipeline_with_non_existing_component(self):
        pass

    def test_load_and_persist_without_train(self):
        pass

    def test_train_with_empty_data(self):
        pass

