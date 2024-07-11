# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.12-slim

# Run Firefox instead of Chrome for more lightweight Image
RUN apt-get update -y \
&& apt-get install --no-install-recommends --no-install-suggests -y tzdata ca-certificates bzip2 curl wget libc-dev libxt6 \
&& apt-get install --no-install-recommends --no-install-suggests -y `apt-cache depends firefox-esr | awk '/Depends:/{print$2}'` \
&& update-ca-certificates \

# Removal
&& apt-get purge -y --auto-remove \
              -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/* /tmp/*

# To Install Geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz && \
    tar -zxf geckodriver-v0.31.0-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-v0.31.0-linux64.tar.gz

# To Install Firefox
RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
    wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-95.0.1&os=linux64" && \
    tar xjf $FIREFOX_SETUP -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm $FIREFOX_SETUP

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

CMD [ "python", "./screengrab.py"]