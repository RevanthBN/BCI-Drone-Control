import argparse
import math

from pythonosc import osc_server


class SimpleServer(osc_server):

  def handle(self, address, message, time):
    if message.is_bundle():
      for msg in message:
        print(time, address, msg.address, msg.args)
    else:
      print(time, address, message.address, message.args)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=8000, help="The port to listen on")
  args = parser.parse_args()

  server = SimpleServer(args.ip, args.port)

  print("Serving on {}".format(server.server_address))
  server.serve_forever()
