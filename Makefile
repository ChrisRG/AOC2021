flake8:
	flake8 aoc2021/ --statistics 

mypy:
	mypy aoc2021/

black:
	black aoc2021/

setup:
	touch aoc2021/day_$(day).py
	touch inputs/day_$(day)_input.txt
	touch puzzles/day_$(day).md
