.PHONY: help up down build restart logs logs-backend logs-db clean rebuild status shell-backend shell-db

# Default target
help:
	@echo "Available commands:"
	@echo "  make up           - Start all services"
	@echo "  make down         - Stop all services"
	@echo "  make build        - Build all services"
	@echo "  make rebuild      - Rebuild and restart all services"
	@echo "  make restart      - Restart all services"
	@echo "  make logs         - View logs from all services"
	@echo "  make logs-backend - View backend logs"
	@echo "  make logs-db      - View database logs"
	@echo "  make status       - Show status of all services"
	@echo "  make shell-backend- Open shell in backend container"
	@echo "  make shell-db     - Open psql shell in database"
	@echo "  make clean        - Stop services and remove volumes"

# Start all services
up:
	docker compose -f docker-compose.dev.yaml up -d

# Stop all services
down:
	docker compose -f docker-compose.dev.yaml down

# Build all services
build:
	docker compose -f docker-compose.dev.yaml build

# Rebuild and restart
rebuild:
	docker compose -f docker-compose.dev.yaml up -d --build --force-recreate

# Restart all services
restart:
	docker compose -f docker-compose.dev.yaml restart

# View all logs
logs:
	docker compose -f docker-compose.dev.yaml logs -f

# View backend logs only
logs-backend:
	docker compose -f docker-compose.dev.yaml logs -f backend

# View database logs only
logs-db:
	docker compose -f docker-compose.dev.yaml logs -f postgres

# Show status of services
status:
	docker compose -f docker-compose.dev.yaml ps

# Open shell in backend container
shell-backend:
	docker exec -it mealprep-backend /bin/bash

# Open psql shell in database
shell-db:
	docker exec -it postgres psql -U admin -d postgres

# Stop and remove everything including volumes
clean:
	docker compose -f docker-compose.dev.yaml down -v
	@echo "Warning: This removed all data volumes!"
