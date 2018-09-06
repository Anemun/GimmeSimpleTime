pipeline {
    agent { label 'docker'}
    stages {        
        stage ('1. Build image'){
            steps {
                sh "docker build -t jackithub/testjob01:${BUILD_NUMBER} -f Dockerfile ."
            }
        }
        stage ('2. Push image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerHub', url: ""]) {
                sh "docker push jackithub/testjob01:${BUILD_NUMBER}"
                }   
            }
        }
        stage ('3. Deploy image to remote server') {
            stages {
                stage ('3.1 Stop current container') {
                    steps {
                        sshagent(credentials: ['arubaSSHroot']) {
                            script {
                                try {
                                    sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker stop gimmeSimpleTimeBot || true && ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker rm gimmeSimpleTimeBot || true"
                                    // sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker stop gimmeSimpleTimeBot"
                                    // sleep 5
                                    // sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker rm gimmeSimpleTimeBot"                                     
                                } catch (err) {
                                    echo err
                                }
                                echo currentBuild.result
                            }
                            
                        }
                    }
                }
                stage ('3.2 Run new container') {
                    steps {
                        sshagent(credentials: ['arubaSSHroot']) {
                            withCredentials([usernamePassword(credentialsId: 'dockerHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD'), 
                                    string(credentialsId: 'testTelebotToken', variable: 'TOKEN')]) {
                                sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker login -u $USERNAME -p $PASSWORD"
                                sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker run -d --name gimmeSimpleTimeBot jackithub/testjob01:${BUILD_NUMBER} $TOKEN"
                            }
                        }
                    }
                }
            }
        }
    }
}


// node('docker') {
//         stage 'Checkout'
//             checkout scm  
//         stage 'Build image'
//             sh "docker build -t jackithub/testjob01:${BUILD_NUMBER} -f Dockerfile ."
//         stage 'Push image'
//             withDockerRegistry([credentialsId: 'dockerHub', url: ""]) {
//                 sh "docker push jackithub/testjob01:${BUILD_NUMBER}"
//             }        
//         stage 'Deploy'         
//             sshagent(credentials: ['arubaSSHroot']) {
//                 withCredentials([usernamePassword(credentialsId: 'dockerHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD'), 
//                                 string(credentialsId: 'testTelebotToken', variable: 'TOKEN')]) {
//                     sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker login -u $USERNAME -p $PASSWORD"
//                     //sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker stop gimmeSimpleTimeBot"                
//                     sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker run -d --name gimmeSimpleTimeBot jackithub/testjob01:${BUILD_NUMBER} $TOKEN"
//                 }
//             }
// }
