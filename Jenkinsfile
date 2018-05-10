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
    stage('test') {
      agent {
        dockerfile {
         dir 'webpagetest-api'
         additionalBuildArgs '--no-cache'
        }
     }
     steps {
      sh '''
      '/usr/src/app/bin/webpagetest test addons.mozilla.org -l "us-east-1:Firefox" -r 5 --first --poll --reporter json > "fxa-homepage.json"'
      python send_to_datadog.py
      '''
      }
      post {
        always {
          archiveArtifacts 'fxa-homepage.json'
        }
      }
    }
  }
}
