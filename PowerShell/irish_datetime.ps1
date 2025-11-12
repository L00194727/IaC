$DDMMYY = "13/10/2025"
$OGGI = [datetime]::ParseExact($DDMMYY, "dd/MM/yyyy", [System.Globalization.CultureInfo]::GetCultureInfo("en-IE"))
$OGGI