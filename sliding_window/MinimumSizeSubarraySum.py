""""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
arr = [1,4,4]
target = 4

n = len(arr)
l = 0
current_sum = 0
count = float('inf')
for r in range(n):
    current_sum += arr[r]
    while current_sum >= target:
        count = min(count,r-l+1)
        current_sum -= arr[l]
        l += 1
res = count if count != float("inf") else 0
print(res)


"""
I want to modify this.
let's start from the above, My perpective is I'll what I learn in this company what was my role in these work and then provide some heading of the work I have worked on or working.

Infosys:

1. I am mainly working as back-end developer, who take care how chatbot back-end logic should work. here my work around - prepared Agentic Rag based pipeline for chatbot workflow, custom tool building for chatbot which will work as a node of langgraph based pipeline, tool orchestration logic preparation, memory based query preparation  for better retrieve chunks from vector db along with hybrid search,  keywords extraction,  re-ranking etc applied NLP based technique, prompt engineering and persistence the generated answer, llm based answer preparation after getting retrieve chunks.
2. Also look into the chunking strategies and embedding techniques, code optimization using parallel threading etc, Managed code with git,  practicing debugging  and logical thinking.

technologies used: Agentic RAG, langgraph, langchain, Mongodb, reddis, Azure AI search,  vscode, python, windows, github, Jenkins, octopus. 

I have received  -  Rise Award  for (GenAI Engineering Contribution) and Insta Award – Infosys (High-impact AI Delivery)
 
Entomo:

1. I have worked as backend developer who work around deep learning based model building , model finetuning, for entity extraction from a documents or job description, prepared classification model and clustering, building a skill recomendation system.

technologies used:   BERT model, T5, GPT, embedding models, Huggingface, pytorch,tensorflow, Applied NLP techniques like token preparation, data clean up and prepration for training the model, python,vscode, linux
I have awared for optimising modelto improve its performance. 

Infowarehouse:

1. Working as a backend developer, where my work around to automate the data scraping from several website like amazon, flipkart, dmart etc, and another automate scraping work to extract cyber security pdf from a given website link. 
2. deep learning based model prepration for image classification (disease vs nutrient-deficiency classification for a various leave images)

technologies used: Webdriver, selenium, beautifulSoup, scikit-learn, deep learning based model : ResNet50, DenseNet121, VGG1, python vscode, linux.

Manhattan Tech Ventures
1. working as python backend developer, where my daily work around develop REST API using Falsk and FastAPI, automated data ingestion (.txt, .odf files) to MYSQL databse and mongo DB. 
2. develope automated scraping code to scrap the data from various website like housein.com, magicbrick etc.

technologies used: SQL, MOngoDB, Webdriver, selenium, beautifulSoup, python, linux.
"""

"""
%%%%%%%%%%%%%%%%%
% This is an sample CV template created using altacv.cls
% (v1.1.2, 1 February 2017) written by LianTze Lim (liantze@gmail.com). Now compiles with pdfLaTeX, XeLaTeX and LuaLaTeX.
% 
%% It may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%    http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2003/12/01 or later.
%%%%%%%%%%%%%%%%

%% If you need to pass whatever options to xcolor
\PassOptionsToPackage{dvipsnames}{xcolor}

%% If you are using \orcid or academicons
%% icons, make sure you have the academicons 
%% option here, and compile with XeLaTeX
%% or LuaLaTeX.
% \documentclass[10pt,a4paper,academicons]{altacv}
\documentclass[10pt,a4paper]{altacv}

%% AltaCV uses the fontawesome and academicon fonts
%% and packages. 
%% See texdoc.net/pkg/fontawecome and http://texdoc.net/pkg/academicons for full list of symbols.
%% 
%% Compile with LuaLaTeX for best results. If you
%% want to use XeLaTeX, you may need to install
%% Academicons.ttf in your operating system's font 
%% folder.


% Change the page layout if you need to
\geometry{left=1cm,right=1cm,marginparwidth=6.8cm,marginparsep=1.2cm,top=1.25cm,bottom=1.25cm}

% Change the font if you want to.

% If using pdflatex:
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[default]{lato}
\usepackage{hyperref}
\usepackage{wrapfig}
\usepackage{lipsum}
% If using xelatex or lualatex:
% \setmainfont{Lato}

% Change the colours if you want to
\definecolor{Mulberry}{HTML}{72243D}
\definecolor{SlateGrey}{HTML}{2E2E2E}
\definecolor{LightGrey}{HTML}{666666}
\colorlet{heading}{Sepia}
\colorlet{accent}{Mulberry}
\colorlet{emphasis}{SlateGrey}
\colorlet{body}{LightGrey}

% Change the bullets for itemize and rating marker
% for \cvskill if you want to
\renewcommand{\itemmarker}{{\small\textbullet}}
\renewcommand{\ratingmarker}{\faCircle}

%% sample.bib contains your publications
\addbibresource{sample.bib}

\begin{document}
\name{Moumita Jana}
\tagline{Generative AI Engineer | 4+ Years Experience}
% \photo{1cm}{Globe_High}

