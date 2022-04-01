# Similar foo using iptables
sudo iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 443 -j ACCEPT
sudo iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 4443 -j ACCEPT
sudo iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 8081 -j ACCEPT
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 4443

# If you're trying to forward for a localhost client, try adding the following:
sudo iptables -t nat -I OUTPUT -p tcp -o lo --dport 443 -j REDIRECT --to-ports 4443
