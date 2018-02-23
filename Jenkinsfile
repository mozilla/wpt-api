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
    stage('docker build') {
       agent any
       steps {
          sh 'docker build -t webpagetest-api .'          
       }
    }
  }
}
