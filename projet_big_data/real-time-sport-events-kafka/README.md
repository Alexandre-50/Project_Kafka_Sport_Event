# Football Events Stream with Kafka

## Project Overview :
This project implements a **real-time event streaming pipeline** using **Apache Kafka** running on Docker.
The goal is to simulate a live sports feed (football matches) where events like goals, fouls, and cards are generated in real-time, ingested by Kafka, and processed by a consumer application to display live statistics.

## Chosen Tool : Apache Kafka
The main Big Data tool used in this project is **Apache Kafka**, combined with **Apache ZooKeeper** for coordination.

Kafka is a **distributed event streaming platform** designed to handle high-throughput, real-time data streams. It is widely used in industry for building data pipelines, streaming analytics, microservices communication, and real-time monitoring systems.

In this project :
- Kafka acts as the **central message broker**
- ZooKeeper manages broker coordination and metadata
- Python applications act as **producer** and **consumer**
- **Docker** ensures reproducible deployment

## Why we Selected This Tool ?
We selected Apache Kafka for several reasons:

First, Kafka is a **core technology in modern Big Data architectures**. It is designed to handle large volumes of streaming data with **low latency** and **high reliability**, which makes it ideal for real-time use cases such as live sports analytics, financial transactions, or IoT streams.

Second, Kafka enforces a **decoupled architecture** between producers and consumers. In this project, the event generator does not need to know how the data is consumed. This separation mirrors real-world systems where the same data stream can be consumed by dashboards, databases, or machine learning pipelines simultaneously.

Finally, Kafka integrates naturally with many other Big Data tools (Spark Streaming, Flink, Hadoop, Data Lakes), making it an excellent foundation for scalable data ecosystems.
---

## Folder Structure :
```text
real-time-sport-events-kafka/
├─ README.md                # Project documentation
├─ docker-compose.yml       # Kafka & Zookeeper stack configuration
├─ requirements.txt         # Python dependencies
├─ .env.example             # Environment configuration example
├─ scripts/
│ ├─ start_demo.ps1         # One-click demo script (Windows)
│ ├─ create_topic.sh        # Helper to create Kafka topics
│ └─ ...
├─ src/
│ ├─ producer_sports.py     # Component 1: Generates random match events
│ ├─ consumer_sports.py     # Component 2: Processes events & updates dashboard
│ ├─ config.py              # Configuration loader
│ └─ ...
├─ data/
│ └─ sample_output.jsonl    # Persisted data output
└─ screenshots/             # Proof of execution
```
---

## Installation & Setup

### 1. Prerequisites
*   **Docker Desktop** installed and running.
*   **Python 3.10+**.
*   **Git Bash** (optional, for shell scripts).
*   **PowerShell** (Windows)

### 2. Docker Stack Setup (Kafka + ZooKeeper)
1.  **Clone the repository** (or unzip the folder).

2.  **Start the Docker Stack** :
    The Kafka ecosystem is deployed using **Docker Compose**.
    From the project root directory, run:

     ```bash
     docker compose up -d
     ```
     This command launches :
    - ZooKeeper (port 2181)
    - Kafka broker (internal 9092, external 29092)
    - Kafka UI (port 8080)
  
    Launching Docker with container Kafka, Zookeeper :
    <img width="1600" height="896" alt="image" src="https://github.com/user-attachments/assets/eff6d959-ea59-4df9-b983-540e8a91bd18" />
    
    Docker container running :
    <img width="1600" height="5 53" alt="image" src="https://github.com/user-attachments/assets/ddd08531-b4ca-442d-ab0d-7aa2ef4da33d" />

