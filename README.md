# Enhancing Retrieval via Graph RAG
# Introduction
Graph RAG is an innovative project that leverages advanced Large Language Model (LLM) techniques to transform the landscape of medical data retrieval and comprehension. By integrating cutting-edge technologies such as triplet generation, knowledge graph construction, semantic search, and an interactive Streamlit application, Graph RAG provides a robust solution for medical professionals and researchers seeking efficient access to complex medical information.
# Problem Statement
Medical research and literature are vast and continuously expanding, making it challenging for healthcare professionals and researchers to efficiently extract relevant information. Traditional search methods often fall short in capturing the nuanced relationships and intricate details inherent in medical data, particularly concerning inflammation-related studies. This information overload hampers timely decision-making and impedes the advancement of medical knowledge.
# Results
![alt text] (Imgs/results.png)
# Solution
Graph RAG addresses these challenges by offering a comprehensive framework that enhances the retrieval and understanding of medical data related to inflammation. The project employs a multi-faceted approach:

**Triplet Generation**: 
 Utilizes LLMs to extract and curate meaningful triplets (subject, predicate, object) from extensive medical literature, ensuring the extraction of relevant and actionable data.

**Knowledge Graph Construction**: 
 Builds a dynamic and scalable knowledge graph using Neo4j, effectively representing the extracted triplets and illustrating the complex interconnections within the data.

**Semantic Search**: 
 Implements Retrieval-Augmented Generation (RAG) techniques to facilitate sophisticated querying, allowing users to retrieve precise and contextually relevant information from the knowledge graph.

**Streamlit Application**: 
 Provides an intuitive and interactive interface for users to explore, visualize, and query the knowledge graph seamlessly, enhancing user experience and accessibility.
# Features

**Automated Triplet Extraction**
- Efficiently parses medical articles and books to generate structured triplets.

**Dynamic Knowledge Graph**
- Utilizes Neo4j to create and manage a scalable knowledge graph that adapts to new data inputs.

**Advanced Semantic Search**
- Employs RAG techniques to deliver accurate and context-aware search results.

**User-Friendly Interface**
- Streamlit-based application offers an interactive platform for data exploration and querying.
# Technical Stack
*Language Models*: Utilizes state-of-the-art LLMs for triplet generation.

*Database*: Neo4j for constructing and managing the knowledge graph.

*Search Techniques*: Retrieval-Augmented Generation (RAG) for semantic search functionality.

*Frontend*: Streamlit for developing the interactive user interface.

