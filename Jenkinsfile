#!/usr/bin/env groovy

pipeline {
  agent {
    label 'webpagetest'
  }
  libraries {
    lib('fxtest@1.10')
  }
  environment {
    WEB_PAGE_TEST = credentials('WEB_PAGE_TEST')
    WEBPAGETEST_SERVER = "https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/"
    PUB_WPT_API_KEY = credentials('PUB_WPT_API_KEY')
  }
  options {
    ansiColor('xterm')
    timestamps()
    timeout(time: 25, unit: 'MINUTES')
  }
  stages {
    stage('Clone webpagetest-api repo') {
      agent any
      steps {
        checkout([
          $class: 'GitSCM',
          branches: [[name: 'master']],
          extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'webpagetest-api']],
          userRemoteConfigs: [[url: 'https://github.com/marcelduran/webpagetest-api']]])
        }
    }
    stage('Run WebPageTest (command-line API)') {
      agent {
        dockerfile { dir 'webpagetest-api' }
      }
      steps {
        writeFile([
          file: 'commands.txt',
          encoding: 'UTF-8',
          text: """test ${TARGET_URL} --location us-east-1-linux:Firefox --keepua --noopt --noimages -r 3 --first --poll 5 --priority 1 --reporter json --label ${TARGET_NAME}.fx.release
test ${TARGET_URL} --location us-east-1-linux:Firefox%20Nightly --keepua  --noopt --noimages -r 3 --first --poll 5 --priority 1 --reporter json --label ${TARGET_NAME}.fx.nightly
test ${TARGET_URL} --location us-east-1-linux:Chrome --keepua  --noopt --noimages -r 3 --first --poll 5 --priority 1 --reporter json --label ${TARGET_NAME}.chrome.release
test ${TARGET_URL} --location us-east-1-linux:Chrome%20Canary --keepua  --noopt --noimages -r 3 --first --poll 5 --priority 1 --reporter json --label ${TARGET_NAME}.chrome.canary"""])
        sh '/usr/src/app/bin/webpagetest batch commands.txt > "wpt.json"'
      }
      post {
        always {
          archiveArtifacts 'commands.txt,wpt.json'
        }
        success {
          stash includes: 'wpt.json', name: 'wpt.json'
        }
        failure {
          ircNotification('#perftest-alerts')
          emailext(
            attachLog: true,
            body: '$BUILD_URL\n\n$FAILED_TESTS',
            replyTo: '$DEFAULT_REPLYTO',
            subject: '$DEFAULT_SUBJECT',
            to: '$DEFAULT_RECIPIENTS')
        }
      }
    }
    stage('Submit stats to Telemetry') {
      agent {
        dockerfile true
      }
      steps {
        unstash 'wpt.json'
        sh 'python --version'
        sh 'python ./send_to_telemetry.py wpt.json'
      }
    }
    stage('Submit stats to Datadog') {
      agent {
        dockerfile {
          args '--net host'
        }
      }
      environment {
        DATADOG_API_KEY = credentials("DATADOG_API_KEY")
        DATADOG_APP_KEY = credentials("DATADOG_APP_KEY")
      }
      steps {
        unstash 'wpt.json'
        sh 'python ./send_to_datadog.py wpt.json'
      }
    }
  }
}
