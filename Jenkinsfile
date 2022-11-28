import groovy.json.JsonOutput
import groovy.transform.Field
import groovy.json.JsonSlurper


node ('master') {

    if ("${params.Branch_Name}" == 'main')
    {
        checkout()
       
        
        if ("${params.Language_Name}" == 'springboot')
            {
//                 JavaBuild()
                echo "Springboot Language"
            }
        else if ("${params.Language_Name}" == 'python')
            {
//                 pybuild()  
                echo "python"
                pybuild()
                dockerbuild()
            }
        else if ("${params.Language_Name}" == 'node')
            {
//                 nodebuild()
            }
        else
            {
                echo "Select Application"
            }
               
    }

}
        

def checkout()
{
    stage ("checkout")
    {
        checkout scm 
    }
 }


def pybuild()
{
    stage ("pybuild")
    {
//         sh "python3 apppy.py"
        echo "pybuild"
    }
 }

def dockerbuild()
{
    stage ("dockerbuild")
    {  
        sh "docker rm -f haridemo"
        sh "docker build -t pyimage:pyimage ."        
        sh "docker run -it -d --name haridemo -p 8081:8089 pyimage:pyimage"
    }
 }
 








