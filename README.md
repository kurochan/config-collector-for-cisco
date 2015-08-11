config-collector
=====

configuration collector for Cisco

## Tasks

```
$ fab -l
Available commands:

debug           enable debug output
role            select role
config.collect  collect configuration
git.push        git push
util.print_env  print Fabric environment
```

## Usage

### collect config
hosts file required

```
$ fab role:router config.collect
```

### push collected config

```
$ fab git.push
```
