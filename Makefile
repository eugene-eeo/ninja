build:
	pip install -r requirements.txt
	npm install .
	./ninja.py  --times=10 | ./proc/htmlify.py --title=simulated  | ./proc/katexify.js > results.html
	./ninja2.py --times=10 | ./proc/htmlify.py --title=calculated | ./proc/katexify.js > results2.html
