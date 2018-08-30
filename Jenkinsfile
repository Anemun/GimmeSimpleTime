node('docker') {
 
    stage 'Checkout'
        checkout scm
    stage 'Build image'
        sh "docker build -t jackithub/testjob01:${BUILD_NUMBER} -f Dockerfile ."
        sh "echo test"
        sh "echo ${jackithub}"
}