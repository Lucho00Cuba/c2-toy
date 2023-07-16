NAME := ""

build: SHELL:=/bin/bash
.SILENT: run
build:
	@if [[ ${NAME} == "" ]]; then echo ">>> NAME is not set"; exit 1; fi
	@docker build --no-cache --build-arg BUILD_DATE=`date -u +%Y-%m-%dT%H:%M:%SZ` -t ${NAME} .

rmi: SHELL:=/bin/bash
.SILENT: run
rmi:
	@if [[ ${NAME} == "" ]]; then echo ">>> NAME is not set"; exit 1; fi
	@docker rmi -f ${NAME}