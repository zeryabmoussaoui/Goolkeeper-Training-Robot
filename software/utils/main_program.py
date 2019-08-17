# In the main program, we program the state machine 
# import all the sub programs that represent the different states and extra features like the LEDs indicators
# import ....

"""##===============================================================================================================##"""
## Finite State Machine :

class FSM(object):
    def __init__(self, character):
        self.char=character
        self.states = {}
        self.transitions = {}         
        self.curState = None
        self.trans = None

    def AddState(self, stateName, state):
        self.states[stateName] = state

    def AddTransition(self, transName, transition):
        self.transitions[transName] = transition
    
    def SetState(self, stateName):
        self.curState = self.states[stateName]
    
    def ToTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    def Execute(self):
        if(self.trans):
              self.curState.Exit()
              self.trans.Execute()
              self.SetState(self.trans.toState) #toState ? 
              self.curState.Enter()
              self.trans = None
        self.curState.Execute()

"""##===============================================================================================================##"""
## IMPLEMENTATION 

Char= type("Char",(object,),{})

class Robot(Char):
    def __init__(self):
        self.FSM=FSM(self)

        ##STATES
        self.FSM.AddState("Initialisation", Initialisation(self.FSM))
        self.FSM.AddState("Move", Move(self.FSM))
        self.FSM.AddState("Analize", Analize(self.FSM))
        self.FSM.AddState("Shoot", Shoot(self.FSM))        	

        ##TRANSITIONS
        self.FSM.AddTransition("toInitialisation", Transition("Initialisation"))
        self.FSM.AddTransition("toMove", Transition("Move"))
        self.FSM.AddTransition("toShoot", Transition("Shoot"))
        self.FSM.AddTransition("toAnalize", Transition("Analize"))

        self.FSM.SetState("Initialisation")

    def Execute(self):
        self.FSM.Execute()

    def SetState(self, stateName):
        self.FSM.SetState(stateName)
    
    def ToTransition(self, toTrans):
        self.FSM.ToTransition(toTrans)

    def Update(self):
        global inputs
        # Updates
        inputs = "1000"
"""##===============================================================================================================##"""
#Main Program
if __name__ == '__main__':
    r = Robot()
    while True:
         r.Execute()
         r.Update()
         r.Execute()
