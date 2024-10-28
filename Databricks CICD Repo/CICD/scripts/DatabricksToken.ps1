param
(
    [parameter(Mandatory = $true)] [String] $databricksWorkspaceResourceId,
    [parameter(Mandatory = $true)] [String] $databricksWorkspaceUrl,
    [parameter(Mandatory = $false)] [int] $tokenLifeTimeSeconds = 300
)

# The Azure Databricks Management API resource (not the service principal ID)
# $azureDatabricksResource = 'https://databricks.azure.net/'
$azureDatabricksPrincipalId = '1834184d-7b40-47f3-9bc6-90665ecd5c23' # 'd999aa23-b2e1-4766-aadc-2e54945fc887'

$headers = @{}
$headers["Authorization"] = "Bearer $((az account get-access-token --resource $azureDatabricksPrincipalId | ConvertFrom-Json).accessToken)"
$headers["X-Databricks-Azure-SP-Management-Token"] = "$((az account get-access-token --resource https://management.core.windows.net/ | ConvertFrom-Json).accessToken)"
$headers["X-Databricks-Azure-Workspace-Resource-Id"] = $databricksWorkspaceResourceId

$json = @{}
$json["lifetime_seconds"] = $tokenLifeTimeSeconds

# Define the request body for the API call
$body = @{
    comment = "Token created for automation"
    lifetime_seconds = 3600  # optional, adjust as necessary
} | ConvertTo-Json

#$req = Invoke-WebRequest -Uri "https://$databricksWorkspaceUrl/api/2.0/token/create" -Method Post -Headers $headers -Body ($json | ConvertTo-Json) -ContentType "application/json"
# $req = Invoke-WebRequest -Uri "https://$databricksWorkspaceUrl/api/2.0/token/create" -Method 'POST' -Body $body -ContentType "application/json"
$req = Invoke-WebRequest -Uri "https://$databricksWorkspaceUrl/api/2.0/token/create" -Body ($json | ConvertTo-Json) -ContentType "application/json"

$bearerToken = ($req.Content | ConvertFrom-Json).token_value

return $bearerToken