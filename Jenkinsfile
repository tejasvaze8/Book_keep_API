pipeline {
    agent { dockerfile {label 'tvaze/graphql-books-2.0:lts'} }
    stages {
        stage('Test') {
            steps {
               sh 'python3 --version'
               echo 'Testing Complete'

            }
        }
    }
}
