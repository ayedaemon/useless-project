PYTHON=python3



quick:
	sudo systemctl start docker

	@echo " [ + ] Building docker image ...."
	docker build \
	-f app1.dockerfile \
	-t flaskdev .


	@echo " [ + ] Starting Development Container.."
	docker run --rm -it \
	--name flaskdev1 \
	-v ${PWD}:/app \
	-p 8000:8000 \
	flaskdev \
	bash -c "pip install -r requirements.txt && python app1.py"
