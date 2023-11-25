# creates a manifest that kills a process named killmenow
# Executes a command
exec { 'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}
