pipeline {
    agent { label 'master' }
    environment {
        APP_NAME = "test app"
    }
    stages {
        stage("Build Image") {
            steps {
                sh "echo ${env.APP_NAME}"
                sh "docker version"
            }
        }
    }
}