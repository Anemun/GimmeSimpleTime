node('docker') {
 
    stage 'Checkout'
        checkout scm
    stage 'Build & UnitTest'
        sh "docker build -t jackithub:testjob01${BUILD_NUMBER} -f Dockerfile ."
}