# Project_Kafka_Sport_Event
Real-time streaming of sports events using the messagin system Apache Kafka.

## Repository structure
```text
project/
  docker-compose.yml        # Docker Compose for Zookeeper, Kafka (Bitnami), and Kafdrop UI
  requirements.txt          # Python dependencies for producer and consumer
  .env.example              # Example environment variables for local setup
  sample_events.json        # Example sport event messages (for reference)

  src/
    producer.py             # Kafka producer simulating real-time sport match events
    consumer.py             # Kafka consumer showing events and live statistics

  scripts/
    create_topic.sh         # Helper script to create the 'sport.events' topic
    run_producer.sh         # Convenience script to run the Python producer
    run_consumer.sh         # Convenience script to run the Python consumer
```
You can push the `project/` folder as the root of your GitHub repository.

---
