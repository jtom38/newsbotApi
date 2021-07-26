.PHONY: help
help: ## Shows this help command
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

test: ## Runs unit tests
	NEWSBOT_MODE='unittest'
	alembic upgrade head
	pytest

test-cleanup:  ## Use this to clean up the db when the test fails
	rm ./mounts/database/newsbot.db
	mv ./mounts/database/test.newsbot.db ./mounts/database/newsbot.db

test-ci: ## Runs unit tests without an existing db on disk. Ideal for CI/CD
	alembic upgrade head
	pytest

refresh: ## Removes temp data for a clean start
	rm ./newsbot.api.db

rmdatabase:
	rm ./newsbot.api.db

docker-build: ## Build docker image
	docker build -t newsbot-api:latest .

docker-run: ## Runs the application
	docker run 

freeze: ## Exports all installed python packages to the requirements.txt
	pip3 freeze > requirements.txt
