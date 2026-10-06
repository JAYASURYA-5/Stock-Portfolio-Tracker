# 📈 Stock Portfolio Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Chart.js-Visualization-orange?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js">
  <img src="https://img.shields.io/badge/HTML5-Web-red?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-Styling-blue?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-Frontend-yellow?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

<p align="center">
  <b>📊 Track • 💰 Calculate • 📈 Analyze • 📁 Export</b>
</p>

<p align="center">
  A modern Python-based stock portfolio management application with both a 
  <b>Flask Web Dashboard</b> and an interactive <b>Console CLI</b>.
</p>

---

## 🌟 Overview

**Stock Portfolio Tracker** is a Python-based application designed to make portfolio management simple and visual.

It allows users to manage their stock holdings, calculate investment values, monitor total portfolio value, visualize asset allocation, and export portfolio information.

The project provides **two different interfaces**:

| Interface | Description |
|---|---|
| 🖥️ **Console CLI** | Lightweight terminal-based portfolio management |
| 🌐 **Web Dashboard** | Interactive visual portfolio management |

---

## ✨ Features

<div align="center">

| 📊 Portfolio | 💰 Calculations | 📈 Analytics |
|:---:|:---:|:---:|
| Manage Holdings | Stock Value | Asset Allocation |
| Add Stocks | Portfolio Value | Interactive Charts |
| Update Quantity | Total Investment | Visual Dashboard |
| Remove Stocks | Individual Value | Portfolio Overview |

| 📁 Export | 🎨 UI | ⚡ Application |
|:---:|:---:|:---:|
| CSV Export | Modern Dark UI | Flask |
| TXT Export | Glassmorphism | Python |
| Data Backup | Responsive Design | CLI + Web |

</div>

---

## 🚀 Why Stock Portfolio Tracker?

Managing multiple investments manually can make it difficult to understand:

- How much money is invested?
- Which stock has the largest allocation?
- What is the total portfolio value?
- How many shares are owned?
- How can portfolio data be saved?

This project provides a **simple centralized solution** for managing and analyzing portfolio information.

---

# 💻 Console Version

The CLI provides a lightweight way to manage your portfolio directly from the terminal.

### Available Operations

```text
┌──────────────────────────────┐
│     STOCK PORTFOLIO CLI      │
├──────────────────────────────┤
│  1. View Stock Prices        │
│  2. Add Stock                │
│  3. Update Quantity          │
│  4. Remove Stock             │
│  5. View Portfolio           │
│  6. Calculate Total Value    │
│  7. Export Portfolio         │
│  8. Exit                     │
└──────────────────────────────┘
```

Run the console application:

```bash
python console_tracker.py
```

---

# 🌐 Web Dashboard

The Flask web application provides a more visual and interactive portfolio experience.

### Dashboard Includes

- 📊 Portfolio overview
- 💰 Total portfolio value
- 📈 Asset allocation chart
- ➕ Add holdings
- 🔄 Update holdings
- 🗑️ Remove holdings
- 📁 Export portfolio
- 🔔 Toast notifications
- 🌙 Modern dark-themed interface

Run the web application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# 📊 Portfolio Visualization

The dashboard uses **Chart.js** to visualize stock allocation.

```text
                    📊 Portfolio
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
        AAPL            MSFT           TSLA
          │              │              │
          └──────────────┼──────────────┘
                         │
                         ▼
               Allocation Calculation
                         │
                         ▼
                  📈 Chart.js
```

---

# 💰 Portfolio Calculation

The application calculates the value of each stock using:

```text
Investment Value = Stock Price × Quantity
```

### Example

```text
Stock       : AAPL
Price       : $178.50
Quantity    : 5

Investment Value
= 178.50 × 5
= $892.50
```

### Total Portfolio

```text
Total Portfolio Value
=
AAPL Value
+ MSFT Value
+ TSLA Value
+ ...
```

### Asset Allocation

```text
Allocation %
=
Individual Stock Value
──────────────────────── × 100
Total Portfolio Value
```

---

# 📈 Supported Stocks

The current application contains predefined reference prices for:

| Symbol | Company |
|:---:|---|
| 🍎 **AAPL** | Apple |
| 🪟 **MSFT** | Microsoft |
| 🔎 **GOOGL** | Google |
| 📦 **AMZN** | Amazon |
| 🚗 **TSLA** | Tesla |
| 💻 **NVDA** | NVIDIA |
| 👤 **META** | Meta |
| 🎬 **NFLX** | Netflix |
| 🔴 **AMD** | AMD |
| 💻 **INTC** | Intel |

> ⚠️ These are predefined project values and are **not live market prices**.

---

# 🛠️ Tech Stack

<p align="center">

| Technology | Role |
|:---:|---|
| 🐍 **Python** | Core application logic |
| 🌐 **Flask** | Web framework |
| 🧱 **HTML5** | Web structure |
| 🎨 **CSS3** | UI styling |
| ⚡ **JavaScript** | Frontend interaction |
| 📊 **Chart.js** | Data visualization |
| 📄 **CSV** | Data export |
| 🔧 **Git** | Version control |

</p>

