# tex project

By `sander.lentink@os3.nl`

## Compile

To compile the tex document, we first express which to compile.
```shell
export TARGET=[proposal|paper|presentation]
```
followed by compiling it
```shell
docker-compose up
```

We we made change to the bibliography,
we need to clear the cache by running
```shell
docker-compose stop && docker-compose rm -vf && docker-compose up
```

