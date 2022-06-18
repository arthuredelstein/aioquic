python3 examples/http3_server.py --port 4433 --certificate /etc/letsencrypt/live/altsvc.arthuredelstein.net/fullchain.pem --private-key /etc/letsencrypt/live/altsvc.arthuredelstein.net/privkey.pem  -v &
python3 examples/http3_server.py --port 4434 --certificate /etc/letsencrypt/live/h3.arthuredelstein.net/fullchain.pem --private-key /etc/letsencrypt/live/h3.arthuredelstein.net/privkey.pem  -v &
