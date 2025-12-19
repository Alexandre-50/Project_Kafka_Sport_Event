Write-Host ">>> Starting Live Demo for Screenshots <<<" -ForegroundColor Green

$CurrentDir = Get-Location

# 1. Start Consumer in a new window
Write-Host "Launching Consumer in new window..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$CurrentDir'; Write-Host 'CONSUMER - LISTENING...'; .\.venv\Scripts\Activate.ps1; python -m src.consumer_sports"

# 2. Start Producer in a new window
Write-Host "Launching Producer in new window..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$CurrentDir'; Write-Host 'PRODUCER - GENERATING EVENTS...'; .\.venv\Scripts\Activate.ps1; python -m src.producer_sports"

# 3. Show Docker Status
Write-Host "`nDocker Status:" -ForegroundColor Yellow
docker compose ps

# 4. Tail the output file
Write-Host "`nTailing data/sample_output.jsonl (Press Ctrl+C to stop tailing)..." -ForegroundColor Cyan
Get-Content data/sample_output.jsonl -Wait -Tail 10
