pipeline {
  agent any

  parameters {
    string(name: 'SELENOID_URL', defaultValue: 'http://selenoid:4444/wd/hub', description: 'URL Selenoid')
    string(name: 'BASE_URL',     defaultValue: 'http://opencart:8080',         description: 'Адрес Opencart')
    choice(name: 'BROWSER',      choices: ['chrome','firefox','opera'],     description: 'Браузер для тестов')
    string(name: 'BROWSER_VERSION', defaultValue: '',                      description: 'Версия браузера')
    string(name: 'THREADS',      defaultValue: '1',                         description: 'Кол-во потоков pytest-xdist')
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/Ivan00333/otus-opencart-ui-testing.git', branch: 'jenkins'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t tests .'
        sh 'docker version'
      }
    }

    stage('Run Tests') {
      steps {
        // пробрасываем WORKSPACE, подключаем сеть, чтобы резолвились имена сервисов
        sh """
          docker run --rm \
            --network selenoid \
            -v \$WORKSPACE/allure-results:/app/allure-results \
            tests pytest -v \
              --alluredir=allure-results \
              --selenoid_url=${params.SELENOID_URL} \
              --base_url=${params.BASE_URL} \
              --browser=${params.BROWSER} \
              --browser_version=${params.BROWSER_VERSION} \
              -n ${params.THREADS}
        """
      }
    }

    stage('Publish Allure Report') {
      steps {
        // плагин Allure Jenkins Plugin
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
