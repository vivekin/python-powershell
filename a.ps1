
param ([Parameter(Mandatory)]$name="dummy")
#param ($name="dummy")

try{
Write-Host "hello $name" -BackgroundColor Cyan
}
catch{
Write-Host "error" -BackgroundColor Red
}
finally {Write-Host "finally" -BackgroundColor Green}