pipeline {
    agent { label 'docker'}
    stages {        
        stage ('Build image'){
            steps {
                sh "docker build -t jackithub/testjob01:${BUILD_NUMBER} -f Dockerfile ."
            }
        }
        stage ('Push image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerHub', url: ""]) {
                sh "docker push jackithub/testjob01:${BUILD_NUMBER}"
                }   
            }
        }
        stage ('Deploy image to remote server') {
            stages {
                stage ('Stop current container') {
                    steps {
                        sshagent(credentials: ['arubaSSHroot']) {
                            catchError{
                                sh "ssh -o StrictHostKeyChecking=no root@80.211.30.61 docker stop gimmeSimpleTimeBot"                            
                            }
                            echo currentBuild.result
                        }
                    }
                }
                stage ('Run new container') {
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
