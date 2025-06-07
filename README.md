# aws-Cowrie-Honeypot

# AWS Cowrie Honeypot Project 🚀

This repository documents the process of deploying a **Cowrie honeypot** on an AWS EC2 instance to capture and analyze real-world attack data. It also includes Python scripts to automate log parsing and send alerts to Slack.

---

## 📌 Project Overview

✅ **Honeypot**: [Cowrie](https://github.com/cowrie/cowrie) (SSH/Telnet honeypot)  
✅ **Cloud Environment**: AWS EC2 (Ubuntu 22.04)  
✅ **Automation**: Python scripts for parsing logs and sending alerts  
✅ **Alerting**: Slack integration for real-time notifications

---

## ⚙️ Setup Steps

### 1️⃣ Launch EC2 Instance

- Use Ubuntu 22.04 AMI (t2.micro recommended)
- Configure Security Group:
  - Expose port `2222` (honeypot SSH/Telnet)
  - Admin SSH access on `22222` restricted to your IP

---

### 2️⃣ Install Dependencies & Cowrie

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3-venv python3-pip libssl-dev libffi-dev libpython3-dev build-essential libsqlite3-dev -y
