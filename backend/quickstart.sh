
sudo systemctl start docker

echo " [ + ] Building docker image ...."
docker build -t flaskdev .


echo " [ + ] Starting Development Container.."
docker run --rm -it \
--name flaskdev1 \
-v $PWD:/app \
-p 8000:8000 \
flaskdev \
bash
