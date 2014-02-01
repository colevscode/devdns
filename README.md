devdns
==========

It does one thing: maps a custom TLD (like .dev) to an IP (like 127.0.0.1).

## Use

    devdns
    devdns test
    devdns dev 192.168.1.110

By default devdns maps the `dev` TLD to `127.0.0.1`. This is probably all most people will need. The first argument, if specified will set a custom TLD like `test` (www.myserver.test). The second argument allows you to specify an IP address, for example the address of a server on your LAN.


## Credits

Much of this code was adopted from [minidns](https://code.google.com/p/minidns/) which itself borrowed heavily from [Frederic's recipe](http://code.activestate.com/recipes/491264-mini-fake-dns-server/).
