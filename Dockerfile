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
      tar \
      netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

ARG GECKO_VERSION=v0.33.0

RUN wget -qO /tmp/geckodriver.tar.gz \
      "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-linux64.tar.gz" \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
    && rm /tmp/geckodriver.tar.gz

WORKDIR /app
VOLUME /allure-results

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["pytest", "--alluredir=/allure-results"]
CMD []
