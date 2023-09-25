1. Set AWS credentials at ~/.aws/credentials
2. Download SSH private key at ~/.ssh/vockey.pem
3. Set the proper permissions for the key: `chmod og-rwx ~/.ssh/vockey.pem`
4. Install requirements: `pip install -r requirements.txt`
5. Install vim and less: `sudo apt update && apt install -y vim less`
6. Edit `inventory.yml` file and replace each server **public** DNS with the current ones. For the kafka_host node, you must use before created hadoop_master DNS.
7. Set up at flume-source/flume-source.conf (a1.sinks.avro_sink.hostname and a1.sinks.kafka_sink.kafka.bootstrap.servers) the **private** DNS of the master instance. 
8. Set up at kafka-consumer/kafka-consumer.py the **private** DNS of the master instance (where kafka is deployed).
9. Set up at kafka-install.yml ("Create weather-events topic" step) the **private** DNS of the master instance (where kafka is deployed). 
10. Set up at server.properties (listeners property) the **private** DNS of the master instance.
11. Install kafka and update flume: `ansible-playbook -i inventory.yml --key-file=~/.ssh/vockey.pem --user ec2-user kafka-install.yml`
12. Connect to each flume-source nodes and launch a different weather station on each, e.g.:

```
python random-events.py --name Bilbao --lat 43.26271 --long -2.92528 --wait 5 --output_dir /home/ec2-user/input
python random-events.py --name Donostia --lat 43.31283 --long -1.97499  --wait 5 --output_dir /home/ec2-user/input
python random-events.py --name Gasteiz --lat 42.84627 --long -2.67225  --wait 5 --output_dir /home/ec2-user/input
``` 
12. Connect to master instance and visualize the messages executing `python kafka-consumer/kafka-consumer.py`