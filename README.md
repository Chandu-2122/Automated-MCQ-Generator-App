### [**- Automated MCQ Generator Using Langchain OpenAI API**]()

**Objective**: Create a tool to automatically generate MCQs based on input text using advanced AI techniques.

**Project Structure**:
- **experiment**: Contains experimental code and logger setup.
- **logs**: Directory for log files.
- **mcqgenrator.egg-info**: Metadata and configuration for the project package.
- **src**: Main source code directory.
  - **MCQGenerator.py**: Core script for generating MCQs.
  - **StreamlitAPP.py**: Streamlit application script.
  - **test.py**: Testing script.
- **data.txt**: Sample input data.
- **Response.json**: Sample response data.
- **requirements.txt**: List of required libraries.

**Libraries Used**:
- `openai`: Accesses the OpenAI API for language processing.
- `langchain`: Implements language chain models for text analysis.
- `streamlit`: Creates the web interface for the application.
- `python-dotenv`: Manages environment variables.
- `PyPDF2`: Extracts text from PDF files for generating MCQs.

**Functionality**:
- The application generates multiple-choice questions from provided text data.
- Utilizes OpenAI API for language processing to create relevant questions and answers.
- The Streamlit interface allows users to input text and view generated MCQs.

**Example**:
- User inputs text into the Streamlit app.
- The app processes the text using Langchain and OpenAI API.
- MCQs are generated and displayed to the user.

**Conclusion**:
- The project demonstrates the capability to automate MCQ generation using modern AI tools, improving efficiency in educational content creation.
