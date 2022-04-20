all:
	hugo -b $URL --gc --minify
	python build_jinja_pages.py
