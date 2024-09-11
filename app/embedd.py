import chromadb
from sentence_transformers import SentenceTransformer
from .dataextractor import createDataset

class VectorStore:

    def __init__(self, collection_name):
       # Initialize the embedding model
        self.embedding_model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')
        self.chroma_client = chromadb.Client()
        #
        # Try to load the collection if it exists, otherwise create it

        try:
            self.collection = self.chroma_client.get_collection(name=collection_name)
            print(f"Loaded existing collection: {collection_name}")
        except:
            self.collection = self.chroma_client.create_collection(name=collection_name)

            print(f"creating the {collection_name} collection")
        
    # Method to populate the vector store with embeddings from a dataset
    def populate_vectors(self, dataset):
        for i, item in enumerate(dataset):
            combined_text = f"{item['Request']}. {item['Response']}"
            embeddings = self.embedding_model.encode(combined_text).tolist()
            self.collection.add(embeddings=[embeddings], documents=[item['Response']], ids=[f"id_{i}"])

    # Method to search the ChromaDB collection for relevant context based on a query
    def search_context(self, query, n_results=1):
        query_embeddings = self.embedding_model.encode(query).tolist()
        return self.collection.query(query_embeddings=query_embeddings, n_results=n_results)



class work_check:

    def __init__(self) -> None:
        self.vec_obj = VectorStore("knowledge-base-1")
    # Example usage


    def working_func(self):
    # Initialize the handler with collection name
        
        test_data = createDataset()
        # Assuming closed_qa_dataset is defined and available
        test_data.append({'Response':'Komorida was born in Kumamoto Prefecture on July 10, 1981. After graduating from high school,he joined the J1 League club Avispa Fukuoka in 2000. His career involved various positions and clubs, from a midfielder at Avispa Fukuoka to a defensive midfielder and center back at clubs such as Oita Trinita, Montedio Yamagata, Vissel Kobe, and Rosso Kumamoto. He also played for Persela Lamongan in Indonesia before returning to Japan and joining Giravanz Kitakyushu, retiring in 2012.','Request': 'who was pineapple'})
        self.vec_obj.populate_vectors(test_data)
        print("getting the call1")

        # context_response = vector_store.search_context("who was pineapple")

        # print("getting the call2", context_response)

        # #print(context_response['documents'][0])

        # return context_response['documents'][0]
    
    def chat_func(self, mes):
        context_response = self.vec_obj.search_context(mes)

        print("getting the call2", context_response)

        if context_response['distances'][0][0] >= 1.4:
            return ["Sorry I could not help you with this request, this is not related to Zpro"]

        # #print(context_response['documents'][0])

        return context_response['documents'][0]
    
