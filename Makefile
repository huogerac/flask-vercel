run_tests:
	docker-compose -f docker-compose.test.yml up -d && \
	sleep 1 && pytest && \
	docker-compose -f docker-compose.test.yml down