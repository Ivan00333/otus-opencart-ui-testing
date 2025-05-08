# сборка образа
# docker build --no-cache -t opencart-tests .

# команда для запуска тестов
# docker run --rm   --network host   -v "$(pwd)/allure-results:/allure-results"   opencart-tests     --browser=chrome     --selenoid_url=http://localhost:4444/wd/hub     --browser_version=128.0

FROM python:3.10-slim

WORKDIR /app

VOLUME /allure-results

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["pytest", "--alluredir=/allure-results"]
CMD []
