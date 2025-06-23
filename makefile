install:
	pip install -r requirements.txt

check-types:
	./scripts/check_types.sh .

check-imports:
	./scripts/check_imports.sh --check-only

check-styles:
	./scripts/check_styles.sh --diff

fix:
	./scripts/check_styles.sh --in-place
	./scripts/check_imports.sh

clean:
	rm -rf __pycache__ *.pyc

run:
	python main.py

generate_mappings:
	./scripts/generate_mappings.sh

test:
	pytest --disable-warnings $(ARGS) -vv -s
