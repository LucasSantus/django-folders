help: ## Help comand
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST); \

migrate: ## Migrate Models
	python manage.py makemigrations home; \
	python manage.py migrate home; \
	python manage.py makemigrations folders; \
	python manage.py migrate folders; \
	python manage.py migrate \

clear: ## Clean project
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log

clear-db: ## Clean Database
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "migrations" -type d | xargs rm -rf
	@rm -rf db.sqlite3
