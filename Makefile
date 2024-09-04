install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-nod:
	poetry run brain-nod
brain-prog:
	poetry run brain-prog
brain-prime:
	poetry run brain-prime
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	poetry run python3 -m pip install dist/*.whl
lint:
	poetry run flake8 brain_games
