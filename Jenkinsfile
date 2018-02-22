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
    stage('test') {
       agent {dockerfile true}
       steps {
          sh "test scripts/amo-details-page.wptscript " +
          "-l 'us-east-1:Firefox' " +
          "-r 5 " +
          "--first " +
          "--poll " +
          "--specs scripts/amo-details-testspecs.json"
       }
    }
  }
}
