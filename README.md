# ColdComposeAI

## Introduction

ColdComposeAI is a powerful tool that automates the process of writing cold emails for job applications. It takes a URL of a careers page, extracts job postings, and generates personalized emails based on your skills and experience. This project is designed for AI and Data Science professionals looking to streamline their job search.

## Features

  * **Job Scraping:** Extracts job postings directly from a company's career page.
  * **Skill Matching:** Matches your skills with the job requirements to tailor the email content.
  * **Personalized Email Generation:** Creates a unique and professional cold email for each job application.
  * **Portfolio Integration:** Automatically includes relevant links from your portfolio to showcase your work.
  * **Streamlit Interface:** Provides a simple and intuitive web interface for easy use.

## How It Works

1.  **URL Input:** You provide the URL of a job listings page.
2.  **Web Scraping:** The tool uses `WebBaseLoader` to fetch and clean the page content.
3.  **Job Extraction:** It then extracts job details like role, experience, skills, and description using a Large Language Model.
4.  **Portfolio Matching:** Your portfolio, stored in an Excel file, is queried to find the most relevant project links based on the required skills.
5.  **Email Generation:** A personalized email is drafted, addressing the specific job requirements and highlighting your capabilities, along with the selected portfolio links.

## Requirements

To run this project, you need to have the following installed:

  * Python 3.x
  * The libraries listed in the `requirements.txt` file, which can be installed using pip: `pip install -r requirements.txt`

## Setup and Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/waleedgul92/ColdComposeAI.git
    cd ColdComposeAI
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API key:**

      * Create a `.env` file in the root directory.
      * Add your Groq Cloud API key to the `.env` file:
        ```
        GROQ_API_KEY="your_api_key_here"
        ```

4.  **Prepare your portfolio:**

      * Create an Excel file named `portfolio.xlsx` in the `Data/` directory.
      * The file should have two columns: "Techstack" and "Links", listing your skills and corresponding portfolio URLs.

5.  **Run the application:**

    ```bash
    streamlit run code/main.py
    ```

6.  **Generate emails:**

      * Open your web browser and go to the Streamlit URL (usually `http://localhost:8501`).
      * Enter the URL of a careers page and click "Submit".
      * The generated emails will be displayed on the page.

## Project Structure

```
ColdComposeAI/
├── .gitignore
├── README.md
├── requirements.txt
├── code/
│   ├── chains.py
│   ├── data_cleaning.py
│   ├── main.py
│   └── portfolio.py
└── Data/
    └── portfolio.xlsx
```