3.  **Create the Kafka Topic** :
    Once Kafka is running, the topic used for streaming is created inside the Kafka container:
    
    ```bash
    docker exec -it kafka kafka-topics --bootstrap-server kafka:9092 `--create --topic sport.events --partitions 1 --replication-factor 1
    ```
    The topic used : 
    <img width="1600" height="188" alt="image" src="https://github.com/user-attachments/assets/e2ed90e6-ce4b-4d5a-b2bd-4d01bc6bcdd1" />

4.  **Install Python Dependencies** :
    ```bash
    python -m venv .venv
    # Windows:
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```
    The installation of python dependies with environments :
    <img width="1600" height="145" alt="image" src="https://github.com/user-attachments/assets/41de6624-cb9d-4947-ab9d-18f5f5038073" />
    Virtual environment activation :
    <img width="1600" height="99" alt="image" src="https://github.com/user-attachments/assets/27e75e7b-c73b-4e5a-9695-06df1593366d" />
---

## Minimal Working Example :
The project contains two different Python scripts:

1.  **`Producer (producer_sports.py)`**: It simulates multiple concurrent football matches. Every second, it randomly generates events such as:

    - GOAL

    - FOUL

    - YELLOW_CARD

    - SUBSTITUTION
and sends a JSON payload to the `sport.events` topic.

2. **`Consumer (consumer_sports.py)`**  
   The consumer subscribes to the same topic and:
   - Displays a real-time dashboard in the terminal using the rich library
   - Aggregates statistics (events per match, event distribution)
   - Writes raw events to data/sample_output.jsonl

   ```json
    {"event_id": "70d2633...", "event_type": "GOAL", "match_id": "match-1", "minute": 12, "payload": {"scorer": "Player A"}}
    {"event_id": "81a9241...", "event_type": "FOUL", "match_id": "match-2", "minute": 13, "payload": {"severity": "high"}}
    {"event_id": "92b1562...", "event_type": "YELLOW_CARD", "match_id": "match-1", "minute": 15, "payload": {"reason": "tackle"}}
   ```
   
   **Consumer raw events running :**

   <img width="600" height="569" alt="Consumer raw events" src="https://github.com/user-attachments/assets/35a2ca17-82fd-486e-bb85-d6462f6afbbf" />

---

## How to Run (Live Demo) :
We have created a PowerShell script to automate the demonstration and open the necessary terminals.

**Simply run:**
```bash
powershell.\scripts\start_demo.ps1
```

This will:
*   Open a **Producer** window (sending data).
*   Open a **Consumer** window (live dashboard).
*   Show the Docker status and data log in the main window.

---

## Screenshots of results :

Since this project runs in a verifiable environment, here are the actual execution logs proving the pipeline works:

### 1. Docker Status (`docker ps`)
```text
NAME                IMAGE                             STATUS
kafka               confluentinc/cp-kafka:7.6.1       Up
kafka-ui            provectuslabs/kafka-ui:latest     Up
zookeeper           confluentinc/cp-zookeeper:7.6.1   Up
```
Docker Container running : 
<img width="1600" height="553" alt="image" src="https://github.com/user-attachments/assets/a4b5e9ae-6bb0-4f19-a6d7-e4791633fb4d" />

### 2. Producer results : 
```text
[producer] bootstrap=localhost:29092 topic=sport.events
[producer] generating ~3 events/s across 5 matches
[bold green]GOAL[/bold green] in match-3 (min 17)
[yellow]YELLOW_CARD[/yellow] in match-4 (min 16)
[blue]SUBSTITUTION[/blue] in match-2 (min 18)
...
```
Producer terminal running :

![WhatsApp Image 2025-12-19 at 14 15 45](https://github.com/user-attachments/assets/dbd5d350-0c57-4495-bed6-e17592128301)

### 3. Consumer Output results :
The consumer displays a live table showing:

  - Total events processed

  - Last event received

  - Events per match

Distribution by event type : 

<img width="1599" height="379" alt="image" src="https://github.com/user-attachments/assets/fabd036c-26ea-424c-9921-9a3f91e83baa" />

---
## How Kafka Fits into a Big Data Ecosystem : 

Kafka acts as the ingestion and streaming layer of a Big Data architecture.

 - In a real-world system:

 - Producers ingest high-velocity data

 - Kafka stores and streams data reliably

 - Consumers process data in real time or batch mode

 - Downstream systems (Spark, Hadoop, ML pipelines, Data Lakes) consume Kafka topics

Kafka ensures scalability, fault tolerance, and real-time processing, which are essential characteristics of Big Data systems.
## Challenges & My Setup Notes

### Docker Networking on Windows
One specific challenge we encountered was connecting to Kafka running in Docker from our local Python scripts running on Windows in our laptops.
*   **Problem**: Initially, I got `NoBrokersAvailable`.
*   **Solution**: I learned about **Advertised Listeners**. I configured `docker-compose.yml` to expose port `29092` to the host (`EXTERNAL`) while keeping `9092` for internal Docker communication (`INTERNAL`).
    *   `KAFKA_ADVERTISED_LISTENERS: INTERNAL://kafka:9092,EXTERNAL://localhost:29092`
    *   My Python config uses `localhost:29092`.


























