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
    timeout(time: 30, unit: 'MINUTES')
  }
  triggers {
    cron('H/10 * * * *')
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
        sh '/usr/src/app/bin/webpagetest test script.txt -l "us-east-1:Firefox" -r 5 --first --poll --reporter json > "batch-URL-results.json"
        }
      post {
        always {
          archiveArtifacts 'batch-URL-results.json'
        }
        success {
          stash includes: 'batch-URL-results.json', name: 'batch-URL-results.json'
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
        unstash 'batch-URL-results.json'
        sh '''
          python ./send_to_datadog.py
        '''
      }
    }
  }
}
