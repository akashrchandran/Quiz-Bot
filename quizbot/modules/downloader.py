import gdown
import os

class FilesDownloder:
    def __init__(self):
        self.qa_model_name = "multitask-qg-ag.ckpt"
        self.qa_model_id = "1ZhLe_nO_1VxIoVj5zRB61Ql-5_l0ZTJi"
        self.qa_model_path = "quizbot/ml_models/question_generation/models/multitask-qg-ag.ckpt"
        self.sense2vec_model_path = "quizbot/ml_models/sense2vec_distractor_generation/data/"
        self.download_qa_model()
        self.download_sense2vec_model()

    def download_qa_model(self):
        if not os.path.exists(self.qa_model_path):
            gdown.download(id=self.qa_model_id, output=self.qa_model_path)
        print("QA model downloaded successfully!")

    def download_sense2vec_model(self):
        if not os.path.exists(self.sense2vec_model_path + "s2v_old"):
            gdown.download(id="1Lz8WZ3nI6zH2q3e2q5oY4KqYV5wXhN5p", output=self.sense2vec_model_path)
        print("Sense2Vec model downloaded successfully!")
        

