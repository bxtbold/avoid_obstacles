def callback(msg):
   global range_ahead
   range_ahead = min(msg.ranges)
