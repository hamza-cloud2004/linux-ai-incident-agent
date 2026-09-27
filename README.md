# Red Hat & OpenAI-Powered Linux Incident Agent 🐧🤖

An enterprise-grade, high-reliability AI-powered incident response and troubleshooting agent built with Flask, Docker, Red Hat environment standards, and **OpenAI API** integration.
This tool helps detect, analyze, and resolve Linux system issues and logs with maximum **reliability**.

---

## 🚀 Key Features & Highlights
* **High Reliability:** Engineered for dependable, enterprise-grade incident detection and log analysis.
* **OpenAI API Integration:** Uses advanced OpenAI models to intelligently inspect and troubleshoot system incidents.
* **Red Hat / Linux Optimized:** Built to handle and analyze Red Hat and Linux system environments efficiently.
* **Flask Web Backend:** Provides an interactive API and robust chat interface (`app.py`).
* **Dockerized Environment:** Fully containerized with `dockerfile` and `docker-compose.yml` for seamless deployment.

---

## 🛠️ Tech Stack & Architecture
* **Python / Flask** (Backend API & Routing)
* **Docker & Docker Compose** (Containerization & Deployment)
* **OpenAI API** (Core AI & Intelligent Analysis Engine)
* **Red Hat Enterprise Linux (RHEL) / Linux** (Target Operating System & Log Environment)

---

## 📂 Project Structure
```text
├── app.py              # Main Flask application with OpenAI integration
├── dockerfile          # Container build instructions
├── docker-compose.yml  # Multi-container orchestration
├── requirements.txt    # Python dependencies
└── test_chat.py        # Script for testing AI incident response
