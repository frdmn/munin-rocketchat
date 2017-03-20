import sys
from rocketchat_API.rocketchat import RocketChat

def main(argv):
  if len(argv) == 2 and argv[1] == 'config':
    print("graph_title RocketChat - message statistics")
    print("graph_category rocketchat")
    print("graph_vlabel Messages")
    print("graph_args --base 1000 -l 0")
    print("total.type GAUGE")
    print("total.label total messages")
    print("total.colour COLOUR8")
    print("channel.type GAUGE")
    print("channel.label channel messages")
    print("channel.colour COLOUR0")
    print("group.type GAUGE")
    print("group.label group messages")
    print("group.colour COLOUR15")
    print("direct.type GAUGE")
    print("direct.label direct messages")
    print("direct.colour COLOUR18")
  else:
    rocketApi = RocketChat('user', 'pass')
    response = rocketApi.statistics()

    print('total.value %d' % response.json()['statistics']['totalChannelMessages'])
    print('channel.value %d' % response.json()['statistics']['totalChannelMessages'])
    print('group.value %d' % response.json()['statistics']['totalPrivateGroupMessages'])
    print('direct.value %d' % response.json()['statistics']['totalDirectMessages'])
  return

if __name__ == "__main__":
  main(sys.argv)
