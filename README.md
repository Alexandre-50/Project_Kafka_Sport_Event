
# Kafka_Sport_Event 

## Project description
This project implements a **real-time sport events streaming pipeline** using **Apache Kafka** in the context of a Big Data course project.
The objective is to simulate **live sport events** (such as goals, fouls, substitutions, match start or end) that are continuously produced by a data source and immediately consumed by one or more consumer applications. This represent real-world scenarios where sport data must be processed and delivered with very low latency, for example for live score applications, real-time dashboards, or analytics platforms.

---

## Chosen Big Data tool
The main Big Data tool used in this project is **Apache Kafka**.
Apache Kafka is a **distributed event streaming platform** designed to handle large volumes of data with high throughput and low latency. It allows applications to publish, store, and consume streams of records in real time. Kafka is widely adopted in industry and is a central component of many Big Data architectures.

---

## Why use technology Apache Kafka ?
We chose **Apache Kafka** because it is particularly well suited for handling **continuous and real-time data streams**, such as live sport events (goals, fouls, substitutions, match status updates).
Kafka makes it possible to **publish and consume messages with very low latency**, while ensuring reliability, scalability, and a clear separation between producers and consumers. This decoupling allows different applications to consume the same stream of sport events independently, without impacting the data producers.
Kafka can also **store events durably**, meaning that messages are not lost even if a consumer application is not running at the time of production. Consumers can later replay past events using offsets, which is a key advantage in real-time systems.
For these reasons, Apache Kafka is an ideal solution for a **real-time sport events streaming project**.

## Project structure
```text
project/
  docker-compose.yml        # Docker Compose for Zookeeper, Kafka
  requirements.txt          # Python dependencies for producer and consumer
  .env.example              # Environment variables for local setup
  sample_events.json        # Sport event messages 

  src/
    producer.py             # Kafka producer simulating real-time football match 
    consumer.py             # Kafka consumer showing events and live statistics

  scripts/
    create_topic.sh         # Helper script to create the 'sport.events' topic
    run_producer.sh         # Convenience script to run the Python producer
    run_consumer.sh         # Convenience script to run the Python consumer
```
---
## Prerequisites

- **Docker** and **Docker Compose** installed
- **Python 3.9+** installed locally
- Git Bash  
  On Windows PowerShell you can either:
  - Run the commands manually, or
  - Use Git Bash to execute the different shell scripts.
---

## Installation and setup

### 1. You can clone and enter the project (optionnal)

```bash
git clone <your-github-url> Project_Kafka_Sport
cd Project_Kafka_Sport/project
```

### 2. Start Kafka (with Docker Compose)

From the `project/` directory:

```bash
C:\kafka
dir
```
This will start:
- `rt-sport-zookeeper` (Zookeeper)
- `rt-sport-kafka` (Kafka broker)
- `rt-sport-kafdrop` (Kafka UI on port 9000)
Then, we use the following command to install different librairies :
```bash
PS C:\Users\arcis\real-time-sport-events-kafka\real-time-sport-events-kafka> docker compose up -d
PS C:\Users\arcis\real-time-sport-events-kafka\real-time-sport-events-kafka> docker ps
```
## Screenshots
Launching Kafka
<img width="633" height="358" alt="Capture d’écran (6172)" src="https://github.com/user-attachments/assets/b6efb773-f3b4-4156-b966-ebc52ce29d26" />
Installation phase (docker-compose.yml)
<img width="1600" height="896" alt="image" src="https://github.com/user-attachments/assets/988547d1-3bcc-4090-90d7-ab4fb27788bc" />




