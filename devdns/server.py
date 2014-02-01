import sys
import socket

__all__ = ['connect', 'get_data']

# DNSQuery class from http://code.activestate.com/recipes/491264-mini-fake-dns-server/
class DNSQuery:
  def __init__(self, data):
    self.data=data
    self.domain=''

    tipo = (ord(data[2]) >> 3) & 15   # Opcode bits
    if tipo == 0:                     # Standard query
      ini=12
      lon=ord(data[ini])
      while lon != 0:
        self.domain+=data[ini+1:ini+lon+1]+'.'
        ini+=lon+1
        lon=ord(data[ini])

  def response(self, ip, tld):
    packet=''
    if self.domain.endswith('.%s.'%tld):
      packet+=self.data[:2] + "\x81\x80"
      packet+=self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'   # Questions and Answers Counts
      packet+=self.data[12:]                                         # Original Domain Name Question
      packet+='\xc0\x0c'                                             # Pointer to domain name
      packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'             # Response type, ttl and resource data length -> 4 bytes
      packet+=str.join('',map(lambda x: chr(int(x)), ip.split('.'))) # 4bytes of IP
    return packet


def connect():
  try:
    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.setblocking(False)
    udps.bind(('',53))
  except Exception, e:
    print "Failed to create socket on UDP port 53:", e
    sys.exit(1)
  return udps


def get_data(udps, tld, ip, verbose=False):
  try:
    data, addr = udps.recvfrom(1024)
    p=DNSQuery(data)
    r=p.response(ip, tld)
    if r and verbose:
      print 'DNS Request: %s -> %s' % (p.domain, ip)
    udps.sendto(r, addr)
  except socket.error:
    pass


def usage():
  print ""
  print "Usage:"
  print ""
  print "\t# devdns [tld] [ip]"
  print ""
  print "Description:"
  print ""
  print "\tMiniDNS will respond to all DNS queries with a single IPv4 address."
  print ""
  print "\tYou may specify the tld for local development as the first argument on the command line:\n"
  print "\t\t# devdns test \n"
  print "\tIf no IP address is specified, 'dev' will be used."
  print ""
  print "\tYou may specify the IP address to be returned as the second argument on the command line:\n"
  print "\t\t# devdns dev 1.2.3.4\n"
  print "\tIf no IP address is specified, 127.0.0.1 will be used."
  print ""

  sys.exit(1)


if __name__ == '__main__':

  tld = 'dev'
  ip = '127.0.0.1'

  if len(sys.argv) > 3 or '-h' in sys.argv or '--help' in sys.argv:
    usage()
  elif len(sys.argv) > 1:
    tld = sys.argv[1]
    if len(sys.argv) > 2:
      ip = sys.argv[2]

  udps = connect()

  print 'devDNS :: *.%s. 60 IN A %s\n' % (tld, ip)
  
  try:
    while 1:
      get_data(udps, tld, ip)
  except KeyboardInterrupt:
    print '\nBye!'
    udps.close()

