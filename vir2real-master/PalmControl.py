import math
import Leap
import json
from LPClient import LeapMotionWSClient

class PalmControlListener(Leap.Listener):
	def __init__(self, host, port):
		super(PalmControlListener, self).__init__()
		self.client = LeapMotionWSClient(host, port)

	def on_init(self, controller):
		print "Initialized"

	def on_connect(self, controller):
		print "Connected"

	def on_disconnect(self, controller):
		print "Disconnected"

	def on_frame(self, controller):
		frame = controller.frame()
		if not frame.hands.is_empty:
			if len(frame.hands) < 2:
				self.one_hand_gesture_recognition(frame.hands[0])
			else:
				#right_hand = max(frame.hands, key=lambda hand: hand.palm_position.x)
				#left_hand = min(frame.hands, key=lambda hand: hand.palm_position.x)
				right_hand = frame.hands.rightmost
				left_hand = frame.hands.leftmost
				self.two_hand_gesture_recognition(left_hand, right_hand)

	def one_hand_gesture_recognition(self, hand):
		if hand.grab_strength < 0.5:
			normal = hand.palm_normal
			velocity = hand.palm_velocity
			cmd_dict = {'action': 'explore', 'normal_x': normal.x, 'normal_y': normal.y, 'normal_z': normal.z, 'velocity_x': velocity.x, 'velocity_y': velocity.y, 'velocity_z': velocity.z}
			send_data = json.dumps(cmd_dict)
			#send_data += '&'
			self.client.send(send_data)

	def two_hand_gesture_recognition(self, left_hand, right_hand):
		pass
