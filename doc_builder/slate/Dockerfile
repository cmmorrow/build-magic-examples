FROM ruby:slim
RUN apt update && \
apt install -y build-essential nodejs tar wget
RUN wget https://github.com/slatedocs/slate/archive/refs/tags/v2.12.0.tar.gz && \
tar -xzf v2.12.0.tar.gz && \
mv slate-2.12.0 /srv/slate
RUN gem install bundler && \
BUNDLE_GEMFILE="/srv/slate/Gemfile" bundle install
CMD [ "/bin/sh" ]