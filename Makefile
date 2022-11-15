.DEFAULT_GOAL := help

.PHONY: build run test help

build: ## Build the Dockerfile into a container
	docker compose build

run: build ## Run the docker container made from the Dockerfile
	docker compose up

test: ## GET python_app/ping then log a read from database. 
	docker compose run python_app python ./test.py

down: ## Run docker compose down. Leaves volumes
	docker compose down

rm-container: ## Removes stopped service containers.
	docker compose rm -f

rm-volume: ##
	docker volume rm redis-volume -f

help: ## Show this help
	#This is a mess of code that prints a pretty help via awk TODO make this simpler
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)  