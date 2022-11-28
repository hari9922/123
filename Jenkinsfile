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
 








