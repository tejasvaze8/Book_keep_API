pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
               sh 'docker push tvaze/graphql-books-2.0:lts'
               sh 'python3 --version'
               echo 'Testing Complete'

            }
        }
    }
}
