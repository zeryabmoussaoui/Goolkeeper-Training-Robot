import time
from pymavlink import mavutil

inputs ="0000"
"""##===============================================================================================================##"""
##Transitions

class Transition(object):
    def __init__(self, toState):
        self.toState = toState
    def Execute(self):
        print "Transitioning..."

"""##===============================================================================================================##"""
##States
class State(object):
    def __init__(self, FSM, shoot_pml=0,shoot_pmr=0, move_pml=0, move_pmr=0, shoot_state=False, move_state=False):

        self.FSM = FSM
        self.shoot_pml = shoot_pml
        self.shoot_pmr = shoot_pmr 
        self.move_pml = move_pml
        self.move_pmr = move_pmr
        self.shoot_state = shoot_state
        self.move_state = move_state 

    def Enter(self):
        pass
    def Execute(self):
        pass
    def Exit(self):
        pass 

class Initialisation(State):
    def __init__(self, FSM):
        super(Initialisation, self).__init__(FSM)
     
    def Enter(self):
         pass 
    def Execute(self):
         if inputs == "0000":
             print "State Initialisation activated !"     
         if inputs == "1000": 
             print "Nouvel Exercice !" 
             self.FSM.ToTransition("toMove")
             self.FSM.Execute()
    def Exit(self):
         print "State Initialisation disactivated !"

class Move(State):
    def __init__(self, FSM,  shoot_pml=0,shoot_pmr=0, move_pml=0, move_pmr=0, shoot_state=False, move_state=True):
        super(Move, self).__init__(FSM, shoot_pml,shoot_pmr, move_pml, move_pmr, shoot_state, move_state)
    
    def Enter(self):
       print "State Move activated !"
    
    def Execute(self):   
       mavutil.set_dialect("ardupilotmega")
       autopilot = mavutil.mavlink_connection('tcp:localhost:5762')   
       msg = None
# wait for autopilot connection
       while msg is None:
            msg = autopilot.recv_msg()
       print msg
# The values of these heartbeat fields is not really important here
# I just used the same numbers that QGC uses
# It is standard practice for any system communicating via mavlink emit the HEARTBEAT message at 1Hz! Your autopilot may not behave the way you want otherwise!

       autopilot.mav.heartbeat_send(
       6, # type
       8, # autopilot
       192, # base_mode
       0, # custom_mode
       4, # system_status
       3  # mavlink_version
       )

       autopilot.mav.command_long_send(
       1, # autopilot system id
       1, # autopilot component id
       400, # command id, ARM/DISARM
       0, # confirmation
       1, # arm!
       0,0,0,0,0,0 # unused parameters for this command
       )
       time.sleep(2)
       autopilot.set_mode_manual()
       autopilot.mav.rc_channels_override_send(autopilot.target_system, autopilot.target_component, 0, 2000, 2000, 0, 0, 0, 0, 0)
       time.sleep(10)
       global inputs
       inputs="1100"
       if  inputs == "1100":
           self.FSM.ToTransition("toShoot") 
           self.FSM.Execute()
    def Exit(self):
        print "State Move disactivated !"
       
class Shoot(State):

    def Enter(self):
        print "State Shoot activated !"

    def Execute(self):
        global inputs        
        inputs = "0110"
        if  inputs == "0110":
            self.FSM.ToTransition("toAnalize") 
            self.FSM.Execute()
    def Exit(self):
        print "State Shoot disactivated !"

class Analize(State):

    def Enter(self):
        print "State Analize activated !"

    def Execute(self):
        global inputs        
        inputs = "0001"
        if  inputs == "0001":
            self.FSM.ToTransition("toAnalize") 
            self.FSM.Execute()
        if  inputs == "1101":
            self.FSM.ToTransition("toShoot") 
            self.FSM.Execute()
        if  inputs == "1001":
            self.FSM.ToTransition("toMove") 
            self.FSM.Execute()

    def Exit(self):
        print "State Analize disactivated !"
      