\personalinfo{%
  % Not all of these are required!
  % You can add your own with \printinfo{symbol}{detail}
  \email{jana12moumita@gmail.com}
  \phone{6296281183}
  % \mailaddress{Bangalore}
  \location{Hyderabad, India}
  \linkedin{\href{https://www.linkedin.com/in/moumita-jana-b97563208/}{moumita-jana}}
  \github{\href{https://github.com/janamoumita1997}{janamoumita1997}}\\
  \faCode{\href{https://leetcode.com/u/jana12moumita/}{leetcode.com/u/jana12moumita}}
  
  
  % \begin{wrapfigure}{r}{4cm}
  % \includegraphics[width=3cm]{Globe_High.png}
  % \end{wrapfigure}
  %% You MUST add the academicons option to \documentclass, then compile with LuaLaTeX or XeLaTeX, if you want to use \orcid or other academicons commands.
%   \orcid{orcid.org/0000-0000-0000-0000}
}

%% Make the header extend all the way to the right, if you want. Extend the right margin by 8cm (=6.8cm marginparwidth + 1.2cm marginparsep)
\begin{adjustwidth}{}{-8cm}
\makecvheader
\end{adjustwidth}
\cvsection{Key Skills}
% \begin{itemize}


\color{black}

\vspace{1mm}
\cvtag{Python} 
\cvtag{MongoDB}
\cvtag{Basic SQL}
\cvtag{FastAPI}
\cvtag{Flask}
\cvtag{Machine Learning}
\cvtag{NLP}
\cvtag{Generative AI}
\cvtag{Agentic AI}
\cvtag{LLMs(BERT,GPT,T5)}
\cvtag{RAG}
\cvtag{GraphRAG}
\cvtag{Prompt Engineering}
\cvtag{LangChain}
\cvtag{LangGraph}
\cvtag{Transformers}
\cvtag{PyTorch}
\cvtag{Azure Cloud}
\cvtag{Azure Batch}
\cvtag{Data Pipelines}
\cvtag{Large-scale Data Handling}
\cvtag{Docker}
\cvtag{GitHub}
\cvsection{Experience and Projects}

\cvevent{}{Backend Developer — Conversational AI \& GenAI Engineering, Infosys}{July'24--Present}{Bangalore}
\textbf{Role:} Backend Developer — Conversational AI \& GenAI Engineering

\textbf{What I Do:}
\begin{itemize}
    \item Designed and built an Agentic RAG-based pipeline for AI chatbot backend, including custom LangGraph tool nodes, tool orchestration logic, and response persistence.
    \item Implemented memory-based query formulation with hybrid search, keyword extraction, re-ranking, and NLP techniques to improve vector database retrieval quality.
    \item Handled prompt engineering, chunking strategies, embedding optimization, parallel threading for performance, and codebase management via Git, Jenkins, and Octopus.
\end{itemize}

\textbf{Technologies Used:} Agentic RAG, LangGraph, LangChain, MongoDB, Redis, Azure AI Search, Python, GitHub, Jenkins, Octopus, VS Code

\textbf{Recognition:} Rise Award — GenAI Engineering Contribution \textbar{} Insta Award — High-Impact AI Delivery


\cvevent{}{Backend Developer — Deep Learning \& NLP, Entomo (KPISoft)}{Mar'23--July'24}{Bangalore}
\textbf{Role:} Backend Developer — Deep Learning \& NLP

\textbf{What I Did:}
\begin{itemize}
    \item Built and fine-tuned deep learning models (BERT, T5, GPT) for entity extraction, classification, and clustering from documents and job descriptions.
    \item Developed a skill recommendation system and handled the full ML pipeline — data cleaning, token preparation, model training, evaluation, and performance optimization.
\end{itemize}

\textbf{Technologies Used:} BERT, T5, GPT, Embedding Models, HuggingFace, PyTorch, TensorFlow, Python, VS Code, Linux

\textbf{Recognition:} Awarded for optimizing model performance and improving overall system accuracy.



\cvevent{}{Backend Developer — Automation \& Deep Learning, Infowarehouse}{Sep'22--Jan'23}{Remote}
\textbf{Role:} Backend Developer — Automation \& Deep Learning

\textbf{What I Did:}
\begin{itemize}
    \item Automated data scraping from e-commerce platforms (Amazon, Flipkart, D-Mart) and built a pipeline to extract cybersecurity PDFs from target websites.
    \item Developed a deep learning image classification model to distinguish plant diseases from nutrient deficiencies across leaf images.
\end{itemize}

\textbf{Technologies Used:} Selenium, WebDriver, BeautifulSoup, Scikit-learn, ResNet50, DenseNet121, VGG16, Python, VS Code, Linux



\cvevent{}{Python Backend Developer — APIs \& Data Automation, Manhattan Tech Ventures}{Oct'21--Aug'22}{Kolkata}
\textbf{Role:} Python Backend Developer — APIs \& Data Automation

\textbf{What I Did:}
\begin{itemize}
    \item Developed REST APIs using Flask and FastAPI, and built automated data ingestion pipelines for .txt and .odf files into MySQL and MongoDB.
    \item Wrote web scraping scripts to collect structured data from real estate platforms like Housing.com and MagicBricks.
\end{itemize}

\textbf{Technologies Used:} Flask, FastAPI, MySQL, MongoDB, Selenium, WebDriver, BeautifulSoup, Python, Linux

\cvsection{EDUCATION:}
\color{black}
\begin{itemize}
    \item \textbf{Completed six-month Machine Learning mentorship program. (Mar'21-Sep'21)}
    \item M.Sc. Physics – Tezpur University
    \item B.Sc. Physics – Vidyasagar University
\end{itemize}
\clearpage
\end{document}

"""

