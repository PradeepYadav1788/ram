# install IIS server role

 function ExitWithCode { param($exitcode=99) $host.SetShouldExit($exitcode); exit }
 
 
 Install-WindowsFeature -name Web-Server -IncludeManagementTools
 
 if($? -eq "true"){
   write-host("Commnad executed successfully")
   }else {
   write-host("Commnad execution failed ")
   ExitWithCode 
}

 # remove default htm file
  remove-item  C:\inetpub\wwwroot\iisstart.htm
  if($? -eq "true"){
   write-host("Commnad executed successfully")
  }else {
   write-host("Commnad execution failed ")
   ExitWithCode 
}

 # Add a new htm file that displays server name
  Add-Content -Path "C:\inetpub\wwwroot\iisstart.htm" -Value $("Hello World from " + $env:computername)
  if($? -eq "true"){
   write-host("Commnad executed successfully")
   }else {
   write-host("Commnad execution failed ")
   ExitWithCode 
}
  
