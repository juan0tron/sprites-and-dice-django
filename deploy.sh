echo "Enabling Virtualenv..."
source /home/sprites/sprites/bin/activate

echo "Downloading updates from Git..."
git checkout .
git pull

echo "Installing Python dependencies..."
pip install -r requirements.txt --quiet

echo "Gathering static files..."
./manage.py collectstatic --noinput

echo "Restarting Gunicorn..."
sudo systemctl restart gunicorn

echo "Restarting nginx..."
sudo nginx -t && sudo systemctl restart nginx

echo "Done!"