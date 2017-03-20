import sys
from rocketchat_API.rocketchat import RocketChat

def main(argv):
  if len(argv) == 2 and argv[1] == 'config':
    print("graph_title RocketChat - user statistics")
    print("graph_category rocketchat")
    print("graph_vlabel Users")
    print("graph_args --base 1000 -l 0")
    print("total.type GAUGE")
    print("total.label total users")
    print("total.colour COLOUR8")
    print("online.type GAUGE")
    print("online.label online users")
    print("online.colour COLOUR0")
    print("away.type GAUGE")
    print("away.label away users")
    print("away.colour COLOUR2")
  else:
    rocketApi = RocketChat('user', 'pass')
    response = rocketApi.statistics()

    print('total.value %d' % response.json()['statistics']['totalUsers'])
    print('online.value %d' % response.json()['statistics']['onlineUsers'])
    print('away.value %d' % response.json()['statistics']['awayUsers'])
  return

if __name__ == "__main__":
  main(sys.argv)
