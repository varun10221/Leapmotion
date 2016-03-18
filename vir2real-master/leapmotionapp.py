import sys
import Leap
from PalmControl import PalmControlListener

def main():
	host = "localhost"
	port = 9999
	listener = PalmControlListener(host, port)
	controller = Leap.Controller()
	controller.set_policy(controller.POLICY_BACKGROUND_FRAMES)
	controller.add_listener(listener)

	print "Press Enter to quit..."
	sys.stdin.readline()
	controller.remove_listener(listener)

main()
