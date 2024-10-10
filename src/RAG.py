from vectorize import VectorDB
import anthropic
import os
import logging
import pandas as pd


# create log file
logging.basicConfig(filename='logs.log', filemode='w', level=logging.INFO)
open('logs.log', 'w').close()

class RAG():
    def __init__(self):
        try:
            API_KEY = os.getenv('ANTHROPIC_API_KEY')
            self.client = anthropic.Client(api_key=API_KEY)
        except Exception as e:
            self.log.error(f"Error connecting to the anthropic API {e}")
            raise e

    

    def get_completion(self, prompt, model='claude-2.1'):
        return self.client.completions.create(prompt=prompt, max_tokens_to_sample=4000, model=model).completion
        # max_tokens_to_sample = 4000 for optimal performance


    def model_prediction(self, question, text):
    # def model_prediction(self, question):
            prompt = "Your challenge is to respond to a question using the information provided in the accompanying text. Construct your answer by extracting relevant details from the text to ensure accuracy and completeness."
            input = f"""\n\nHuman: {prompt}
        
                            <question>{question}</question>

                            <text>{text}</text>
                            
                            Assistant:"""
            
            try:
                completion = self.get_completion(input)
                return completion
            except Exception as e:
                raise e

    def get_response(self,question):
        vector_db = VectorDB()
        docs = vector_db.get_db_retriever(question, k=3)
        logging.info(docs)
        text = [doc.page_content for doc in docs]
        logging.info(text)

        response = self.model_prediction(question, text)
        return response
    
    def get_response_eval(self,question):
        vector_db = VectorDB()
        docs = vector_db.get_db_retriever(question, k=3)
        logging.info(docs)
        text = [doc.page_content for doc in docs]
        logging.info(text)

        response = self.model_prediction(question, text)
        print(response)
        return question, text, response
    
    def save_to_csv(self, question, source, answer, scores):

        data = {
            'Question': question,
            'Source': source,
            'Answer': answer,
            'Similarity Score': scores[0],
            'Relevancy Score': scores[1],
            'Reason': scores[2],
            'Coherence Score': scores[3],
            'Coherence Reason': scores[4],
            'Faithfulness Score': scores[5],
            'Faithfulness Reason': scores[6],
            'Hallucination Score': scores[7],
            'Hallucination Reason': scores[8],
            'Toxicity Score': scores[9],
            'Toxicity Reason': scores[10],
            'Bias Score': scores[11],
            'Bias Reason': scores[12]
        }

        df = pd.DataFrame([data])

        file_exists = os.path.isfile('er_metrics.csv')

        if file_exists:
            df.to_csv('er_metrics.csv', mode='a', header=False, index=False)
        else:
            df.to_csv('er_metrics.csv', index=False)

        print("Scores saved successfully.")



