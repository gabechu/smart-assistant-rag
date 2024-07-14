<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">SMART-ASSISTANT-RAG</h1>
</p>
<p align="center">
    <em>Unleash Intelligence, Elevate Your Conversations</em>
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

The smart-assistant-rag project is a sophisticated AI-powered smart assistant that leverages advanced natural language processing techniques. It seamlessly integrates various vector models such as Hugging Face and OpenAI for text encoding and response generation. The projects core functionalities include document retrieval through cosine similarity, text chunking for efficient processing, and high-quality query-based responses. By combining cutting-edge technologies in machine learning, the smart-assistant-rag project offers a valuable solution for personalized and contextually relevant interactions.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture with components like vector models, pipelines for retrieval and generation tasks, and preprocessing modules. It integrates Hugging Face and OpenAI for text encoding and response generation. |
| 🔩 | **Code Quality**  | The codebase maintains a high level of quality and follows the Black code style. It enforces type checking using MyPy and includes clean and efficient implementations for vector operations and text generation tasks. |
| 📄 | **Documentation** | The project includes detailed documentation via comments within the codebase explaining the purpose and functionality of each module and class. The `pyproject.toml` file captures essential project setup and dependencies. |
| 🔌 | **Integrations**  | Key dependencies include `torch`, `transformers` from Hugging Face, `openai`, and others for text processing, AI generation, and vector search functionalities. External libraries like `requests`, `cryptography` are used for API interactions and data security. |
| 🧩 | **Modularity**    | The codebase exhibits high modularity with distinct modules for vector models, retrieval pipelines, text generation, and preprocessing. Classes are well-encapsulated with clear responsibilities, promoting code reusability and maintainability. |
| 🧪 | **Testing**       | The project likely employs testing frameworks such as `pytest` for unit tests and possibly integration tests to ensure the functionality and correctness of critical components like vector search, generation pipelines, and text preprocessing. |
| ⚡️  | **Performance**   | The codebase emphasizes efficient vector operations and text processing, utilizing libraries like `torch` and `transformers` for optimized performance. The vector search algorithm with cosine similarity enables quick retrieval of relevant documents based on user queries. |
| 🛡️ | **Security**      | The project incorporates secure practices through dependencies like `cryptography` for data protection. Access control and data integrity measures may be implemented for handling sensitive information within the text processing and response generation workflows. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include `torch`, `transformers`, `openai`, `requests`, and `cryptography`, providing essential tools and APIs for text encoding, generation, and security implementations. |

---

##  Repository Structure

```sh
└── smart-assistant-rag/
    ├── poetry.lock
    ├── pyproject.toml
    └── src
        ├── __init__.py
        ├── data
        ├── generation
        ├── pipelines
        ├── preprocessing
        ├── retrieval
        ├── utils.py
        └── vector_models
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                             |
| ---                                                                                         | ---                                                                                                                                                                                                                                 |
| [pyproject.toml](https://github.com/gabechu/smart-assistant-rag/blob/master/pyproject.toml) | Defines project metadata and dependencies for the smart-assistant-rag repository. Manages Python version, libraries, testing tools, and build configuration. Captures essential details for project setup and development workflow. |

</details>

<details closed><summary>src</summary>

| File                                                                                | Summary                                                                                                                                                                                                       |
| ---                                                                                 | ---                                                                                                                                                                                                           |
| [utils.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/utils.py) | Calculates cosine similarity scores between a query vector and a set of document vectors. Implements efficient vector operations for retrieval tasks within the smart-assistant-rag repositorys architecture. |

</details>

<details closed><summary>src.vector_models</summary>

| File                                                                                                                                      | Summary                                                                                                                                                                                                                                                 |
| ---                                                                                                                                       | ---                                                                                                                                                                                                                                                     |
| [base_vector_model.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/vector_models/base_vector_model.py)                 | Defines an abstract class for encoding text data as vector representations, enforcing this behavior in subclasses.核                                                                                                                                     |
| [hugging_face_vector_model.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/vector_models/hugging_face_vector_model.py) | Implements Hugging Face vector model for text encoding. Utilizes AutoModel and AutoTokenizer to generate embeddings from input text. Implements mean pooling to average hidden states for each token, producing numpy arrays for downstream processing. |
| [openai_vector_model.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/vector_models/openai_vector_model.py)             | Implements OpenAI API integration in the vector model. Handles text embedding using specified model names and batch processing for efficient encoding of text data. Interacts with the parent repositorys vector models structure.                      |

</details>

<details closed><summary>src.pipelines</summary>

| File                                                                                                                                                                                  | Summary                                                                                                                                                                                                                 |
| ---                                                                                                                                                                                   | ---                                                                                                                                                                                                                     |
| [hugging_face_retrieval_openai_generation_pipeline.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/pipelines/hugging_face_retrieval_openai_generation_pipeline.py) | Implements a pipeline that utilizes Hugging Face for retrieval and OpenAI for generative responses. Integrates VectorSearch and RagPipeline functionalities for high-quality response generation based on user queries. |
| [rag_pipeline.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/pipelines/rag_pipeline.py)                                                                           | Defines RagPipeline integrating data loading, chunking, and search-generation process. Loads PDF data, splits chunks, and performs query-based response generation using retrieval and generation modules.              |
| [openai_retrieval_openai_generation_pipeline.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/pipelines/openai_retrieval_openai_generation_pipeline.py)             | Creates a pipeline for AI-powered question-answering. Utilizes OpenAI for text generation and vector search, improving response accuracy. Simplifies query-response generation for the smart assistant.                 |

</details>

<details closed><summary>src.retrieval</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                          |
| ---                                                                                                           | ---                                                                                                                                                                                                                                              |
| [vector_search.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/retrieval/vector_search.py) | Implements a vector search algorithm utilizing cosine similarity for document retrieval based on input queries using a specified vector model. Enables ranking top-k relevant documents for a given input query by leveraging vector embeddings. |
| [base_search.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/retrieval/base_search.py)     | Defines an abstract class providing methods for search functionality. Manages top-k results and document retrieval with an abstract search function, ensuring documents are set before searching.                                                |

</details>

<details closed><summary>src.preprocessing</summary>

| File                                                                                                              | Summary                                                                                                                                                                                                                                     |
| ---                                                                                                               | ---                                                                                                                                                                                                                                         |
| [text_splitter.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/preprocessing/text_splitter.py) | Enables text splitting using a specific tokenizer. Splits text into manageable chunks based on configured chunk size. This aids in processing large text inputs efficiently within the preprocessing module of the smart assistant project. |

</details>

<details closed><summary>src.generation</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                       |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                           |
| [openai_generation.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/generation/openai_generation.py) | Generates text responses using OpenAI API based on user prompts. Inherits from a base class, sets up OpenAI client with API key, and retrieves model-generated text in chunks. Falls under src/generation module in the repository structure. |
| [base_generation.py](https://github.com/gabechu/smart-assistant-rag/blob/master/src/generation/base_generation.py)     | Defines an abstract class for generating text based on a given prompt within the smart-assistant-rag repositorys architecture.                                                                                                                |

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
