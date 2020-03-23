#!/usr/bin/env bash
# Manifest that executes and kill process
exec { 'pkill':
	command   => 'pkill killmenow',
	path      => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
	provider  => 'shell',
}
