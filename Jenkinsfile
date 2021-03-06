pipeline {
    agent { label 'docker'}
    environment {
        DOCKER_IMAGE = "jackithub/testjob01:${BUILD_NUMBER}"
        CONTAINER_NAME = "${params.containerName}"        
    }
    stages {         
        stage ('1. Build image'){
            steps {
                sh "docker build -t $DOCKER_IMAGE -f Dockerfile ."
            }
        }
        stage ('2. Push image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerHub', url: ""]) {
                sh "docker push $DOCKER_IMAGE"
                }   
            }
        }
        stage ('3. Deploy image to remote server') {
            stages {
                stage ('3.1 Stop current container') {
                    steps {
                        sshagent(credentials: ['SSHroot']) {
                             withCredentials([string(credentialsId: 'ServerIP', variable: 'IP')]) {
                                sh "ssh -o StrictHostKeyChecking=no $IP docker stop $CONTAINER_NAME || true && ssh -o StrictHostKeyChecking=no $IP docker rm $CONTAINER_NAME || true"                              
                             }
                        }
                    }
                }
                stage ('3.2 Run new container') {
                    steps {
                        sshagent(credentials: ['SSHroot']) {
                            withCredentials([usernamePassword(credentialsId: 'dockerHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD'),
                                    string(credentialsId: 'ServerIP', variable: 'IP'), 
                                    string(credentialsId: 'testTelebotToken', variable: 'TOKEN')]) {
                                sh "ssh -o StrictHostKeyChecking=no $IP docker login -u $USERNAME -p $PASSWORD"
                                sh "ssh -o StrictHostKeyChecking=no $IP docker run -d --name $CONTAINER_NAME $DOCKER_IMAGE $TOKEN"
                            }
                        }
                    }
                }
            }
        }
    }
}