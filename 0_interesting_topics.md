## MESSAGE:
## If you are interested in collaborating and learning any of these topics, please send me an email at my work address.

zbigniew.galar@wz.uni.lodz.pl

Zbigniew Galar, PhD University of Lodz Department of Management

## Definitions
### Retrieval-Augmented Generation (RAG)
**Formal Definition** Retrieval-Augmented Generation (RAG) is a technique that optimizes the output of an AI model by referencing an authoritative knowledge base outside its training data before generating a response. Instead of relying solely on what the AI "memorized" during its creation, RAG allows the AI to look up specific, private, or real-time data (like your company's latest policy documents or inventory levels) to answer questions accurately.

**"The Open-Book Exam" analogy:**
- **Standard AI (without RAG):** Taking a **closed-book exam**. The student (AI) must rely entirely on their memory. If they don't know the answer, they might guess confidently (hallucinate) or give outdated information.
- **AI with RAG:** Taking an **open-book exam**. The student (AI) is allowed to open a textbook (your company’s data) to find the exact answer, cite the page number, and summarize it for you.

**Strategic Value**
- **Accuracy & Trust:** significantly reduces "hallucinations" (AI making things up) by grounding answers in your actual business data.
- **Cost Efficiency:** It is far cheaper than "fine-tuning" (retraining) a model. You don't need to retrain the AI every time your data changes; you just update the documents it reads.
- **Data Privacy:** It allows you to use a powerful public AI model (like GPT-4) without training your sensitive data _into_ the model. The AI reads your data only when necessary to answer a specific question.

### Model Context Protocol (MCP)
**Formal Definition** The Model Context Protocol (MCP) is an open technical standard that functions as a universal translator between AI models (like Claude, ChatGPT, or Gemini) and external data systems (like company databases, Slack, Google Drive, or CRMs). It standardizes how AI agents discover, access, and use data, eliminating the need for developers to build custom integrations for every specific tool.

**USB-C analogy:**
"USB-C for AI"** Just as a USB-C port allows you to connect a camera, printer, or hard drive to any laptop without needing a different custom cable for each device, MCP allows any AI model to plug into any software system instantly.

**Strategic Value**
- **Scalability:** Reduces the "N×M" integration problem (connecting _every_ AI to _every_ tool), significantly lowering development costs.
- **Interoperability:** Prevents vendor lock-in by allowing companies to switch AI models without rebuilding their data connections.
- **Security:** Provides a standardized, controlled layer for managing how AI agents access sensitive enterprise data.

### AI Agent vs. Standard Model Access (Chatbot)
- **Standard Model Access (Chatbot):** A passive, "stateless" interaction where the user inputs a prompt and the AI generates a text response based on its training. The AI outputs information but cannot interact with the outside world or perform actions on its own. It stops working the moment it finishes generating text.
- **AI Agent:** An autonomous system where the AI model acts as the "brain" or "controller." It is capable of reasoning through a problem, creating a plan, and using external tools (software, browsers, APIs) to execute that plan. It operates in a loop: perceiving, thinking, acting, and checking results until the goal is achieved.

**"The Consultant vs. The Intern" analogy:**
- **Standard Access (The Consultant):** You are in a room with a genius consultant. You can ask them _how_ to write a marketing email or analyze a spreadsheet. They will give you brilliant advice or write the text for you, but they cannot actually open your laptop, hit "send," or update the database. You (the human) must execute the work.
- **AI Agent (The Intern):** You have a capable intern. You say, "Check our CRM for leads who haven't replied in 3 months and send them a re-engagement email." The intern (Agent) logs into the CRM, filters the list, drafts the email, sends it, and reports back to you when finished.

**Strategic Value**
- **From "Content" to "Action":** Standard access is useful for _knowledge work_ (summarizing, drafting, brainstorming). Agents are useful for _operations_ (booking meetings, filing reports, coding software).
- **Autonomy:** Agents reduce the "human-in-the-loop" bottleneck. Instead of micromanaging the AI prompt-by-prompt, managers set a high-level goal ("Objective") and let the agent figure out the steps ("Chain of Thought").
- **Complexity Management:** Agents can handle multi-step workflows. If step 1 fails (e.g., "The website is down"), an agent can recognize the error and try a different approach; a standard model would simply hallucinate or stop.
#### Interactions
``` mermaid
graph TD
    %% 1. The Trigger
    subgraph "Demand Side"
        A("Business Request")
    end

    %% 2. The Orchestrator
    subgraph "AI Core (The Brain)"
        B{"AI Agent"}
        B_Note["Functions: Reasoning, Planning & Decision Making"]
        B --- B_Note
    end

    %% 3. The Knowledge Source (RAG)
    subgraph "Knowledge Layer (RAG)"
        C[("Vector Database")]
        C_Content["Stores: Unstructured Data (Policies, PDFs, Historical Archives)"]
        C --- C_Content
    end

    %% 4. The Tooling Source (MCP)
    subgraph "Execution Layer (MCP)"
        D["MCP Server (Standardized Interface)"]
        E[("Live Enterprise Systems")]
        E_Content["Stores: Structured Data (SQL, CRMs) & APIs"]
        D --- E
        E --- E_Content
    end

    %% 5. The Result
    subgraph "Supply Side"
        F("Business Outcome / Action")
    end

    %% Interactions
    A --> B
    
    %% RAG Loop: Checking "What do we know?"
    B -- "1. Retrieve Context" --> C
    C -- "2. Provide Augmented Context" --> B

    %% MCP Loop: Checking "What is happening now?"
    B -- "3. Request Tool Access" --> D
    D -- "4. Return Real-Time Data" --> B

    %% Final Synthesis
    B --> F
```

## Links
### Graph DB and knowledge graphs
**A graph database that supports more than 10 billion vertices & edges, high performance and scalability:**
https://github.com/apache/incubator-hugegraph
**Convert any text into a graph of knowledge given an ontology:**
https://github.com/rahulnyk/graph_maker
**AI Powered Knowledge Graph Generator:**
https://github.com/robert-mcdermott/ai-knowledge-graph
**Graph powered knowledge base:**
https://github.com/perstarkse/minne/
**Memento MCP: A Knowledge Graph Memory System for LLMs:**
https://github.com/gannonh/memento-mcp/
**Persistent memory for AI models through a local knowledge graph:**
https://github.com/shaneholloman/mcp-knowledge-graph/
**3D Graph RAG:**
https://github.com/ChristopherLyon/graphrag-workbench/
**GraphSearch: An Agentic Deep Searching Workflow for Graph Retrieval-Augmented Generation:**
https://github.com/DataArcTech/GraphSearch/
**Knowledge graphs from text with visualization:**
https://github.com/stair-lab/kg-gen
**Open source graph database with Cypher queries:**
https://kuzudb.com/
**Cloud native vector database:**
https://github.com/weaviate/weaviate
**Convert any text into knowledge graph with GPT 3:**
https://github.com/varunshenoy/GraphGPT
**A Streamlit application that extract graph data (entities and relationships) from text input using LangChain and OpenAI's GPT models, and generates interactive graphs:**
https://github.com/thu-vu92/knowledge-graph-llms
**Loading CSV or JSON into Neo4j:**
https://github.com/rush-db/rushdb
### Prompt engineering
**Vibe coding tutorial:**
https://github.com/EnzeD/vibe-coding/
**Structured prompt builder:**
https://github.com/Siddhesh2377/structured-prompt-builder/
**Running many agents in parallel:**
https://github.com/wandb/catnip/
**Local chat with PDFs:**
https://github.com/jacoblee93/fully-local-pdf-chatbot/
**Virtual desktop for agents:**
https://github.com/cyberdesk-hq/cyberdesk/
**Transform any app idea into working code through 5 AI-powered stages using the latest 2025 AI models:**
https://github.com/KhazP/vibe-coding-prompt-template/
**GitHub for prompts:**
https://github.com/newdee/prompt-shelf
**Awesome Anthropic prompts:**
https://github.com/langgptai/awesome-claude-prompts
**AI engineering book repository:**
https://github.com/chiphuyen/aie-book?tab=readme-ov-file
**Anthropic courses on prompt engineering:**
https://github.com/anthropics/courses
**Help others understand AI agents:**
https://github.com/NeoVertex1/SuperPrompt
**Repository dedicated to collecting and sharing AI prompts, best practices, and curated rules for developers:**
https://github.com/instructa/ai-prompts
**GitHub Copilot tutorial:**
https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming
**Leaked system prompts by elder-plinius:**
https://github.com/elder-plinius/CL4R1T4S
**Leaked system prompts:**
https://github.com/jujumilk3/leaked-system-prompts
**Anthropic's Prompt Engineering Interactive Tutorial:**
https://github.com/anthropics/prompt-eng-interactive-tutorial
**Simplest GenAI that can be trained locally on GPT-2 level:**
https://github.com/karpathy/nanoGPT
**Repository for prompt engineering testing for a specific task:**
https://github.com/mshumer/gpt-prompt-engineer
**Reasoning models prompting:**
https://simonwillison.net/2025/Feb/2/openai-reasoning-models-advice-on-prompting/
**Source to prompt:**
[HTML file](<file:///C:\Main\4_Science\0_Sources\your-source-to-prompt.html>)
**Prompt management:**
https://github.com/Dicklesworthstone/your-source-to-prompt.html?tab=readme-ov-file
### Notes and Documentation
**Let Claude Code chat directly with NotebookLM for source-grounded answers based exclusively on your uploaded documents:**
https://github.com/PleasePrompto/notebooklm-skill
**Docify - Local-First AI Second Brain:**
https://github.com/keshavashiya/docify
**PDF to Markdown and Word Converter:**
https://github.com/murtaza-nasir/pdf3md
**Your AI second brain for saving and organizing everything that matters:**
https://github.com/supermemoryai/supermemory
**Personal note-taking and documentation platform:**
https://github.com/timothepoznanski/poznote
**Publishing Obsidian notes as website:**
https://github.com/oleeskild/obsidian-digital-garden
**Bookmarks management:**
https://github.com/linkwarden/linkwarden
**Collaborative note taking:**
https://github.com/hackmdio/codimd/
**AI dictation and note taking app:**
https://github.com/amicalhq/amical/
**Speech to text using OpenAI Whisper:**
https://github.com/HeroTools/open-whispr/
**Extract tabular data from PDFs:**
https://github.com/camelot-dev/excalibur/
**Command Line Interface (CLI) for Mermaid diagrams:**
https://github.com/mermaid-js/mermaid-cli/
**Extract structured data from any text – automatically optimized for any LLM using DSPs:**
https://github.com/langstruct-ai/langstruct/
**DeepNotes is an open source, end-to-end encrypted infinite canvas tool with deep page nesting and realtime collaboration:**
https://github.com/DeepNotesApp/DeepNotes/
**Convert HTML to Markdown:**
https://github.com/matthewwithanm/python-markdownify/
**Create instant, fast, beautiful documentation with zero configuration:**
https://github.com/invertase/docs.page/
**Obsidian read it later:**
https://github.com/DominikPieper/obsidian-ReadItLater/
**Awesome Web scraping:**
https://github.com/lorien/awesome-web-scraping/
**Local Excalidraw Editor:**
https://github.com/tyrchen/excaliapp/
**Refactor PDFs and Doc into Markdown and JSON:**
https://github.com/axa-group/Parsr/
**Markdown Note-Taking App:**
https://github.com/Smaug6739/Alexandrie/
**Speech to text for any app:**
https://github.com/heyito/ito/
**GitHub profile README generator:**
https://github.com/rahuldkjain/github-profile-readme-generator/
**Build own website from markdown:**
https://github.com/Doctave/doctave/
**Text to diagrams:**
https://github.com/terrastruct/d2/
**Obsidian theme:**
https://github.com/Akifyss/obsidian-border
**JSON visualization tool:**
https://github.com/AykutSarac/jsoncrack.com/
**PDF annotation tool that runs entirely in your browser:**
https://github.com/rudi-q/leed_pdf_viewer
**Notes app with Markdown, checklists, images, tag chips, color themes etc.:**
https://github.com/nikunjsingh93/react-glass-keep
**Smart Composer is an Obsidian plugin that helps you write efficiently with AI by easily referencing your vault content:**
https://github.com/glowingjade/obsidian-smart-composer
**Gmail to SQLite:**
https://github.com/marcboeker/gmail-to-sqlite
**OpenAI chatGPT alternative GUI:**
https://github.com/billmei/every-chatgpt-gui
**An image of a math formula and returns corresponding LaTeX code:**
https://github.com/lukas-blecher/LaTeX-OCR
**Open source note app similar to Obsidian with Zettelkasten:**
https://github.com/Zettlr/Zettlr
**Open source note app similar to Obsidian:**
https://github.com/TriliumNext/Trilium
**Web scraping:**
https://github.com/firecrawl/firecrawl
**Private AI enables you to keep your data, models, and infrastructure under your control:**
https://github.com/tdi/awesome-private-ai
**PDF to Markdown and Word Converter:**
https://github.com/murtaza-nasir/pdf3md
**Presentations to markdown:**
https://github.com/ssine/pptx2md
**Downloading Youtube videos:**
https://github.com/NickvisionApps/Parabolic
**Documents sharing with encryption:**
https://github.com/cryptpad/cryptpad
**Awesome Obsidian:**
https://github.com/kmaasrud/awesome-obsidian
**HTML to Markdown:**
https://github.com/JohannesKaufmann/html-to-markdown
**Twitter X video downloader:**
https://github.com/ezshine/twitterxdownload
**Yaml resumes:**
https://github.com/yamlresume/yamlresume
**Everything to markdown:**
https://github.com/wisupai/e2m
**RSS Feed with AI:**
https://github.com/Seanium/FeedMe
**Voice cloning:**
https://github.com/myshell-ai/OpenVoice
**Local file manager:**
https://github.com/mickael-kerjean/filestash
**Automatic document classification, smart tagging, and semantic search using OpenAI-compatible APIs and Ollama:**
https://github.com/clusterzx/paperless-ai
**API designed for managing knowledge bases and files stored in vector databases—no GPU, internet, or cloud services required:**
https://github.com/mudler/LocalRecall
**Glass lives on your desktop, sees what you see, listens in real time, understands your context, and turns every moment into structured knowledge:**
https://github.com/pickle-com/glass
**Records and transcribes your meetings and generates powerful summaries from your raw meeting notes:**
https://github.com/fastrepl/hyprnote
**Various materials and tools that I use every day:**
https://github.com/trimstray/the-book-of-secret-knowledge
**Knowledge management system with RAG:**
https://github.com/GitHamza0206/simba
**Converting PDFs and images into clean, readable, plain Markdown text:**
https://github.com/chatdoc-com/OCRFlux
**Documents storage and management:**
https://github.com/papra-hq/papra
**Isometric diagrams:**
https://github.com/stan-smith/FossFLOW
**Progressive Web App (PWA) for creating beautiful isometric diagrams:**
https://github.com/stan-smith/FossFLOW
**Youtube videos transcripts summarizer:**
https://github.com/jaye773/youtube-summarizer
**A modern diagram scripting language that turns text to diagrams:**
https://github.com/terrastruct/d2
**Turns Codebase into Easy Tutorial with AI:**
https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge
**A lightweight static site generator for technical documentation:**
(Dory is a lightweight static site generator built for developers who want fast, clean, and customizable documentation — without the overhead of server-side rendering, complex CI/CD setups, or cloud-specific constraints.)
https://github.com/clidey/dory
**Changes normal code into prompt friendly text:**
https://github.com/cyclotruc/gitingest
**Knowledge from documents without hallucinations:**
https://github.com/arc53/DocsGPT
**Youtube transcriptions from videos:**
https://github.com/jdepoix/youtube-transcript-api
**RAG techniques - all different approaches:**
https://github.com/FareedKhan-dev/all-rag-techniques
**Open Source chatting with documents:**
https://github.com/Cinnamon/kotaemon
**Repository structure documentation to markdown:**
https://github.com/tesserato/CodeWeaver
**Download tool:**
https://github.com/imputnet/cobalt?tab=readme-ov-file
**Documents (pdf, office) to markdown or JSON:**
https://github.com/CatchTheTornado/text-extract-api
**Repository to diagram:**
https://github.com/ahmedkhaleel2004/gitdiagram
**Document analyzer:**
https://github.com/clusterzx/paperless-ai
**Book knowledge extractor and summarizer:**
https://github.com/echohive42/AI-reads-books-page-by-page
**Wiki, knowledge management, presentation and digital assets:**
https://github.com/BeeSyncAI/BeeSync
**Markitdown - convert Word, PDF documents to markdown:**
https://github.com/microsoft/markitdown
**Power Point to text:**
https://github.com/ALucek/ppt2desc
**Private encrypted note taking:**
https://github.com/streetwriters/notesnook
**Text to diagrams:**
https://github.com/terrastruct/d2
**Automatic presentation generation:**
https://github.com/icip-cas/PPTAgent
**Indexing scanned documents:**
https://github.com/paperless-ngx/paperless-ngx
**Web scraping:**
https://github.com/ScrapeGraphAI/Scrapegraph-ai
**Saving websites to a single HTML file:**
https://github.com/gildas-lormeau/SingleFile
**Documentation for the teams with collaboration features:**
https://github.com/outline/outline
**Time tracker for teams:**
https://github.com/solidtime-io/solidtime?tab=readme-ov-file
**Text dialogue to speech:**
https://github.com/nari-labs/dia
### Search
 **A lightweight yet powerful search tool designed for seamless integration with AI agents:**
https://github.com/sentient-agi/OpenDeepSearch
**Search markdown files:**
https://github.com/johannesjo/super-productivity
**Knowledge management for RAG systems:**
https://github.com/GitHamza0206/simba
**Deep Searcher:**
https://github.com/zilliztech/deep-searcher
**Knowledge graphs for finance:**
https://github.com/OpenSPG/openspg
**Knowledge graph with chat:**
https://medium.com/@jlowe_34257/chatting-with-your-knowledge-graph-53fdd3a84c63
**Retrieval-Augmented Generation (RAG) techniques:**
https://github.com/athina-ai/rag-cookbooks
**Knowledge Graph Builder App:**
https://github.com/neo4j-labs/llm-graph-builder
**R2R (Reason to Retrieve) AI retrieval system, supporting Retrieval-Augmented Generation (RAG):**
https://github.com/SciPhi-AI/R2R
**Visual based RAGs:**
https://github.com/tjmlabs/ColiVara
**Search Engine:**
https://github.com/typesense/typesense
**Documents search:**
https://github.com/gsidhu/buzee-tauri
**Temporal Knowledge Graphs for agentic applications:**
https://github.com/getzep/graphiti
### AI agents
**Visual workflow builder for creating AI agent pipelines:**
https://github.com/firecrawl/open-agent-builder
**Prometheus is a research-backed, production-ready platform that leverages unified knowledge graphs and multi-agent systems to perform intelligent operations on multilingual codebases:**
https://github.com/EuniAI/Prometheus
**Dynamic Kanban MCP Server v3.0:**
https://github.com/renatokuipers/dynamic-kanban-mcp
**A low code / no code tool for automating interactions with large language models:**
https://github.com/fluent-ai/fluent-ai
**Simple Implementations of Retrieval Augmented Generation (RAG) Systems:**
https://github.com/rasbt/RAGs
**Autonomous multi-agent coding framework that plans, builds, and validates software for you:**
https://github.com/AndyMik90/Auto-Claude/
**Open-source scaffolding for building your own AI-powered operating system:**
https://github.com/danielmiessler/Personal_AI_Infrastructure/
**Awesome AI coding tools:**
https://github.com/ai-for-developers/awesome-ai-coding-tools/
**MCP agents:**
https://github.com/nanobot-ai/nanobot/
**Agentic RAG for dummies with LangGraph:**
https://github.com/GiovanniPasq/agentic-rag-for-dummies/
**Curated collection of papers and resources on unlocking the potential of Agents through Reinforcement Learning:**
https://github.com/0russwest0/Awesome-Agent-RL/
**This template showcases a ReAct agent implemented using LangGraph, designed for LangGraph Studio. ReAct agents are uncomplicated, prototypical agents that can be flexibly extended to many tools.:**
https://github.com/langchain-ai/react-agent/
**Autonomous Data Science:**
https://github.com/ruc-datalab/DeepAnalyze/
**NeuralAgent is your AI personal assistant that actually _gets things done_:**
https://github.com/mosdehcom/neuralagent/
**Self Hosted AI RAG and MCP Platform:**
https://github.com/dilolabs/nosia/
**Private agent:**
https://agent.ii.inc/
**Build collaborative AI agents that work together, handle payments, and automate complex workflows:**
https://github.com/dcSpark/shinkai-local-ai-agents/
**LLM applications from scratch:**
https://github.com/hamzafarooq/building-llm-applications-from-scratch/
**This is a curated list of books for engineers on development with Large Language Models (LLMs):**
https://github.com/Jason2Brownlee/awesome-llm-books/
**Chat with your docs, use AI Agents, hyper-configurable, multi-user, & no frustrating setup required:**
https://github.com/Mintplex-Labs/anything-llm/
**Ask questions to your data in natural language:**
https://github.com/sinaptik-ai/pandas-ai/
**Better RAG:**
https://github.com/superagent-ai/reag
**Open Source Deep Research:**
https://github.com/HKUDS/Auto-Deep-Research
**LLM twin of a person:**
https://github.com/decodingml/llm-twin-course
**How to use AI agents to transform businesses:**
https://github.com/coleam00/ai-agents-masterclass
**Local PDFs to podcast conversion:**
https://github.com/Goekdeniz-Guelmez/Local-NotebookLM
**Local AI like DeepSeek and Liama from browser:**
https://github.com/sauravpanda/BrowserAI
**AI with spreadsheets (Excel):**
https://github.com/ianand/spreadsheets-are-all-you-need
**Introduction to deep learning, fastai and PyTorch:**
https://github.com/fastai/fastbook
**Learn AI engineering:**
https://github.com/ashishps1/learn-ai-engineering
**List of awesome AI applications:**
https://github.com/ai-collection/ai-collection
**List of free API LLMs:**
https://github.com/zukixa/cool-ai-stuff?tab=readme-ov-file
**Multi-AI Agents framework with self-reflection:**
https://github.com/MervinPraison/PraisonAI
**Windows AI agent:**
https://github.com/CursorTouch/Windows-Use
**Repository scraping for AI:**
https://github.com/coderamp-labs/gitingest
**Local RAG:**
https://github.com/dmayboroda/minima
**VS MCP server:**
https://github.com/juehang/vscode-mcp-server
**Jupyter MCP server:**
https://github.com/datalayer/jupyter-mcp-server
**Getting data from multiple databases with LLMs:**
https://github.com/clidey/whodb
**Context engineering is the delicate art and science of filling the context window with just the right information for the next step:**
https://github.com/davidkimai/Context-Engineering
**The repo is a guide to building agents from scratch:**
https://github.com/langchain-ai/agents-from-scratch
**OWL agents:**
https://github.com/camel-ai/owl
**Open Source Local no cloud Manus alternative with voice commands:**
https://github.com/Fosowl/agenticSeek
**Anthropic AI agents:**
https://github.com/Intelligent-Internet/ii-agent
**Visual building of agents:**
https://github.com/langflow-ai/langflow
**Working with Windows system with Claude paid 20$/month version:**
https://github.com/wonderwhy-er/DesktopCommanderMCP/blob/main/FAQ.md#how-much-does-it-cost-to-use-claude-desktop-commander
**Agents tutorial:**
https://github.com/patchy631/ai-engineering-hub
**Visual agents:**
https://github.com/MotiaDev/motia
**Prompt engineering courses:**
https://github.com/anthropics/courses
**Screen Parsing tool for Pure Vision Based GUI Agent:**
https://github.com/microsoft/OmniParser
**ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning:**
https://github.com/microsoft/ExACT
**AI agent for unit testing:**
https://github.com/BuilderIO/micro-agent
**AutoGen studio for agents with no code:**
https://github.com/microsoft/autogen/tree/main/python/packages/autogen-studio
https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
https://www.youtube.com/watch?v=oum6EI7wohM
**Agents made simple with JSON task lists:**
https://github.com/Pravko-Solutions/FlashLearn
**Simple agents:**
https://github.com/huggingface/smolagents
**Universal agents:**
https://github.com/All-Hands-AI/open-operator
**Web agents:**
https://github.com/huginn/huginn
**Coding agents:**
https://github.com/potpie-ai/potpie
**Agentic AI workflows:**
https://github.com/PrefectHQ/ControlFlow
**AI workflows and agents:**
https://github.com/julep-ai/julep
**Agents:**
https://github.com/NirDiamant/GenAI_Agents
**AI browser operator:**
https://github.com/web-infra-dev/midscene
### Visualizations
**Database schemas visualization:**
https://github.com/liam-hq/liam
**Markdown web pages:**
https://github.com/bloom42/markdown-ninja/
**Map showing the world's infrastructure:**
https://github.com/openinframap/openinframap/
**3D interactive flight path visualization:**
https://github.com/jeantimex/flight-path/
**iCraft Editor - Help you easily create stunning 3D architecture diagrams:**
https://github.com/gantFDT/icraft/
**Maps in [[Python]]:**
https://github.com/opengeos/leafmap
**Making a good Resume:**
https://github.com/srbhr/Resume-Matcher/
**SVG editor:**
https://github.com/MewPurPur/GodSVG/
**Security-first diagramming for teams:**
https://www.drawio.com/
**No code forms creator. Create beautiful, accessible forms and export:**
https://github.com/iduspara/shadcn-builder/
**Wallpapers:**
https://github.com/niumoo/bing-wallpaper/
**Application to manage Obsidian notes from terminal:**
https://github.com/erikjuhani/basalt
**Flow charts in ASCII:**
https://github.com/lewish/asciiflow
**Visualize your Markdown as mindmaps:**
https://github.com/markmap/markmap
**Prettymapp is a webapp and Python package to create beautiful maps from OpenStreetMap data:**
https://github.com/chrieke/prettymapp
**Change images into CAD 3D objects:**
https://github.com/ferdous-alam/GenCAD
**Free-and-open-source (FOSS) geographical information system (GIS):**
https://github.com/qgis/QGIS
**Edit, preview and share mermaid charts/diagrams:**
https://github.com/mermaid-js/mermaid-live-editor
**Text to Mermaid graphs:**
https://github.com/liujuntao123/smart-mermaid
**2D graphic editor:**
https://github.com/PixiEditor/PixiEditor
**Interactive visualizations for large embeddings:**
https://github.com/apple/embedding-atlas
**Generate slides from markdown:**
https://github.com/googleworkspace/md2googleslides
**A comprehensive analytics and data management platform:**
https://github.com/databuddy-analytics/Databuddy
**Datashader is a data rasterization pipeline for automating the process of creating meaningful representations of large amounts of data:**
https://github.com/holoviz/datashader
**Open source BI with website and markdown:**
https://github.com/evidence-dev/evidence
**Service logs visualization:**
https://github.com/grafana/grafana
**Knowledge graphs from text:**
https://github.com/robert-mcdermott/ai-knowledge-graph
**Business Intelligence:**
https://github.com/metabase/metabase
**Visualizations with AI:**
https://github.com/microsoft/data-formulator
**Visualize database schemas:**
https://github.com/liam-hq/liam?tab=readme-ov-file
**Visualization of GitHub repositories as diagram:**
https://github.com/ahmedkhaleel2004/gitdiagram
**Pack GitHub repository into AI friendly file:**
https://github.com/yamadashy/repomix
**Dataframes visualization:**
https://github.com/Kanaries/pygwalker
**Database schemas visualization:**
https://github.com/liam-hq/liam
### Business Management
**Curated list about Project Management interesting and useful topics:**
https://github.com/shahedbd/awesome-project-management
**Modern Warehouse Management System WMS:**
https://github.com/fjykTec/ModernWMS
**Real time collaborative project manager based on Kanban:**
https://github.com/easyflow-live/easyflow
**FlowInquiry is a free, open-source tool for managing projects, tickets, and requests:**
https://github.com/flowinquiry/flowinquiry
**Open Source CRM:**
https://github.com/twentyhq/twenty
**3D organization chart:**
https://github.com/bumbeishvili/org-chart/
**View data files (CSV, Excel) in terminal:**
https://github.com/forensicmatt/datatui/
**Generate Google slides from markdown:**
https://github.com/googleworkspace/md2googleslides
**Open source Grammarly alternative:**
https://github.com/zlwaterfield/scramble
**E-mail template builder:**
https://github.com/usewaypoint/email-builder-js
**[[Action items global]] application:**
https://github.com/johannesjo/super-productivity
**Awesome free applications:**
https://github.com/Axorax/awesome-free-apps
**Open source video calls:**
https://github.com/jitsi/jitsi-meet
**Virtual monitor for screen sharing:**
https://github.com/Stengo/DeskPad
**Extension allows you to create unique, random email addresses that forward to your real inbox:**
https://github.com/webmonch/hide-my-mail-cloudflare
**All-in-One AI Productivity Platform:**
https://github.com/dtyq/magic
**Knowledge management and collaboration:**
https://github.com/logseq/logseq
**Self hosting:**
https://github.com/mikeroyal/Self-Hosting-Guide
**Project management tool for tracking issues, sprints, and product roadmaps:**
https://github.com/makeplane/plane
**Collaborative drawing:**
https://github.com/excalidraw/excalidraw
**Alternatives to Saas products:**
https://github.com/RunaCapital/awesome-oss-alternatives
**Code review sources:**
https://github.com/joho/awesome-code-review
**Organize, and log your interactions with your family and friends:**
https://github.com/monicahq/monica
### Extract Transform Load ETL
**Solution to create and maintain small to medium volume data pipelines using the Extract & Load (EL) approach (DBtoDB, FStoDB, DBtoFS):**
https://github.com/slingdata-io/sling-cli
**Visual Data Preparation Powered by Python:**
https://github.com/amphi-ai/amphi-etl
**Your Open-Source AI Data Scientist:**
https://github.com/FireBird-Technologies/Auto-Analyst/
**Data Science for Beginners - A Curriculum:**
https://github.com/microsoft/Data-Science-For-Beginners/
**CSV Everything A Chrome Extension that converts images of tables or charts into downloadable CSV files using the OpenRouter API.:**
https://github.com/matsonj/csv-everything/
**SQL database management with AI:**
https://github.com/wannabespace/conar/
**Awesome Database Tools:**
https://github.com/mgramin/awesome-db-tools
**TreeSheets is a "hierarchical spreadsheet" that is a great replacement for spreadsheets:**
https://github.com/aardappel/treesheets
**[[Alteryx Designer]] alternative in [[Python]]:**
https://github.com/Edwardvaneechoud/Flowfile?tab=readme-ov-file
**Big CSV files edition:**
https://github.com/Tablecruncher/tablecruncher
**Data validation using Python type hints:**
https://github.com/pydantic/pydantic
**Data Engineer Handbook:**
https://github.com/DataExpert-io/data-engineer-handbook
**No code ETLs:**
https://github.com/nocobase/nocobase?tab=readme-ov-file
**[[Python]] pandas AI:**
https://github.com/sinaptik-ai/pandas-ai
**Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG:**
https://github.com/pathwaycom/pathway
### Linux
**Bash course:**
https://github.com/bahamas10/bash-course
**Linux customization:**
https://github.com/avtzis/awesome-linux-ricing/
**Linux data backups:**
https://github.com/bit-team/backintime
**How to secure [[Linux]] server:**
https://github.com/imthenachoman/How-To-Secure-A-Linux-Server
**Minimalistic Youtube experience:**
https://github.com/christian-fei/my-yt
**Linux software:**
https://github.com/luong-komorebi/Awesome-Linux-Software
**Home server management:**
https://github.com/IceWhaleTech/CasaOS
https://github.com/1Panel-dev/1Panel
**Self hosted Git service:**
https://github.com/go-gitea/gitea
**Open source e-mail:**
https://github.com/nizzyabi/Mail0
### Automation - Jobs displacement
**Actions are triggered by GitHub platform events directly in a repo and run on-demand workflows:**
https://github.com/sdras/awesome-actions
**Self hosted location history tracker:**
https://github.com/Freika/dawarich
**E-mail workflows automation:**
https://github.com/mxgoai/mxgo-core
**Automated Data Science:**
https://github.com/InnovatingAI/AutoMind
**Productivity:**
https://github.com/johannesjo/super-productivity
**Automation:**
https://github.com/HariSekhon/DevOps-Bash-tools
**Task automation with AI:**
https://github.com/danielmiessler/Fabric
**Mini Mouse Macro:**
https://sourceforge.net/projects/minimousemacro/
**Desktop customization:**
https://github.com/eythaann/Seelen-UI
### Research
**List of public real time datasets:**
https://github.com/bytewax/awesome-public-real-time-datasets
**Paper2Agent: Reimagining Papers As AI Agents:**
https://github.com/jmiao24/Paper2Agent
**Satellite tracking:**
https://github.com/thkruz/keeptrack.space/
**Paper to poster:**
https://github.com/Paper2Poster/Paper2Poster/
**A powerful AI-powered research tool that combines Firecrawl's web scraping capabilities with advanced AI reasoning to help you search, analyze, and understand web content.:**
**https://github.com/firecrawl/open-researcher/**
**A transparent peer-reviewed framework for pricing and risk analysis for a benchmarking, validation, training, teaching reference and an extensible foundation for tailored risk solutions:**
https://github.com/OpenSourceRisk/Engine/
**The Well: 15TB of Physics Simulations:**
https://github.com/PolymathicAI/the_well/
**Tools to work with ArXiv:**
https://github.com/artnitolog/awesome-arxiv/
**The level of detail 1 (LoD1) data of buildings across the globe:**
https://github.com/zhu-xlab/GlobalBuildingAtlas/
**Complete the Data Science undergraduate curriculum on your own time:**
https://github.com/ossu/data-science/
**Claude scientific skills:**
https://github.com/K-Dense-AI/claude-scientific-skills
**Paper to Agent. Automatically detects and runs all relevant tutorials from a research paper’s codebase:**
https://github.com/jmiao24/Paper2Agent
**Paper library - metadata scratcher:**
https://github.com/Future-Scholars/paperlib?tab=readme-ov-file
**AI Scientist:**
https://github.com/SakanaAI/AI-Scientist
**Best open source tools:**
https://oss.gallery/
**Chat with PDF documents with privacy:**
https://github.com/roe-ai/vectorless
**Organic Maps** is a privacy-first offline maps & GPS app for hiking, cycling, biking, and driving. Absolutely free:
https://github.com/organicmaps/organicmaps
**Paper to podcast:**
https://github.com/Azzedde/paper_to_podcast
**Understand any company inside out:**
https://github.com/exa-labs/company-researcher
**Platform empowers bootcamps, educators, and businesses to manage training programs:**
https://github.com/classroomio/classroomio
**Flash RAG for science research:**
https://github.com/RUC-NLPIR/FlashRAG
**Dialog from text:**
https://github.com/nari-labs/dia
**Fullstack app template combining React frontend and LangGraph backend with Gemini for web search and research automation:**
https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart
**Paper to TLDR poster:**
https://github.com/Paper2Poster/Paper2Poster
**Time series data analysis:**
https://github.com/facebookresearch/Kats
**Automated AI Scientist:**
https://github.com/SakanaAI/AI-Scientist
**Research assistant:**
https://github.com/dzhng/deep-research
**[[Artificial Intelligence]] concepts in [[Excel]]:**
https://github.com/ImagineAILab/ai-by-hand-excel
**Deep Research with small local AI:**
https://github.com/masterFoad/NanoSage
**Science animation:**
https://github.com/3b1b/manim
**Time Series model proposal:**
https://github.com/google-research/timesfm
**Article search with context:**
https://consensus.app/
**Build from scratch own technology:**
https://github.com/codecrafters-io/build-your-own-x
### Security
**Curated list of awesome free (mostly open source) forensic analysis tools and resources:**
https://github.com/cugu/awesome-forensics
**A secure, zero-knowledge password manager with end-to-end encryption:**
https://github.com/nerdylua/password-manager-web
**Airgapped Offline RAG:**
https://github.com/vincentkoc/airgapped-offfline-rag
**Personal data cloud:**
https://github.com/gyaaniguy/personal-drive
**Windows Startup processes manager:**
https://github.com/00000vish/Win-Startup-Manager
**A wearable device that captures what you say and hear in the real world and then transcribes and stores it on your own server:**
https://github.com/adamcohenhillel/ADeus
**Hacking Guide:**
https://github.com/0xbitx/Hacking-guide/
**OTP on a watch:**
https://github.com/0x4f53/Wristkey/
**A Linux program to create a Windows USB stick installer from a real Windows DVD or image:**
https://github.com/WoeUSB/WoeUSB-ng/
**Youtube player without recommendations and ads:**
https://github.com/hotheadhacker/youtube-player/
**Windows setting monitoring:**
https://github.com/nolesapex/DidMySettingsChange/
**Youtube local:**
https://github.com/user234683/youtube-local/
**Provable Cryptography for Bitcoin: An Introduction:**
https://github.com/cryptography-camp/workbook/releases
**Selfhosted `trashmail` solution - Receive Emails via `Web UI`, `JSON API`, `RSS feed` and `Custom Webhooks`:**
https://github.com/HaschekSolutions/opentrashmail/
**Enhances Windows by conveniently applying privacy, usability, and performance optimizations, all while maintaining functionality and customizability:**
https://github.com/Atlas-OS/Atlas/
**KeePass Tools:**
https://github.com/lgg/awesome-keepass/
**Remove Windows AI:**
https://github.com/zoicware/RemoveWindowsAI/
**RTranslator in real time phone application:**
https://github.com/niedev/RTranslator
**Maps built for transparency, privacy, and not-for-profit values. A fork of Organic Maps, originally based on Maps.ME.**
https://github.com/comaps/comaps/
**A list of free and open source forensics analysis tools and other resources:**
https://github.com/mesquidar/ForensicsTools/
**Direct cell phones communication:**
https://github.com/igatha/flare-gun
**Harden Windows Security:**
https://github.com/HotCakeX/Harden-Windows-Security
**Bypassing the DPI (Deep Packet Inspection) system without admin:**
https://github.com/GVCoder09/NoDPI
**Open source platform to securely manage remote access for any-sized organization as VPN replacement:**
https://github.com/firezone/firezone
**Password cracking tool:**
https://github.com/openwall/john
**Air-gapped data transfer:**
https://github.com/sz3/libcimbar
**Network-wide ad blocking via your own Linux hardware:**
https://github.com/pi-hole/pi-hole
**Rust version of Microsoft Remote Desktop Protocol, with a focus on security:**
https://github.com/Devolutions/IronRDP
**Personal Google drive:**
https://github.com/gyaaniguy/personal-drive
**AI-focused knowledge base of defensive countermeasures designed to help security professionals protect AI/ML systems from emerging threats:**
https://github.com/edward-playground/aidefense-framework
**Mesh communication with file sharing:**
https://github.com/markqvist/NomadNet
**Privacy tools list:**
https://github.com/pluja/awesome-privacy
**Secure notes on desktop and phone:**
https://github.com/streetwriters/notesnook
**Signing documents:**
https://github.com/OpenSignLabs/OpenSign
**Open source alternatives to software:**
https://github.com/piotrkulpinski/openalternative
**A self-hosted, open-source ingress-as-a-service platform:**
That allows you to expose applications and services running in private or local networks to the internet—securely, reliably, and without complex infrastructure.
https://github.com/wiredoor/wiredoor
**Disk encryption with strong security based on TrueCrypt:**
https://github.com/veracrypt/VeraCrypt
**A modern, cross-platform encryption tool designed to protect your sensitive data—whether it's text, files, or even embedded within images:**
https://github.com/OfficialAroCodes/AroCrypt
**Syncthing files between two computers:**
https://github.com/syncthing/syncthing
**Dead Man's Hand - execute when lack of input for a time:**
https://github.com/bkupidura/dead-man-hand
**DNS block list:**
https://github.com/hagezi/dns-blocklists
**Black Hat tools:**
https://github.com/UCYBERS/Awesome-Blackhat-Tools
**Secure file sharing with passkeys like Yubikey:**
https://github.com/RockwellShah/filekey
**Document signing:**
https://github.com/documenso/documenso
**Documents signing:**
https://github.com/docusealco/docuseal
### Cursor IDE
**Make Devin with Cursor rules:**
https://github.com/grapeot/devin.cursorrules
**Cursor rules:**
https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python-llm-ml-workflow-cursorrules-prompt-file/.cursorrules
**Cursor Agent an AI team and advanced skills:**
https://github.com/eastlondoner/cursor-tools
**Chat history with Cursor stored locally:**
https://github.com/specstoryai/getspecstory
### Python
**This Python training is for JPMorgan business analysts and traders, as well as select clients:**
https://github.com/jpmorganchase/python-training
**Python Time Series Analysis notebooks:**
https://github.com/FilippoMB/python-time-series-handbook
**Educational notebooks:**
https://github.com/marimo-team/learn/
**Business Intelligence dashboards in Python:**
https://github.com/holoviz/panel/
**GitHub repositories automatic wiki page:**
https://github.com/daeisbae/open-repo-wiki/
**Python visualization:**
https://github.com/pedroCabrera/PyFlow/
**Deepnote is a drop-in replacement for Jupyter with an AI-first design, sleek UI:**
https://github.com/deepnote/deepnote/
**Python package for concise, transparent, and accurate predictive modeling:**
https://github.com/csinva/imodels/
**Awesome vibe coding:**
https://github.com/filipecalegario/awesome-vibe-coding
**A Machine Learning Library for Time Series:**
https://github.com/salesforce/Merlion
**Python interactions:**
https://github.com/simonw/llm
**Python examples and tutorial code:**
https://github.com/geekcomputers/Python
**Analyze time series data:**
https://github.com/facebookresearch/Kats
**Cheat Sheets for Developers:**
https://github.com/Fechin/reference
**Data pipeline orchestrator:**
https://github.com/dagster-io/dagster
**Machine Learning case studies:**
https://github.com/Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies
**Cognitive load - how to write a good code:**
https://github.com/zakirullin/cognitive-load
**Jupyter Notebooks Lite in browser:**
https://github.com/jupyterlite/jupyterlite
**Modern open source Jupyter notebook alternative:**
https://github.com/pretzelai/pretzelai
**PDF manipulation in pure Python:**
https://github.com/py-pdf/pypdf
**Transfer entire project of py files into single text file:**
https://github.com/travisvn/gptree
**IDE editor that combines the simplicity of a code editor with a canvas UI that makes it easier to understand code:**
https://github.com/haystackeditor/haystack-editor
**Time series with transformers:**
https://github.com/VenkatachalamSubramanianPeriyaSubbu/multiresolution-time-series-transformer
**Tutorial for business analysts and traders, as well as select clients:**
https://github.com/jpmorganchase/python-training
**Awesome First Pull Request Opportunities:**
https://github.com/MunGell/awesome-for-beginners
**Time series forecasting:**
https://github.com/google-research/timesfm
**Executable files:**
https://github.com/pex-tool/pex?tab=readme-ov-file#documentation
