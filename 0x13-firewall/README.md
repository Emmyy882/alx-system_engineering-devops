# 0x13. Firewall


![V1HjQ1Y](https://github.com/Emmyy882/alx-system_engineering-devops/assets/110739304/5adbe626-f02d-45b7-ac6e-7e291bc0c2ab)

## background Context
### Your servers without a firewall

![holbertonschool-firewall](https://github.com/Emmyy882/alx-system_engineering-devops/assets/110739304/4cc60b80-93e4-4ffd-9483-7153804746ec)

Tasks
Task 0: Block all incoming traffic

Instructions on how to configure the firewall using ufw to block all incoming traffic except specific TCP ports (22, 443, 80).

Solution: 0-block_all_incoming_traffic_but

    In this task, we will configure the ufw firewall on the web-01 server to block all incoming traffic except for specific TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).
    
Steps:

    Install ufw (Uncomplicated Firewall):
    sudo apt update
    sudo apt install ufw

Configure ufw rules:

    sudo ufw default deny incoming # Deny all incoming traffic by default
    sudo ufw allow 22/tcp # Allow SSH port 22
    sudo ufw allow 80/tcp # Allow HTTP port 80
    sudo ufw allow 443/tcp # Allow HTTPS port 443

Enable the firewall:

    sudo ufw enable

Verify the rules:

    sudo ufw status

Ensure you can still SSH into the server (ssh user@web-01),

access the web server via HTTP (http://web-01), and access it via HTTPS (https://web-01)

