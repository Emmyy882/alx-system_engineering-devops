# creates a manifest that kills a process named killmenow
exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  logoutput   => true,
}
