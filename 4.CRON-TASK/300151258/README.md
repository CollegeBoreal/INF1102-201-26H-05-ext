## CRON Task – Nginx Log Monitoring

### Objective

The goal of this exercise is to monitor Nginx web server logs and automatically extract visitor IP addresses.
We created a shell script that analyzes the Nginx access logs and schedules it with **CRON** so it runs automatically every hour.

---

### 1. Extract IP addresses from Nginx logs

The Nginx access log is located at:

```
/var/log/nginx/access.log
```

To extract visitor IP addresses we used:

```bash
awk '{print $1}' /var/log/nginx/access.log
```

To remove duplicates:

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq
```

To save the unique IP addresses into a file:

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq > /home/ubuntu/nginx_ips.txt
```

---

### 2. Creating the automation script

We created a shell script called:

```
scruter_nginx.sh
```

Script content:

```bash
#!/bin/bash

# Log file
LOG_FILE="/var/log/nginx/access.log"

# Output file
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extract unique IP addresses
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Log execution timestamp
echo "Script executed on $(date)" >> /home/ubuntu/nginx_ips.log
```

---

### 3. Making the script executable

```bash
chmod +x scruter_nginx.sh
```

---

### 4. Testing the script

```bash
./scruter_nginx.sh
```

Verify results:

```bash
cat /home/ubuntu/nginx_ips.txt
```

---

### 5. Automating the task with CRON

Edit the cron table:

```bash
crontab -e
```

Add the following line:

```
0 * * * * /home/ubuntu/INF1102-201-26H-05/4.CRON-TASK/300151258/scruter_nginx.sh
```

This runs the script **every hour**.

Verify the scheduled task:

```bash
crontab -l
```

---

### 6. Checking the CRON service

```bash
systemctl status cron
```

This confirms that the scheduler is active and running.

---

### 7. Finding the most frequent visitors (bonus)

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr
```

This command counts how many times each IP address visited the server.

---

### Screenshots

Example outputs of the script and commands are included in the `images` folder.

1. Script execution
2. Extracted IP addresses
3. Cron configuration
4. Cron service status

---
## CRON Task – Nginx Log Monitoring

### Objective

The goal of this exercise is to monitor Nginx web server logs and automatically extract visitor IP addresses.
We created a shell script that analyzes the Nginx access logs and schedules it with **CRON** so it runs automatically every hour.

---

### 1. Extract IP addresses from Nginx logs

The Nginx access log is located at:

```
/var/log/nginx/access.log
```

To extract visitor IP addresses we used:

```bash
awk '{print $1}' /var/log/nginx/access.log
```

To remove duplicates:

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq
```

To save the unique IP addresses into a file:

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq > /home/ubuntu/nginx_ips.txt
```

---

### 2. Creating the automation script

We created a shell script called:

```
scruter_nginx.sh
```

Script content:

```bash
#!/bin/bash

# Log file
LOG_FILE="/var/log/nginx/access.log"

# Output file
OUTPUT_FILE="/home/ubuntu/nginx_ips.txt"

# Extract unique IP addresses
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Log execution timestamp
echo "Script executed on $(date)" >> /home/ubuntu/nginx_ips.log
```

---

### 3. Making the script executable

```bash
chmod +x scruter_nginx.sh
```

---

### 4. Testing the script

```bash
./scruter_nginx.sh
```

Verify results:

```bash
cat /home/ubuntu/nginx_ips.txt
```

---

### 5. Automating the task with CRON

Edit the cron table:

```bash
crontab -e
```

Add the following line:

```
0 * * * * /home/ubuntu/INF1102-201-26H-05/4.CRON-TASK/300151258/scruter_nginx.sh
```

This runs the script **every hour**.

Verify the scheduled task:

```bash
crontab -l
```

---

### 6. Checking the CRON service

```bash
systemctl status cron
```

This confirms that the scheduler is active and running.

---

### 7. Finding the most frequent visitors (bonus)

```bash
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr
```

This command counts how many times each IP address visited the server.


