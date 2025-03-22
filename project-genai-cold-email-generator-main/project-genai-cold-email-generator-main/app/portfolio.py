import os
import pandas as pd
import chromadb  # Ensure chromadb is installed

class Portfolio:
    def __init__(self):
        # Get the correct file path
        file_path = os.path.join(os.path.dirname(__file__), "resource", "my_portfolio.csv")
        
        # Load the CSV file
        self.data = pd.read_csv(file_path)
        
        # Initialize ChromaDB client correctly
        self.chroma_client = chromadb.PersistentClient('vectorstore')

    def load_portfolio(self):
        return self.data

    def query_links(self, skills):
        # Dummy implementation for filtering links by skills
        filtered_data = self.data[self.data['skills'].str.contains('|'.join(skills), case=False, na=False)]
        return filtered_data['links'].tolist()
