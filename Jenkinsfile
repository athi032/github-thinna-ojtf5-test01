pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                echo 'Run Selenium Tests'
                bat 'python IframeCase/test_iframe.py'
            }
        }
    }
}
