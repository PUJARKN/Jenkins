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
                sh './your-script.sh'  // Or specify the commands directly
            }
        }
    }
}
