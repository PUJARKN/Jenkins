pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/your-repo.git', branch: 'main'
            }
        }
        stage('Run Script') {
            steps {
                python "pythonbascis1.py"
            }
        }
    }
}
