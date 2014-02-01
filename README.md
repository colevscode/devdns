devdns
==========

It does one thing: maps a custom TLD (like .dev) to an IP (like 127.0.0.1).

## Use

    sudo devdns
    sudo devdns test
    sudo devdns dev 192.168.1.110

By default devdns maps the `dev` TLD to `127.0.0.1`. This is probably all most people will need. The first argument, if specified will set a custom TLD like `test` (www.myserver.test). The second argument allows you to specify an IP address, for example the address of a server on your LAN.

You need to run it as root because it uses port 53, the standard DNS port. Also you'll want to add localhost (127.0.0.1) to the top of your DNS server list. I recommend adding google's DNS addresses (8.8.8.8 and 8.8.4.4) as backup servers.

![](http://raw.github.com/colevscode/devdns/master/dnsconfig.png)

## Credits

Much of this code was adopted from [minidns](https://code.google.com/p/minidns/) which itself borrowed heavily from [Francisco's recipe](http://code.activestate.com/recipes/491264-mini-fake-dns-server/).
