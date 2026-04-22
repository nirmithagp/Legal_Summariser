import os
from dotenv import load_dotenv
from crewai.tools import BaseTool  # import BaseTool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
persist_directory_name = os.getenv("PERSIST_DIRECTORY_NAME", "chroma_db")

base_path = os.path.dirname(os.path.abspath(__file__))
persist_directory_path = os.path.join(base_path, persist_directory_name)

ipc_collection = Chroma(
    collection_name="ipc_collection",
    persist_directory=persist_directory_path,
    embedding_function=HuggingFaceEmbeddings(),
)

class IPCSearchTool(BaseTool):
    name: str = "IPC Section Search Tool"
    description: str = "Searches IPC sections from ChromaDB based on a user's query."

    def _run(self, query: str) -> str:
        docs = ipc_collection.similarity_search(query, k=5)
        if not docs:
            return "No relevant IPC sections found for this query."

        output = "Identified IPC Sections:\n"
        for doc in docs:
            section = doc.metadata.get("section", "N/A")
            section_title = doc.metadata.get("section_title", "N/A")
            chapter = doc.metadata.get("chapter", "N/A")
            chapter_title = doc.metadata.get("chapter_title", "N/A")
            content = doc.page_content

            output += f"- Section {section} – {section_title}\n"
            output += f"  Chapter: {chapter} – {chapter_title}\n"
            output += f"  Content: {content}\n\n"

        return output.strip()

# Create the tool instance
ipc_sections_search_tool = IPCSearchTool()
