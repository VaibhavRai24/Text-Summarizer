from Text_Summarization.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import Pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
        
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penality":0.8, "num_beams": 8, "max_length": 128
        }
        
        pipe = Pipeline("summarization", model= self.config.model_path, tokenizer= tokenizer)
        
        print("Dialogue")
        print(text)
        
        
        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\Model Summary")
        print(output)
        
        return output