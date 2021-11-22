# Dockerfile, Image, Container
FROM python:3.8

# ADD price_comparison_lazada_shopee.py .
# ADD scape_lazada.py .
# ADD scape_shopee.py .

# RUN pip install pandas matplotlib seaborn selenium webdriver_manager heroku
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# RUN chmod -R 775 /home/node/app
# RUN chown -R node:root /home/node/app


# Set display port as an environment variable
 # ENV DISPLAY=:99
 
 COPY . /app
WORKDIR /app

RUN chmod -R 775 .
# RUN chmod -R 775 /.wdm
RUN chown -R root .
# RUN chown -R root /.wdm

CMD [ "python", "./price_comparison_lazada_shopee.py" ]