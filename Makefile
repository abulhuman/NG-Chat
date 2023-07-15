.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m source.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m source.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python -m source.manage runserver

.PHONY: shell
shell:
	poetry run python -m source.manage shell

.PHONY: superuser
superuser:
	poetry run python -m source.manage createsuperuser

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: dev-db-up
dev-db-up:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml --project-name project_dev_db up --force-recreate db -d

.PHONY: dev-db-down
dev-db-down:
	docker compose --project-name project_dev_db down

.PHONY: update
update: install migrate install-pre-commit ;
