# install IIS server role

 param($code=99)
 function ExitWithCode { 
 if($? -eq "true"){
   write-host("Commnad executed successfully")
  }else {
   write-host("Commnad execution failed ")
   exit $code
} 
}
 
 
 
 Install-WindowsFeature -name Web-Server -IncludeManagementTools
 ExitWithCode

 # remove default htm file
  remove-item  C:\inetpub\wwwroot\iisstart.htm
  ExitWithCode

 # Add a new htm file that displays server name
  Add-Content -Path "C:\inetpb\ww\iisstart.htm" -Value $("Hello World from " + $env:computername)
  ExitWithCode
  
