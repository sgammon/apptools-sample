
#
#    apptools sample: makefile
#
#    :author: Sam Gammon <sam@keen.io>
#    :copyright: (c) Keen IO, 2013
#    :license: The inspection, use, distribution, modification or implementation
#              of this source code is governed by a private license - all rights
#              are reserved by the Authors (collectively, "Keen IO") and held
#              under relevant California and US Federal Copyright laws. For full
#              details, see ``LICENSE.md`` at the root of this project. Continued
#              inspection of this source code demands agreement with the included
#              license and explicitly means acceptance to these terms.
#


### === VARS === ###

HOST=127.0.0.1
PORT=5000


### === ROUTINES === ###

all: build
run: build devserver

build: develop
	@echo "Building SASS..."
	#@bin/compass compile --force --output-style=compressed

	@echo "=== Build complete. ==="

package: develop
	@echo "Making buildroot..."
	@mkdir -p dist/

	@echo "Building source package..."
	@bin/python setup.py sdist

	@echo "Building egg..."
	@bin/python setup.py bdist_egg

	@echo "=== apptools-sample distribution built. ==="

develop: .develop
	@echo "Updating source dependencies..."
	@git submodule update --init

test:
	@pip install nose
	@echo "Running testsuite..."
	@nosetests coolapp_tests --no-byte-compile

coverage:
	@pip install nose
	@echo "Running testsuite (with coverage)..."
	@nosetests coolapp_tests --with-coverage \
							 --cover-package=coolapp \
							 --cover-html-dir=.develop/coverage_html \
							 --cover-xml-file=.develop/coverage.xml \
							 --no-byte-compile;

deploy:
	@echo "Deployment is not currently supported from dev. Check back later."

clean:
	@echo "Cleaning object files..."
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "*.pyo" -exec rm -f {} \;

	@echo "Cleaning SASS cache..."
	@rm -fr .sass-cache

distclean: clean
	@echo "Cleaning development state..."
	@rm -fr .develop

	@echo "Cleaning gemroot..."
	@rm -fr .Gems

	@echo "Cleaning virtualenv..."
	@rm -fr .Python bin/ include/ lib/ config.rb .env .develop

forceclean: distclean
	@echo "Resetting codebase..."
	@git reset --hard

	@echo "Cleaning libraries..."
	@rm -fr assets/js/source/apptools coolapp/lib/apptools coolapp/lib/appfactory

	@echo "Cleaning untracked files..."
	@git clean -df

### === dirs === ###
bin: .env
lib: .env

### === defs === ###
.develop: bin lib config.rb .env
	@echo "Installing brew dependencies..."
	@-brew install libev
	@-brew install redis

	@echo "Installing development dependencies..."
	@-bin/pip install cython "git+git://github.com/surfly/gevent.git#egg=gevent"
	@-bin/pip install cython "git+git://github.com/keenlabs/logbook.git#egg=logbook"
	@bin/pip install -r ./requirements.txt
	@mkdir .develop
	@chmod -R 775 .develop

.env:
	@echo "Initializing virtualenv..."
	@pip install virtualenv
	@virtualenv . --prompt=" (apptools-sample) "

	@echo "Symlinking toolchain..."
	@ln -s $(PWD)/scripts/web.py $(PWD)/bin/web
	@ln -s $(PWD)/scripts/compile_templates.py $(PWD)/bin/compile_templates
	@chmod +x $(PWD)/scripts/web.py $(PWD)/bin/web
	@echo "$(PWD)/coolapp/lib" > lib/python2.7/site-packages/coolapp-lib.pth
	@echo "$(PWD)/coolapp" > lib/python2.7/site-packages/coolapp.pth
	@echo "$(PWD)/.." > lib/python2.7/site-packages/apptools-sample.pth

	@echo "Overriding standard Google paths..."
	@echo "" > lib/python2.7/site-packages/protobuf-2.5.0-py2.7-nspkg.pth
	@rm -fr lib/python2.7/site-packages/webapp2_extras

config.rb:
	@echo "Installing Compass..."
	@gem install compass --install-dir ./.Gems

	@echo "Configuring Compass..."
	@-compass init -x sass --prepare --environment development --relative-assets --sass-dir assets/style/source --css-dir assets/style/static/compiled --images-dir assets/img/static --javascripts-dir assets/js/static --fonts-dir assets/ext/static/fonts

	@echo "Symlinking Compass binaries..."
	@ln -s $(PWD)/.Gems/bin/compass $(PWD)/bin/compass
	@ln -s $(PWD)/.Gems/bin/sass $(PWD)/bin/sass
	@ln -s $(PWD)/.Gems/bin/scss $(PWD)/bin/scss
	@ln -s $(PWD)/.Gems/bin/sass-convert $(PWD)/bin/sass-convert

	@echo "Cleaning junk..."
	@rm -fr ./stylesheets ./sass

	@echo "Compass is ready."

devserver:
	@echo "Would run devserver."
