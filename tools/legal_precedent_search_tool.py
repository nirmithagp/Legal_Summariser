import os
from dotenv import load_dotenv
from crewai.tools import BaseTool  # BaseTool from crewai.tools
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
persist_directory_name = os.getenv("PERSIST_DIRECTORY_NAME", "chroma_db")

base_path = os.path.dirname(os.path.abspath(__file__))
persist_directory_path = os.path.join(base_path, persist_directory_name)

# Initialize ChromaDB collection for legal precedents
precedent_collection = Chroma(
    collection_name="legal_precedent_collection",
    persist_directory=persist_directory_path,
    embedding_function=HuggingFaceEmbeddings(),
)

class LegalPrecedentSearchTool(BaseTool):
    name: str = "Legal Precedent Search Tool"
    description: str = "Searches legal precedents from ChromaDB based on a user's query."

    def _run(self, query: str) -> str:
        docs = precedent_collection.similarity_search(query, k=5)
        if not docs:
            return "No relevant legal precedents found."

        output = "Identified Legal Precedents:\n"
        for doc in docs:
            case_name = doc.metadata.get("case_name", "N/A")
            year = doc.metadata.get("year", "N/A")
            court = doc.metadata.get("court", "N/A")
            summary = doc.page_content

            output += f"- Case: {case_name} ({year})\n"
            output += f"  Court: {court}\n"
            output += f"  Summary: {summary}\n\n"

        return output.strip()

# Create the tool instance
legal_precedent_search_tool = LegalPrecedentSearchTool()

