#!/usr/bin/env groovy

pipeline {
  agent none
  environment {
    WEB_PAGE_TEST = credentials('WEB_PAGE_TEST')
    WEBPAGETEST_SERVER = "https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/"
  }
  options {
    ansiColor('xterm')
    timestamps()
    timeout(time: 90, unit: 'MINUTES')
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
        sh '/usr/src/app/bin/webpagetest batch commands.txt > "alexa-topsites.json"'
        }
      post {
        always {
          archiveArtifacts 'alexa-topsites.json'
        }
        success {
          stash includes: 'alexa-topsites.json', name: 'alexa-topsites.json'
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
        unstash 'alexa-topsites.json'
        sh '''
          python ./send_to_datadog.py
        '''
      }
    }
  }
}
