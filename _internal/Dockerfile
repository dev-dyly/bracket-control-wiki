FROM ruby:3.3
RUN gem install jekyll --version 3.10.0 --no-document
RUN gem install kramdown-parser-gfm --version 1.1.0 --no-document
WORKDIR /site
ENTRYPOINT ["jekyll"]
