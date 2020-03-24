#!/usr/bin/env bash
# configuration with puppet
file_line { 'PasswordAuthentication':
        path => '~/etc/ssh/ssh_config',
        line => 'PasswordAuthentication no',
}
file_line { 'IdentityFile':
        path => '~/etc/ssh/ssh_config',
        line => 'IdentityFile ~/.ssh/holberton'
}
