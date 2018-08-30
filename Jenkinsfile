node('docker') {
 
    stage 'Checkout'
        checkout scm
    stage 'Build image'
        DOCKERHUB_CREDS = credentials('dockerHub')
        sh "docker build -t jackithub/testjob01:${BUILD_NUMBER} -f Dockerfile ."
    stage 'Push image'
        withDockerRegistry([credentialsId: 'dockerHub', url: ""])
            sh 'docker push jackithub/testjob01:${BUILD_NUMBER}'

        
}