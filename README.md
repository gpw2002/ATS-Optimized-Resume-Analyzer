Here’s the raw content for your README file:

```markdown
# Track My Resume Application

**Track My Resume Application** is an advanced Applicant Tracking System (ATS) leveraging the power of the Gemini Pro LLM model for natural language processing, text classification, and analysis. This application simplifies the hiring process by allowing users to manage, track, and extract text from resumes in various formats such as PDF and DOCX, all through an intuitive web interface built with Streamlit.

## 🚀 Features

- **Resume Tracking**: Keep track of resumes and manage job applicants effectively.
- **Text Extraction**: Extract text content from various file formats (PDF, DOCX) for further analysis and processing.
- **Streamlit Interface**: Easy-to-use, interactive web-based user interface powered by Streamlit.
- **Natural Language Processing**: Utilize the Gemini Pro LLM for advanced text classification and analysis.
- **Google Generative AI Integration**: Enhanced capabilities with Google’s Generative AI to improve processing and decision-making.
- **Environment Management**: Seamless integration with `python-dotenv` for environment variable management and configuration.

## 🛠️ Tech Stack & Dependencies

The project relies on several powerful tools and libraries:

- **[Gemini Pro LLM](https://cloud.google.com/vertex-ai/docs/generative-ai/overview)**: Used for natural language processing and text classification.
- **[Streamlit](https://streamlit.io/)**: Framework for building fast, interactive web applications.
- **[Google Generative AI](https://cloud.google.com/)**: Advanced AI for enhanced functionality.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Used for managing environment variables.
- **[pdf2image](https://pypi.org/project/pdf2image/)**: Converts PDFs to images to facilitate text extraction.
- **[docx2txt](https://pypi.org/project/docx2txt/)**: Extracts text from DOCX files.
- **[PyPDF2](https://pypi.org/project/PyPDF2/)**: Handles PDF manipulation, reading, and text extraction.
- **[streamlit-lottie](https://pypi.org/project/streamlit-lottie/)**: Adds engaging Lottie animations to the Streamlit interface for better user experience.

## 🧩 Installation Guide

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

Start by cloning the project from GitHub:

```bash
git clone https://github.com/Gitesh08/Track-my-resume.git
```

### 2. Navigate to the Project Directory

```bash
cd Track-my-resume
```

### 3. Set Up a Python Virtual Environment

To keep dependencies isolated, create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Ensure you have a `.env` file for managing environment variables. Here's an example `.env` file structure:

```
# .env
API_KEY=your_google_api_key
MODEL=gemini_pro_model
```

### 6. Run the Streamlit Application

Once everything is set up, run the application using Streamlit:

```bash
streamlit run app.py
```

Open your browser and navigate to the provided local address to start using the app.

---

## 🎨 Application UI

The user-friendly interface provides the following sections:

1. **Upload Resume**: Upload PDF or DOCX resumes for processing.
2. **Extracted Text Display**: View and analyze the extracted text from uploaded resumes.
3. **Track Applications**: See all tracked resumes with insights into each applicant.
4. **AI-Powered Analysis**: Get resume insights using the Gemini Pro model for text analysis and classification.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, feel free to:

1. **Open an Issue**: Describe the feature/bug you're addressing.
2. **Submit a Pull Request**: Make sure your PR is clear and concise.

### Development Workflow:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request on GitHub.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 Acknowledgments

Special thanks to:

- **Google Cloud** for the Gemini Pro LLM and Generative AI.
- **Streamlit** for enabling rapid web app development.
```
