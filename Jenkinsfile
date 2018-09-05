node('docker') {
 
    stage 'Checkout'
        checkout scm
    stage 'Testing'
        DOCKER_CREDS = credentials('dockerHub')
        DOCKER_LOGIN = "${env.DOCKER_CREDS_USR}"
        sh "echo ${DOCKER_LOGIN}"
    // stage 'Build image'
    //     sh "docker build -t jackithub/testjob01:${BUILD_NUMBER} -f Dockerfile ."
    // stage 'Push image'
    //     withDockerRegistry([credentialsId: 'dockerHub', url: ""]) {
    //         sh "docker push jackithub/testjob01:${BUILD_NUMBER}"
    //     }
    // stage 'Deploy'         
    //     sshagent(credentials: ['arubaSSHroot']) {            
    //         //sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 uptime"
    //         //sh "ssh -v root@80.211.30.61"            
    //         sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker login -u ${DOCKER_LOGIN} -p $DOCKER_PASS"
    //         sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker run jackithub/testjob01:${BUILD_NUMBER}"
    //     }
        // docker.withServer('tcp://80.211.30.61:4243') {
        //     docker.image('jackithub/testjob01:${BUILD_NUMBER}').withRun('-p 3306:3306') {
        //         sh 'ehco test'

        //     }
        // }    
}