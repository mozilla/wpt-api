#!/usr/bin/env groovy

pipeline {
  agent none
  environment {
    WEB_PAGE_TEST = credentials('WEB_PAGE_TEST')
    WEBPAGETEST_SERVER = "https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/"
    PAGE_URL = "https://latest.dev.lcip.org/?service=sync&entrypoint=firstrun&context=fx_desktop_v3"
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
        sh '/usr/src/app/bin/webpagetest test "${PAGE_URL}" -l "us-east-1-linux:Firefox" -r 5 --first --poll --reporter json > "fxa-homepage.json"'
        }
      post {
        always {
          archiveArtifacts 'fxa-homepage.json'
        }
        success {
          stash includes: 'fxa-homepage.json', name: 'fxa-homepage.json'
        }
      }
    }
    stage('Submit stats to datadog') {
      agent {
        dockerfile {
          args '--net host'
        }
      }
      steps {
        unstash 'fxa-homepage.json'
        sh '''
          python ./send_to_datadog.py
        '''
      }
    }
  }
}
