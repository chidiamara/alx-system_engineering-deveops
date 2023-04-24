# This manifest sets up client SSH configuration file so that
# one can connect to a server without typing a password
exec {'/etc/ssh/ssh_config':
path     => '/bin',
command  => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
provider => 'shell',
}
