$PGSMC = Find-Module -Name * -Tag 'PSEdition_Core'
"There are {0:N0} Modules that Support PowerShell Core" -f $PGSMC.Count