<div align="center">

# 💼 Job Portal Backend API

### 🚀 A Production-Style REST API built with Python & Django

A secure and scalable **Job Portal Backend** built using **Django REST Framework**, featuring JWT authentication, role-based access control, job management, applications, resume uploads and protected APIs.

<br/>

<a href="https://jobportalbackend-uypb.onrender.com">
<img src="https://img.shields.io/badge/🚀_Live_API-Open_API-0F172A?style=for-the-badge" />
</a>

<a href="https://github.com/Sumit-1104/JobPortalBackend">
<img src="https://img.shields.io/badge/💻_Source_Code-GitHub-181717?style=for-the-badge&logo=github" />
</a>

<br/><br/>

<img src="https://img.shields.io/github/stars/Sumit-1104/JobPortalBackend?style=for-the-badge&logo=github" />
<img src="https://img.shields.io/github/forks/Sumit-1104/JobPortalBackend?style=for-the-badge&logo=github" />
<img src="https://img.shields.io/github/last-commit/Sumit-1104/JobPortalBackend?style=for-the-badge" />

</div>

---

# 📌 About The Project

**Job Portal Backend** is a RESTful API designed to power a modern job marketplace where candidates can discover and apply for jobs while employers can create, manage and review job applications.

The project demonstrates practical backend development using:

* 🐍 Python
* ⚡ Django
* 🔌 Django REST Framework
* 🔐 JWT Authentication
* 👥 Role-Based Authorization
* 🗄️ Database Management
* 📁 Resume/File Uploads
* 🔎 Job Search
* 📮 Application Management

The repository currently contains dedicated Django apps for **accounts, jobs and applications**, along with configuration, templates and static resources.

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔐 Authentication

* User Signup
* User Login
* JWT Authentication
* Protected APIs
* Token-based authorization

</td>

<td width="50%">

### 👥 User Roles

* Candidate
* Employer
* Role-based permissions
* Profile management
* Protected employer actions

</td>
</tr>

<tr>
<td width="50%">

### 💼 Job Management

* Create jobs
* Update jobs
* Manage jobs
* Job search
* Job listing APIs

</td>

<td width="50%">

### 📄 Applications

* Apply for jobs
* Resume upload
* Cover letter support
* Application tracking
* Employer application management

</td>
</tr>
</table>

These are the core capabilities currently documented for the repository.

---

# 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      Client/UI      │
                    │ Web / Mobile / App  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     REST API        │
                    │ Django REST         │
                    │ Framework           │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
       ┌───────────┐     ┌───────────┐     ┌──────────────┐
       │ Accounts  │     │   Jobs    │     │ Applications │
       │           │     │           │     │              │
       │ Auth      │     │ Job CRUD  │     │ Apply        │
       │ Profiles  │     │ Search    │     │ Resume       │
       │ Roles     │     │ Manage    │     │ Cover Letter │
       └───────────┘     └───────────┘     └──────────────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │      Database       │
                    │       SQLite        │
                    └─────────────────────┘
```

---

# 🧩 Project Structure

```text
JobPortalBackend/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
│
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
│
├── applications/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── static/
├── templates/
│
├── manage.py
├── requirements.txt
├── Procfile
├── render.yaml
└── README.md
```

The repository structure includes the three main application modules plus project configuration and deployment-related files.

---

# 🔐 Authentication Flow

```text
        User
         │
         ▼
    ┌───────────┐
    │  Signup   │
    └─────┬─────┘
          │
          ▼
    ┌───────────┐
    │   Login   │
    └─────┬─────┘
          │
          ▼
   ┌──────────────┐
   │ JWT Token    │
   └──────┬───────┘
          │
          ▼
 ┌───────────────────┐
 │ Protected API     │
 │ Authorization     │
 └─────────┬─────────┘
           │
           ▼
    ┌──────────────┐
    │ Role Check   │
    └──────┬───────┘
           │
      ┌────┴─────┐
      ▼          ▼
 Candidate    Employer
