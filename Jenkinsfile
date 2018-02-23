#!/usr/bin/env groovy

pipeline {
  agent none
  stages {
    stage('cleanup') {
      deleteDir()
    }
    stage('clone') {
       agent any
       steps {
          git 'https://github.com/marcelduran/webpagetest-api'
        }
    }
    stage('test') {
      agent {
        dockerfile true
      }
      environment {
        WEB_PAGE_TEST = credentials('WEB_PAGE_TEST')
        WEBPAGETEST_SERVER = "https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/"
      }
      steps {
          sh '/usr/src/app/bin/webpagetest test "https://latest.dev.lcip.org/?service=sync&entrypoint=firstrun&context=fx_desktop_v3" -l "us-east-1:Firefox" -r 9 --first --poll --reporter json > fxa-homepage.json'
      }
    }
  }
}
