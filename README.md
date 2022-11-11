pipeline {
    agent any
      stages {
        stage ("hello") {
          step {
           echo "welcome jenkins pipeline"
           }
         }
       }
     }
