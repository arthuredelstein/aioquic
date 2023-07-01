python3 examples/http3_server.py --port 4433 --certificate /etc/letsencrypt/live/altsvc.privacytests2.org/fullchain.pem --private-key /etc/letsencrypt/live/altsvc.privacytests2.org/privkey.pem  -v &

python3 examples/http3_server.py --port 4434 --certificate /etc/letsencrypt/live/h3.privacytests2.org/fullchain.pem --private-key /etc/letsencrypt/live/h3.privacytests2.org/privkey.pem  -v &

python3 examples/http3_server.py --port 4435 --certificate /etc/letsencrypt/live/altsvc.privacytests3.org/fullchain.pem --private-key /etc/letsencrypt/live/altsvc.privacytests3.org/privkey.pem  -v &
