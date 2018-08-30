node('docker') {
 
    stage 'Checkout'
        checkout scm
    stage 'Build image'
        sh "docker build -t jackithub/testjob01:${BUILD_NUMBER} -f Dockerfile ."
    stage 'Push image'
        withDockerRegistry([credentialsId: 'dockerHub', url: ""]) {
            sh 'docker push jackithub/testjob01:${BUILD_NUMBER}'
        }
    stage 'Deploy' 
        docker.withServer('tcp://80.211.30.61:4243') {
            docker.image('jackithub/testjob01:${BUILD_NUMBER}').withRun('-p 3306:3306') {
                sh 'ehco test'

            }
        }    
}