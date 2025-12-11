# python-port-scanner
A lightweight network security tool designed to scan a target host for open ports, identify services, and provide clear results. This project is part of a cybersecurity learning series, progressing from simple tools to more advanced security automation.

---

## 🚀 Technology Stack

**Language:**  
- Python 3.x  

**Libraries:**  
- `socket` (core network scanning)  
- `sys` (command-line input)  
- `datetime` (logging timestamps, optional)  
- `threading` (for advanced version)  

**Platform:**  
- Works on macOS, Windows, and Linux  
- No external dependencies  

---

## 🎯 Project Scope

The goal of this project is to design and build a Python-based port scanner that teaches key cybersecurity and networking concepts. It is intentionally structured in *three upgrade stages* to mirror real development and skill progression:

1. **Networking fundamentals**  
2. **Socket programming in Python**  
3. **Automation and efficiency improvements**  
4. **Tool design and documentation best practices**  

This scanner will eventually evolve into a polished cybersecurity tool suitable for portfolio demonstration.

---

## 📘 What This Port Scanner Does

A port scanner helps security analysts:

- Identify which ports are open on a target device  
- Map ports to common services (e.g., 22 → SSH, 80 → HTTP)  
- Test security exposure and evaluate risk  
- Learn foundational reconnaissance techniques  

Core functionality:

1. Takes an IP or hostname.  
2. Attempts TCP connections to a list of ports.  
3. Determines if each port is **open** or **closed**.  
4. Outputs a clean, readable report.  

---

## 🧩 Project Design Overview  
Below are the major components we will develop:

### **1. Input Handling**
- Accept an IP or domain from the user.
- Validate the input and handle errors gracefully.
---
### **2. Scanning Logic**
- Use Python’s `socket` library to test connections.
- Measure response success/failure.
- Store results for reporting.
---
### **3. Service Mapping**
- Use a pre-built dictionary mapping ports to service names.  
- Examples:  
  - 22 → SSH  
  - 80 → HTTP  
  - 443 → HTTPS  
---
### **4. Output Formatting**
Produce a clean report such as:
```bash
Scanning host: 192.168.1.10...

Open Ports Found:
22/tcp - SSH
80/tcp - HTTP
443/tcp - HTTPS

Scan Complete.
```
---
## 🏗️ Development Roadmap (Three Upgrade Options)

### **Dev 01 — Simple Version (Beginner)**
A clean, educational starting point.
- Scan top 20 common ports  
- Sequential scanning  
- Clear and minimal code  
- Best for understanding fundamentals  

### **Dev 02 — Intermediate Version**
Builds on the simple version.
- Scan top 100 ports  
- Improved efficiency  
- Better error handling  
- Intro to performance tuning  

### **Dev 03 — Advanced Version (Portfolio-Ready)**
A powerful, professional-grade scanner.
- Full port range (1–65535)  
- Multi-threaded scanning  
- Service banner grabbing  
- Save results to `report.txt` or JSON  
- Color-coded terminal output  
- Optional progress bar  

This roadmap represents how a real security engineer progressively enhances tools.

---

## 🧠 Why This Project Matters

Port scanning is one of the most fundamental cybersecurity skills.  
Building your own scanner helps you understand:

- How networks communicate  
- How attackers discover exposure  
- How to automate reconnaissance  
- How services identify themselves  
- How to build real-world security tooling  

This project is a stepping stone toward more advanced tools such as:

- Vulnerability scanners  
- Network mappers  
- Intrusion detection scripts  
- Automated pentesting routines  

---

We will start with Option 1 as the foundation, then level up the tool over time.

---
## 📂 Repository Structure (recommended)
port-scanner/
│── scanner.py
│── README.md
│── utils/
│ └── common_ports.py
│── examples/
│ └── sample_output.txt
│── .gitignore
---

## ✨ Author
Cybersecurity student & Python developer building hands-on security tools as part of a practical learning roadmap.





