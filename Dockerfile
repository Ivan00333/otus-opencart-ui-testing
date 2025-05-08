# сборка образа
# docker build --no-cache -t tests .

FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
      firefox-esr \
      chromium \
      chromium-driver \
      wget \
      ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN GECKO_TAG=$(wget -qO- https://api.github.com/repos/mozilla/geckodriver/releases/latest \
         | grep '"tag_name"' \
         | sed -E 's/.*"([^"]+)".*/\1/') \
    && wget -qO /tmp/geckodriver.tar.gz \
         "https://github.com/mozilla/geckodriver/releases/download/${GECKO_TAG}/geckodriver-${GECKO_TAG}-linux64.tar.gz" \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
    && rm /tmp/geckodriver.tar.gz

WORKDIR /app
VOLUME /allure-results

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["pytest", "--alluredir=/allure-results"]
CMD []
