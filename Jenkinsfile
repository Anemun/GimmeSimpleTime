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
        sshagent(credentials : ['6025612b-7b20-43aa-b93c-3f0556761e00']) {
            sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 uptime"
            sh "ssh -v root@80.211.30.61"
            sh "docker run jackithub/testjob01:${BUILD_NUMBER}"
        }
        // docker.withServer('tcp://80.211.30.61:4243') {
        //     docker.image('jackithub/testjob01:${BUILD_NUMBER}').withRun('-p 3306:3306') {
        //         sh 'ehco test'

        //     }
        // }    
}