# this Puppet manifest installs the flask from pip3
package { 'flask':
 ensure  => '2.1.0',
 provider => 'pip3',
}
