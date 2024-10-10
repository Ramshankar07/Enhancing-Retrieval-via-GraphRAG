from vectorize import VectorDB
import anthropic
import os
from langchain._api.module_import import LangChainDeprecationWarning
# from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
open('logs.log', 'w').close()

class graphRAG():
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


    def model_prediction(self, question, text, format='graph'): 
        
        with open(f'prompt/{format}.txt', 'r') as file:
            prompt = file.read()

        input = f"""\n\nHuman: {prompt}
    
                        <question>{question}</question>

                        <text>{text}</text>
                        
                        Assistant:"""
        
        try:
            completion = self.get_completion(input)
            return completion
        except Exception as e:
            raise e
    
    def process_response(self, response):
        # extract content inside <answer> tag
        start = response.find('<answer>') + len('<answer>')
        end = response.find('</answer>')
        response = response[start:end]
        return response

    def check_response(self, question, response, format='graph'):
        with open(f'prompt/{format}.txt', 'r') as file:
            given_prompt = file.read()

        prompt = """You will be given a prompt and a question and answer pair.
                    Your challenge is to determine if the answer follows all the instructions in the prompt.
                    If the answer follows all the instructions in the prompt, return the answer as is.
                    If the answer does not follow all the instructions in the prompt, modify the answer so that it does.
                    Make sure to do not indicate research or document references in the answer.
                    Just provide the answer to the question in a clear and concise manner."""

        input = f"""\n\nHuman: {prompt}
    
                        <question>{question}</question>

                        <prompt>{given_prompt}</prompt>

                        <answer>{response}</answer>
                        
                        Assistant:"""
        try:
            completion = self.get_completion(input)
            return completion
        except Exception as e:
            raise e

    def get_response(self, question):
        vector_db = VectorDB()
        docs = vector_db.get_db_retriever(question, k=6)
        text = [doc.page_content for doc in docs]

        response = self.model_prediction(question, text)
        return response
    
    def get_response_recommedations(self, question):
        vector_db = VectorDB()
        docs = vector_db.get_db_retriever(question, k=6)
        text = [doc.page_content for doc in docs]

        response = self.model_prediction(question, text, format='recommendations')
        response = self.process_response(response)
        return response
    
    
    

