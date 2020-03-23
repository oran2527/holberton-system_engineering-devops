# This manifest creates a file with some specifications
#!/usr/bin/env bash
file { 'tmp/holberton':
    ensure  => file
    path    => '/tmp/holberton',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
  }
