### @author - Saket Mishra

# Supply Chain Analytics for Robotics-as-a-Service (RaaS)

## 📌 Project Overview
This project presents an **end-to-end supply chain analytics solution** for a **Robotics-as-a-Service (RaaS)** company. The goal is to simulate a realistic, enterprise-grade supply chain environment and answer **strategic business questions** around demand planning, inventory optimization, SLA performance, and asset utilization.

The project is intentionally designed at a **Senior Supply Chain Analyst** level, emphasizing:
- Business problem framing
- KPI-driven analysis
- Scalable, config-driven Python pipelines
- Decision-oriented insights

Because real-world RaaS supply chain data is rarely public, this project uses a **synthetic but highly realistic dataset**, generated using industry-informed assumptions.

---

## 🏭 Business Context
A Robotics-as-a-Service company rents autonomous robots (AMRs, Picker Bots, Sorter Bots) to enterprise customers across multiple industries and regions. Customers pay monthly subscription fees with strict **SLA uptime commitments**.

Key supply chain challenges:
- High capital cost of robots
- Long manufacturing and refurbishment lead times
- Spare-parts availability driving uptime
- Balancing utilization vs. overstocking
- SLA penalties caused by downtime

---

## 🎯 Business Questions Answered

### 1️⃣ Are we holding the right level of robot and spare-parts inventory?
- Calculates **safety stock** and **reorder points** by robot type and region
- Uses service-level–based inventory modeling

### 2️⃣ Can we accurately forecast demand for robots?
- Builds a **time-series demand forecast** using historical contract commitments
- Supports mid-term capacity and procurement planning

### 3️⃣ Where are SLA breaches coming from?
- Analyzes downtime drivers by robot type and geography
- Identifies high-risk segments causing SLA violations

### 4️⃣ How efficiently are robots being utilized?
- Flags underutilized robot fleets
- Highlights working-capital inefficiencies

---

## 🗂️ Project Structure

```text
raas-supply-chain-analytics/
│
├── README.md
├── requirements.txt
├── config.yaml
│
├── data/
│   ├── raw/
│   │   └── raas_synthetic_data.csv
│   └── processed/
│
├── src/
│   ├── 01_generate_data.py
│   ├── 02_data_validation.py
│   ├── 03_inventory_analysis.py
│   ├── 04_demand_forecasting.py
│   ├── 05_sla_analysis.py
│   └── 06_utilization_analysis.py
│
├── outputs/
│   ├── figures/
│   └── metrics/
│
└── notebooks/
    └── exploratory_analysis.ipynb

