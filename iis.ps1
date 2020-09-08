# install IIS server role

 function ExitWithCode { param($exitcode=99) $host.SetShouldExit($exitcode); exit }
 
 
 Install-WindowsFeature -name Web-Server -IncludeManagetTools
 
 if($? -eq "true"){
   write-host("Commnad executed successfully")
   }else {
   write-host("Commnad execution failed ")
   ExitWithCode 
}

 # remove default htm file
  remove-item  C:\inetpub\wwwroot\ii.htm
  if($? -eq "true"){
   write-host("Commnad executed successfully")
  }else {
   write-host("Commnad execution failed ")
   ExitWithCode 
}

 # Add a new htm file that displays server name
  Add-Content -Path "C:\inetpub\wwwroot\iisstart.htm" -Value $("Hello Wor from " + $env:computername)
  if($? -eq "true"){
   write-host("Commnad executed successfully")
   }else {
   write-host("Commnad execution failed ")
   ExitWithCode 
}
  
