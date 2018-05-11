#!/usr/bin/env groovy

pipeline {
  agent none
  environment {
    WEB_PAGE_TEST = credentials('WEB_PAGE_TEST')
    WEBPAGETEST_SERVER = "https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/"
    PAGE_URL = "https://latest.dev.lcip.org/?service=sync&entrypoint=firstrun&context=fx_desktop_v3"
  }
  triggers {
    cron('H/5 * * * *')
  }
  options {
    ansiColor('xterm')
    timestamps()
    timeout(time: 30, unit: 'MINUTES')
  }
  stages {
    stage('clone') {
       agent any
       steps {
         checkout([
           $class: 'GitSCM',
           branches: [[name: 'master']],
           extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'webpagetest-api']],
           userRemoteConfigs: [[url: 'https://github.com/marcelduran/webpagetest-api']]])
        }
    }
    stage('Run webpagetest') {
      agent {
        dockerfile { dir 'webpagetest-api' }
      }
      steps {
        sh '/usr/src/app/bin/webpagetest test addons.mozilla.org -l "us-east-1:Firefox" -r 5 --first --poll --reporter json > "fxa-homepage.json"'
        }
      post {
        always {
          archiveArtifacts 'fxa-homepage.json'
        }
        success {
          stash includes: 'fxa-homepage.json', name: 'fxa-homepage.json'
        }
        failure {
          archiveArtifacts 'fxa-homepage.json'
        }
      }
    }
    stage('Submit stats to datadog') {
      agent {
        dockerfile { dir 'webpagetest-api' }
      }
      steps {
        unstash 'fxa-homepage.json'
        sh '''
          python --version
          echo $(pwd)
          ls .
          ls $(pwd)
          # echo ${WORKSPACE}
          # see https://support.cloudbees.com/hc/en-us/articles/230922508-Pipeline-Files-manipulation
          ls -la send_to_datadog.py
          chmod +x send_to_datadog.py
          python ./send_to_datadog.py
          ls -la send_to_datadog.py
        '''
      }
    }
  }
}