---

# 🏗️ Architecture

```text
                         👤 USER
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       🖥️ Console CLI              🌐 Web Dashboard
              │                         │
              │                       Flask
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                  📊 Portfolio Logic
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
          Holdings       Prices      Calculations
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                   💰 Portfolio Value
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
             📈 Charts          📁 Export
```

---

# 🔄 Application Flow

```text
                    START
                      │
                      ▼
              Choose Interface
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
       Console                  Web App
          │                       │
          └───────────┬───────────┘
                      ▼
                Select Stock
                      │
                      ▼
                Enter Quantity
                      │
                      ▼
             Calculate Value
                      │
                      ▼
            Portfolio Summary
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      📊 Analyze              📁 Export
          │                       │
          ▼                       ▼
       Chart.js               CSV / TXT
```

---

# 📂 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── 📁 static/
│   ├── 📁 css/
│   │   └── style.css
│   │
│   └── 📁 js/
│       └── app.js
│
├── 📁 templates/
│   └── index.html
│
├── 🐍 app.py
│
├── 🐍 console_tracker.py
│
├── 📄 requirements.txt
│
├── 📄 .gitignore
│
└── 📖 README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/JAYASURYA-5/Stock-Portfolio-Tracker.git
```

### 2️⃣ Enter the Project

```bash
cd Stock-Portfolio-Tracker
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

## 🖥️ Console Application

```bash
python console_tracker.py
```

## 🌐 Web Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 📁 Export Portfolio

Portfolio information can be exported into:

### 📊 CSV

Perfect for:

- Microsoft Excel
- Google Sheets
- Data analysis
- Record keeping

### 📄 TXT

Useful for:

- Simple reports
- Backup
- Quick viewing

---

# 🎨 UI Highlights

The web dashboard focuses on a modern financial-dashboard style.

### Design Features

- 🌙 Dark theme
- ✨ Glassmorphism
- 🌈 Gradient effects
- 💡 Glowing UI elements
- 🔔 Toast notifications
- 📊 Interactive charts
- 📱 Responsive layout
- 🎯 Simple navigation

---

# 🔐 Data Handling

The web version uses **session-based portfolio storage** to maintain the user's current portfolio during the application session.

The current project uses predefined stock prices rather than a live stock-market API.

---

# 🚀 Future Enhancements

The project can be extended with:

### 📡 Live Market Data

Integrate APIs such as:

- Alpha Vantage
- Finnhub
- Twelve Data
- Yahoo Finance

### 📊 Advanced Analytics

- Profit & Loss
- Daily returns
- Annual returns
- Portfolio performance
- Risk analysis
- Historical charts

### 🔔 Smart Alerts

- Price alerts
- Target price notifications
- Portfolio change notifications

### 👤 User Accounts

- Registration
- Login
- Multiple portfolios
- Cloud storage
- Personalized dashboard

### 📱 Mobile App

Create Android/iOS applications for portfolio monitoring.

### ☁️ Cloud Deployment

Deploy the application using cloud platforms for access from anywhere.

---

# 🎯 Project Objectives

- 📊 Simplify stock portfolio management.
- 💰 Calculate investment values automatically.
- 📈 Visualize portfolio allocation.
- 📁 Provide easy data export.
- 🖥️ Support both CLI and web interfaces.
- 🎨 Create a modern financial dashboard.
- 🧑‍💻 Demonstrate practical Python and Flask development.

---

# 🌟 Key Benefits

```text
             📈 STOCK PORTFOLIO TRACKER
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
     💰 Manage       📊 Analyze       📁 Export
        │               │                │
        ▼               ▼                ▼
    Holdings        Allocation        CSV/TXT
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                 🎯 Better Overview
```

---

# 🎓 Learning Outcomes

This project demonstrates practical experience in:

- Python programming
- Flask development
- Web application development
- HTML & CSS
- JavaScript
- Data visualization
- Portfolio calculations
- File handling
- CSV generation
- Session management
- Git & GitHub

---

# 🔮 Future Vision

The goal is to evolve this project from a simple portfolio tracker into a complete **personal investment dashboard** featuring:

```text
📊 Portfolio
   +
📈 Live Market Data
   +
💰 P&L Analytics
   +
🔔 Smart Alerts
   +
🤖 AI Insights
   +
☁️ Cloud Sync
   =
🚀 Complete Investment Platform
```

---

# 👨‍💻 Developer

### Jayasurya K

🎓 Student Developer | 💻 Full Stack Developer | 🤖 AI Enthusiast

**GitHub:**  
https://github.com/JAYASURYA-5

---

# 🔗 Project

### 📈 Stock Portfolio Tracker

**Repository:**  
https://github.com/JAYASURYA-5/Stock-Portfolio-Tracker

---

# ⭐ Show Your Support

If you like this project:

⭐ **Star the repository**  
🍴 **Fork the project**  
🐛 **Report issues**  
💡 **Suggest improvements**

---

<div align="center">

## 📈 Track Your Stocks. Understand Your Portfolio. Make Better Decisions.

### Built with ❤️ using Python & Flask

**© 2026 Jayasurya K**

</div>
