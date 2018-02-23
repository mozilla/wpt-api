#!/usr/bin/env groovy

pipeline {
    agent none

stages {
    stage('clone') {
       agent any
       steps {
          git 'https://github.com/marcelduran/webpagetest-api'
          checkout([
              $class: 'GitSCM',
              branches: [[name: 'master']],
              doGenerateSubmoduleConfigurations: false,
              extensions: [[
                  $class: 'RelativeTargetDirectory',
                  relativeTargetDir: 'scripts']],
              submoduleCfg: [],
              userRemoteConfigs: [[
                  url: 'https://github.com/stephendonner/webpagetest-amo']]])
        }
    }
    stage('build docker image') {
       agent any
       steps {
          sh 'docker build -t webpagetest-api https://github.com/marcelduran/webpagetest-api.git'
       }
    }
    stage('test') {
      agent {
        dockerfile true
      }
      environment {
        WEB_PAGE_TEST = credentials('WEB_PAGE_TEST')
      }
      steps {
         sh "docker run --rm -t webpagetest-api test -e WEBPAGETEST_SERVER=https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/ test 'https://latest.dev.lcip.org/?service=sync&entrypoint=firstrun&context=fx_desktop_v3' -l 'us-east-1:Firefox' -r 9 --first --poll --reporter json > 'fxa-homepage.json'"
      }
    }
  }
}
