PYTHON=python3

BUILD_DIR=build

APP_NAME?=default
# quick:
# 	sudo systemctl start docker

# 	@echo " [ + ] Building docker image ...."
# 	docker build \
# 	-f app1.dockerfile \
# 	-t flaskdev .


# 	@echo " [ + ] Starting Development Container.."
# 	docker run --rm -it \
# 	--name flaskdev1 \
# 	-v ${PWD}:/app \
# 	-p 8000:8000 \
# 	flaskdev \
# 	bash -c "pip install -r requirements.txt && python app1.py"

app_auth: deps
	cp -rv blueprints/mod_auth_api ${BUILD_DIR}/${APP_NAME}/blueprints/
	cp -rv models/* ${BUILD_DIR}/${APP_NAME}/models/
	

app_scanner: deps
	cp -rv blueprints/mod_scanner ${BUILD_DIR}/${APP_NAME}/blueprints/


	


deps:
	mkdir -p ${BUILD_DIR}/${APP_NAME}/{blueprints,models}
	cp config.py ${BUILD_DIR}/${APP_NAME}/config.py
	cp extensions.py ${BUILD_DIR}/${APP_NAME}/extensions.py
	cp requirements.txt ${BUILD_DIR}/${APP_NAME}/requirements.txt
	cp app_${APP_NAME}.dockerfile ${BUILD_DIR}/${APP_NAME}/Dockerfile
	cp gunicorn_entry.sh ${BUILD_DIR}/${APP_NAME}/gunicorn_entry.sh
	cp app_${APP_NAME}.py ${BUILD_DIR}/${APP_NAME}/app.py


clean:
	rm -rf ${BUILD_DIR}/*


app:
	cp docker-compose.* ${BUILD_DIR}/docker-compose.yaml
	make app_${APP_NAME}

compose:
	docker-compose -f ./build/docker-compose.yaml up --build


all:
	make clean; make app APP_NAME=auth; make app APP_NAME=scanner;
	make compose