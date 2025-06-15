pipeline {
  agent any

  parameters {
    string(name: 'SELENOID_URL', defaultValue: 'http://selenoid:4444/wd/hub', description: 'URL Selenoid')
    string(name: 'BASE_URL', defaultValue: 'http://opencart:8080',         description: 'Адрес Opencart')
    string(name: 'DB_HOST',  defaultValue: 'mariadb',                   description: 'Хост БД')
    string(name: 'DB_PORT',  defaultValue: '3306',                       description: 'Порт БД')
    choice(name: 'BROWSER',  choices: ['chrome','firefox','opera'],     description: 'Браузер для тестов')
    string(name: 'BROWSER_VERSION', defaultValue: '',                      description: 'Версия браузера')
    string(name: 'THREADS',      defaultValue: '1',                         description: 'Кол-во потоков pytest-xdist')
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/Ivan00333/otus-opencart-ui-testing.git', branch: 'jenkins'
      }
    }

   stage('Bring up stack') {
      steps {
        sh 'docker compose up -d phpadmin mariadb opencart selenoid selenoid-ui'
        sh '''
          ./wait-for-it.sh mariadb:3306 -s -t 60 &&
          ./wait-for-it.sh opencart:8080 -s -t 60 &&
          ./wait-for-it.sh selenoid:4444 -s -t 60
        '''
      }
    }

    stage('Run tests via Compose') {
      steps {
        sh 'mkdir -p allure-results'
        sh """
          docker-compose run --rm \
            -e SELENOID_URL=${params.SELENOID_URL} \
            -e BASE_URL=${params.BASE_URL} \
            -e DB_HOST=${params.DB_HOST} \
            -e DB_PORT=${params.DB_PORT} \
            -e BROWSER=${params.BROWSER} \
            -e BROWSER_VERSION=${params.BROWSER_VERSION} \
            -e THREADS=${params.THREADS} \
            tests pytest -v \
              --alluredir=allure-results \
              --selenoid_url=\$SELENOID_URL \
              --base_url=\$BASE_URL \
              --db_host=\$DB_HOST \
              --db_port=\$DB_PORT \
              --browser=\$BROWSER \
              --browser_version=\$BROWSER_VERSION \
              -n \$THREADS
        """
      }
    }

    stage('Tear down stack') {
      steps {
        sh 'docker-compose down --remove-orphans'
      }
    }

    stage('Publish Allure Report') {
      steps {
        allure includeProperties: false, results: [[path: 'allure-results']]
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
    }
  }
}