```

---

# 👤 User Roles

## 🎓 Candidate

Candidates can:

* Create an account
* Authenticate using JWT
* Manage their profile
* Search jobs
* Apply for jobs
* Upload resumes
* Submit cover letters
* Track applications

---

## 🏢 Employer

Employers can:

* Authenticate securely
* Create jobs
* Manage job listings
* View applications
* Manage candidate applications

---

# 🔌 API Modules

| Module                  | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| 🔐 **Accounts API**     | Authentication, users & profiles           |
| 💼 **Jobs API**         | Job creation, listing, search & management |
| 📄 **Applications API** | Job applications & application management  |
| 🛡️ **JWT Security**    | Protected API access                       |
| 📁 **Media**            | Resume/file uploads                        |

---

# 🛠️ Tech Stack

### Backend

<p>
<img src="https://skillicons.dev/icons?i=python,django" />
</p>

### API & Authentication

<p>
<img src="https://img.shields.io/badge/Django_REST_Framework-red?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/JWT-Authentication-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />
<img src="https://img.shields.io/badge/REST-API-005571?style=for-the-badge" />
</p>

### Database

<p>
<img src="https://skillicons.dev/icons?i=sqlite" />
</p>

### Development Tools

<p>
<img src="https://skillicons.dev/icons?i=git,github,vscode,postman" />
</p>

### Deployment

<p>
<img src="https://img.shields.io/badge/Render-Deployment-46E3B7?style=for-the-badge&logo=render&logoColor=black" />
</p>

---

# 🧪 API Testing

The API can be tested using **Postman**.

Typical development workflow:

```text
1. Register User
       ↓
2. Login
       ↓
3. Receive JWT Token
       ↓
4. Add Token to Authorization Header
       ↓
5. Access Protected APIs
       ↓
6. Create / Search / Apply
```

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Sumit-1104/JobPortalBackend.git
```

```bash
cd JobPortalBackend
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

---

## 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

# 🌐 Live Deployment

### 🚀 Live API

**https://jobportalbackend-uypb.onrender.com**

The project is configured for deployment with Render-related files such as `Procfile` and `render.yaml` in the repository.

---

# 📸 API Workflow Preview

```text
┌────────────────────────────────────────────┐
│              JOB PORTAL API                │
├────────────────────────────────────────────┤
│                                            │
│  🔐 Authentication                         │
│       │                                    │
│       ├── Signup                           │
│       └── JWT Login                        │
│                                            │
│  💼 Jobs                                   │
│       │                                    │
│       ├── Create Job                       │
│       ├── Search Jobs                      │
│       └── Manage Jobs                      │
│                                            │
│  📄 Applications                           │
│       │                                    │
│       ├── Apply                            │
│       ├── Resume                           │
│       ├── Cover Letter                     │
│       └── Application Management            │
│                                            │
└────────────────────────────────────────────┘
```

---

# 🎯 Project Goals

This project was built to demonstrate practical backend engineering concepts including:

* RESTful API design
* Django application architecture
* Authentication & authorization
* Role-based access control
* Database relationships
* File handling
* API testing
* Deployment
* Real-world business workflows

---

# 🔮 Future Improvements

Potential future enhancements include:

* 🔔 Email notifications
* 💬 Real-time messaging
* ❤️ Saved jobs
* 🔎 Advanced job filtering
* 📊 Employer analytics dashboard
* 🔔 Application status notifications
* ☁️ Cloud file storage
* 🐳 Docker support
* ⚙️ CI/CD pipeline
* 🧪 Automated API tests

---

# 📈 Developer Focus

```text
Python                  ████████████████████
Django                  ████████████████████
Django REST Framework   ███████████████████░
REST API                ███████████████████░
JWT Authentication      ██████████████████░░
SQL / Database          ██████████████████░░
Git & GitHub            ████████████████░░░░
```

---

# 👨‍💻 Author

<div align="center">

## **Sumit Satpute**

### Python & Django Developer

Building backend systems, REST APIs and full-stack web applications.

<br/>

<a href="https://github.com/Sumit-1104">
<img src="https://img.shields.io/badge/GitHub-Sumit--1104-181717?style=for-the-badge&logo=github" />
</a>

<a href="https://my-portfolio-sumit-1104.vercel.app">
<img src="https://img.shields.io/badge/🌐_Portfolio-Visit-000000?style=for-the-badge" />
</a>

</div>

---

<div align="center">

### ⭐ If this project helped you, consider giving it a star!

**Built with 🐍 Python + ⚡ Django + 🔌 REST API**

</div>
