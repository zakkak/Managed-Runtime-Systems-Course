SOURCES      := ${wildcard *.adoc}
TARGETS      := ${SOURCES:.adoc=.html}
PLOT_SOURCES := ${wildcard plots/*.py}
PLOT_TARGETS := ${PLOT_SOURCES:.py=.svg}

all: $(TARGETS) $(PLOT_TARGETS)

reveal.js:
	git clone -b 4.1.1 --depth 1 https://github.com/hakimel/reveal.js.git

%.svg: %.py 
	python3 $<

%.html: %.adoc common/* reveal.js 
	bundle exec asciidoctor-revealjs -r asciidoctor-diagram $<

autobuild:
	echo "Watching *.adoc for changes"
	inotifywait -m -e close_write *.adoc common/* | \
	while read events; do \
		echo $$events; \
  		bundle exec asciidoctor-revealjs -r asciidoctor-diagram $(SOURCES); \
	done

setup:
	bundle config --local github.https true
	bundle config set --local path '.bundle/gems'
	bundle --binstubs=.bundle/.bin

clean:
	rm -rf *.html figures/layers.svg figures/java-native-stack.svg figures/jvm-architecture.svg figures/object-array-layout.svg