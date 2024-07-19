<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">SMART-ASSISTANT-RAG</h1>
</p>
<p align="center">
    <em>Unlock Answers at the Speed of Thought</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/gabechu/smart-assistant-rag?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/gabechu/smart-assistant-rag?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/gabechu/smart-assistant-rag?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/gabechu/smart-assistant-rag?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

Smart Assistant RAG is a sophisticated open-source project that combines retrieval and generation capabilities. It leverages AI models like Hugging Face and OpenAI for efficient search and response generation from documents. With modules for evaluation, preprocessing, and text generation, the project excels in evaluating relevance, diversity, and speed of generated responses. Smart Assistant RAG showcases the fusion of cutting-edge technologies to enhance the document retrieval and information generation process, providing users with a powerful and intelligent assistant for various tasks.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project architecture includes retrieval and generation pipelines using Hugging Face and OpenAI models. It defines vector models for text encoding and search functionalities for efficient document retrieval and response generation. |
| 🔩 | **Code Quality**  | The codebase maintains high-quality standards with consistent code formatting using Black and type checking with Mypy. It follows best practices for AI tasks and development tools integration. |
| 📄 | **Documentation** | The project provides detailed documentation, including notebooks for evaluating smart assistants' relevance and retrieval performance. It also explains the vector models, pipelines, and evaluation processes within the repository structure. |
| 🔌 | **Integrations**  | Key dependencies include libraries like Transformers and Torch for AI tasks, along with tools for code formatting and type checking. External APIs from OpenAI are used for text generation and retrieval tasks. |
| 🧩 | **Modularity**    | The codebase is modular with distinct modules for vector models, pipelines, retrieval, generation, and evaluation. It emphasizes reusability and encapsulation of functionalities for different components. |
| 🧪 | **Testing**       | Testing frameworks and tools such as evaluate and pytest are used for evaluating generated responses, retrieval performance, and overall system efficiency. The codebase focuses on ensuring accuracy and reliability through testing. |
| ⚡️  | **Performance**   | The project demonstrates efficient text encoding, retrieval, and generation processes for quick response generation. It utilizes vector-based search with cosine similarity calculations for faster document retrieval and processing. |
| 🛡️ | **Security**      | Measures like cryptography for data protection and access control are implemented within the codebase. It ensures secure communication and handling of sensitive information within the smart assistant system. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include Transformers, Torch, OpenAI API, cryptography for security, and development tools like Black and Mypy for code quality. |
| 🚀 | **Scalability**   | The project's architecture and modular design support scalability to handle increased traffic and load. It can efficiently scale the retrieval and generation processes for enhancing smart assistant capabilities. |

---

##  Repository Structure

