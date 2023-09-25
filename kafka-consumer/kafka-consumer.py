from kafka import KafkaConsumer

consumer = KafkaConsumer('weather-events', bootstrap_servers='ip-172-31-21-208.ec2.internal:9092')
for msg in consumer:
    print (msg)

