import os
import sys
import logging
from dotenv import load_dotenv
# import anthropic
from langchain_anthropic import ChatAnthropic


class VectorDB():
    def __init__(self):
        # Load and set the environment variable
        load_dotenv()
        API_KEY = os.getenv('ANTHROPIC_API_KEY') # Authentication
        self.llm = ChatAnthropic(model="claude-2.1", anthropic_api_key=API_KEY)

        logging.basicConfig(filename='logs.log', filemode='w', level=logging.INFO)
        logging.info('Loaded the model!')
        sys.stdout.flush()


    def chunk_documents(self):
        loader = DirectoryLoader('./source/', glob="./*.txt", loader_cls=TextLoader)
        documents = loader.load()

        # Chunk the data
        text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""], chunk_size=1000, chunk_overlap=200)
        chunked_documents = text_splitter.split_documents(documents)
        logging.info('chunking')
        logging.info(chunked_documents)

        for i in chunked_documents:
            logging.info(i.metadata)
        return(chunked_documents)
    