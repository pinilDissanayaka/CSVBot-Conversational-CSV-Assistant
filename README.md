# 🗂️ CSVBot - Your Conversational CSV Assistant

🚀 CSVBot is an AI-powered tool designed to help you interact with your CSV files through natural language queries. No more writing code or complex formulas—just ask questions, and CSVBot will provide the answers or perform data transformations, making data analysis intuitive and fun!

🔗 Try it out live: CSVBot is hosted [here](https://csvbot-conversational-csv-assistant-wqmbaqrcshdhnbcotm9dt5.streamlit.app/) 👈

## ✨ Key Features
- Conversational Queries: Ask questions like "What is the total revenue for 2023?" or "List the top 5 products by sales."
- Data Transformation: Perform operations like sorting, filtering, and grouping data with natural language commands.
- Contextual Insights: Powered by LangChain and LLaMA3, CSVBot retrieves contextual data and recommendations.
- RAG Integration: Using Pinecone as a vector store, CSVBot performs Retrieval-Augmented Generation to combine your CSV data with external knowledge for richer insights.
- Embeddings: Leverages Gemini AI embeddings for high-quality understanding of your CSV data.
- Visualizations: Instantly generate charts or graphs from your queries (e.g., "Show me a bar chart of monthly sales").
  
## 🛠️ Tech Stack
- LangChain: Enables conversational natural language interaction.
- Pinecone: Provides fast, scalable vector search for RAG.
- LLaMA 3: Powers the underlying language model for understanding and generating responses.
- Gemini AI Embeddings: Used to create high-quality vector embeddings for your CSV data.

## ⚙️ How It Works
1. Upload Your CSV: Start by uploading your CSV file.
2. Ask Your Query: Use natural language to ask questions (e.g., "What are the average sales for each region?").
3. Get Insights: CSVBot processes your data and retrieves or generates the requested information, including enhanced insights using RAG.
4. Export or Visualize: Save your transformed data or generate a visualization on the fly!

## 📦 Installation

```
# Clone the repository
git clone https://github.com/pinilDissanayaka/CSVBot-Conversational-CSV-Assistant.git

# Navigate to the directory
cd CSVBot

# Install dependencies
pip install -r requirements.txt

```

##🚀 Usage

1. Run the App:
```
streamlit run CSVBot.py
```

2. Upload CSV: Once the app is running, upload your CSV file and start querying.

3. Ask Questions:

- "What is the total profit in Q1 2023?"
- "Sort sales data by region."
- "Show a pie chart of revenue by product category."
- Export Results: Save transformed data or visualizations as CSV or image files.

## 🤖 AI Architecture

CSVBot uses a combination of:

- LangChain to create a conversational flow.
- LLaMA3 for understanding and generating responses based on CSV data.
- Pinecone as a vector store for fast retrieval of relevant data.
- Gemini AI embeddings to represent CSV content in vector space for efficient querying and insights.
  
## 🎨 Screenshots
![Screenshot 2024-10-24 133537](https://github.com/user-attachments/assets/7f13aee2-f656-4c46-8a8c-248ab64b14c3)

![CSV Assistant](https://github.com/user-attachments/assets/fe636390-b17b-47d0-851b-9713b402d499)


## 🤝 Contributing
Feel free to fork this repo, submit issues, or make pull requests. Any contribution is appreciated! 🙌

##📄 License
This project is licensed under the MIT License.


Let CSVBot turn your CSV files into knowledge! 💡 Upload, ask, and discover.