```sh
└── smart-assistant-rag/
    ├── .github
    │   └── PULL_REQUEST_TEMPLATE.md
    ├── README.md
    ├── notebooks
    │   ├── evaluate_rag.ipynb
    │   └── evaluate_retrieval.ipynb
    ├── poetry.lock
    ├── pyproject.toml
    ├── src
    │   ├── __init__.py
    │   ├── data
    │   ├── evaluation
    │   ├── generation
    │   ├── pipelines
    │   ├── preprocessing
    │   ├── retrieval
    │   ├── utils.py
    │   └── vector_models
    └── tests
        ├── rag_evaluation_data.json
        └── retrieval_evaluation_data.json
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                 |
| ---                                                                                         | ---                                                                                                                                                                                                                                                     |
| [pyproject.toml](https://github.com/gabechu/smart-assistant-rag/blob/master/pyproject.toml) | Defines project dependencies for the smart-assistant-rag repository using pyproject.toml. Specifies libraries like Transformers and Torch for AI tasks, along with development tools. Maintains code formatting with Black and type checking with Mypy. |

</details>

<details closed><summary>notebooks</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                     |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                         |
| [evaluate_rag.ipynb](https://github.com/gabechu/smart-assistant-rag/blob/master/notebooks/evaluate_rag.ipynb)             | Generates responses for evaluating smart assistants relevance, diversity, and speed in retrieving and generating information from documents. Utilizes distinct retrieval and generation pipelines for analysis in the smart assistant repository structure. |
| [evaluate_retrieval.ipynb](https://github.com/gabechu/smart-assistant-rag/blob/master/notebooks/evaluate_retrieval.ipynb) | Executes retrieval evaluation using various vector models. Loads and evaluates top-k retrieval results, measuring precision, recall, and MRR. Facilitates comparison between HuggingFace and OpenAI vector models.                                          |

</details>

<details closed><summary>src</summary>

| File                                                                                | Summary                                                                                                                                                                       |
| ---                                                                                 | ---                                                                                                                                                                           |
| [utils.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/utils.py) | Calculates cosine similarity in batches between query and document vectors, aiding in efficient similarity computations within various modules like retrieval and generation. |

</details>

<details closed><summary>src.vector_models</summary>

| File                                                                                                                                      | Summary                                                                                                                                                                                                      |
| ---                                                                                                                                       | ---                                                                                                                                                                                                          |
| [base_vector_model.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/vector_models/base_vector_model.py)                 | Defines an abstract base for vector models to encode text inputs with floating-point arrays.                                                                                                                 |
| [hugging_face_vector_model.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/vector_models/hugging_face_vector_model.py) | Implements a Hugging Face vector model for encoding text using mean pooling. Utilizes transformers library for model loading and tokenization. Performs vector encoding efficiently for downstream tasks.    |
| [openai_vector_model.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/vector_models/openai_vector_model.py)             | Implements OpenAI embedding generation with efficient batching for text encoding using the OpenAI API within the vector models module. Enhances the architecture with advanced text processing capabilities. |

</details>

<details closed><summary>src.pipelines</summary>

| File                                                                                                                                                                                  | Summary                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                                   | ---                                                                                                                                                                                                                                             |
| [hugging_face_retrieval_openai_generation_pipeline.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/pipelines/hugging_face_retrieval_openai_generation_pipeline.py) | Defines pipeline integrating Hugging Face retrieval and OpenAI generation for RAG. Utilizes Hugging Face vector model and OpenAI GPT-4o. Achieves seamless retrieval and generation functionalities for the Smart Assistant RAG project.        |
| [rag_pipeline.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/pipelines/rag_pipeline.py)                                                                           | Generates responses by loading PDF documents in chunks for retrieval. Utilizes a retrieval module and a generation module to search queried information. Facilitates document context extraction and response generation based on user queries. |
| [openai_retrieval_openai_generation_pipeline.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/pipelines/openai_retrieval_openai_generation_pipeline.py)             | Defines a pipeline merging OpenAI retrieval and generation models for the Smart Assistant RAG system. Integrates OpenAI Vector Model for search and GPT-4 for text generation, enhancing the assistants capabilities.                           |

</details>

<details closed><summary>src.retrieval</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                    |
| [vector_search.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/retrieval/vector_search.py) | Implements a vector-based search to find top-k relevant documents given a query, leveraging cosine similarity. Ensures documents are loaded before searching, with configurable top-k results. Crucial for document retrieval within the smart assistant architecture. |
| [base_search.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/retrieval/base_search.py)     | Defines an abstract base class for search operations within the repositorys retrieval module. Specifies methods for setting and retrieving documents, as well as performing search operations on a given query.                                                        |

</details>

<details closed><summary>src.evaluation</summary>

| File                                                                                                                       | Summary                                                                                                                                                                                                                                                  |
| ---                                                                                                                        | ---                                                                                                                                                                                                                                                      |
| [rag_evaluator.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/evaluation/rag_evaluator.py)             | Calculates** BLEU, diversity, and speed scores for generated responses using RagPipeline. **Iterates** over evaluation data, **comparing** generated against reference, **displaying** metrics.                                                          |
| [retrieval_evaluator.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/evaluation/retrieval_evaluator.py) | Evaluates retrieval performance by calculating metrics like Precision@k, Recall@k, and MRR. Fetches evaluation data and uses a retrieval search method. Enables analysis of query relevance based on retrieved and relevant documents for each instance. |

</details>

<details closed><summary>src.preprocessing</summary>

| File                                                                                                              | Summary                                                                                                                                                    |
| ---                                                                                                               | ---                                                                                                                                                        |
| [text_splitter.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/preprocessing/text_splitter.py) | Enables text splitting into chunks based on a specified size using a customized tokenizer for the smart-assistant-rag repositorys preprocessing component. |

</details>

<details closed><summary>src.generation</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                   |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                       |
| [openai_generation.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/generation/openai_generation.py) | Generates text completions from OpenAI models based on user input prompts, utilizing OpenAI API for language generation. A subclass of BaseGeneration, it facilitates chat-like interactions by creating and processing model completions for natural language responses. |
| [base_generation.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/generation/base_generation.py)     | Defines an abstract base class for generating text output based on input prompts. This module acts as a blueprint for implementing text generation functionality within the smart assistant projects architecture.                                                        |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the smart-assistant-rag repository:
>
> ```console
> $ git clone https://github.com/gabechu/smart-assistant-rag
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd smart-assistant-rag
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run smart-assistant-rag using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/gabechu/smart-assistant-rag/issues)**: Submit bugs found or log feature requests for the `smart-assistant-rag` project.
- **[Submit Pull Requests](https://github.com/gabechu/smart-assistant-rag/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/gabechu/smart-assistant-rag/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/gabechu/smart-assistant-rag
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/gabechu/smart-assistant-rag/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=gabechu/smart-assistant-rag">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
