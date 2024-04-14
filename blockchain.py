#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from node import Block

node_1 = MyOwnPeer2PeerNode("10.20.1.105", 8001, 1, [Block.create_genesis_block(), Block(1), Block(2)])
node_2 = MyOwnPeer2PeerNode("10.20.1.105", 8002, 2)
node_3 = MyOwnPeer2PeerNode("10.20.1.105", 8003, 3)

time.sleep(1)

node_1.start()
node_2.start()
node_3.start()

time.sleep(1)

debug = True
node_1.debug = debug
node_2.debug = debug
node_3.debug = debug

node_1.connect_with_node('10.20.1.105', 8002)
node_2.connect_with_node('10.20.1.105', 8003)
node_3.connect_with_node('10.20.1.105', 8001)

time.sleep(2)

node_1.send_to_nodes("message: Hi there!")


node_1.send_to_nodes(node_1.get_chain_string())


time.sleep(10)

node_1.stop()
time.sleep(10)
node_2.stop()
time.sleep(10)
node_3.stop()
print('end test')