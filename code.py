print "\n" * 100
pbs_rate = 5
pbs_required = {
    "Daniel":250,
    "James":500,
    "Katie":750,
    "Abby":1000,
    }

M16_required = {
    "Daniel":"Y",
    "James":"Y",
    "Katie":"N",
    "Abby":"Y",
    }




def employee_register():
    """
    Code for registering Employee information.
    """

def employee_register():
    """
    Code for registering Customer information.
    """

def party_total():
    total = 0
    multiplier = 0
    pbs_cost_list = []
    m16_cost_list = []
    party_instr = ["50", "100"]
    """
    Code for working out an estimated total cost,
    for each paintball party.
    """
    for key in M16_required:
        m16_cost_list.append(M16_required[key])
        
    for key in pbs_required:
        pbs_cost_list.append(pbs_required[key])
        
    for i in pbs_cost_list:
        temp = i
        mp = 0
        while temp >= 100:
            mp += 1
            temp -= 100
        temp = (5 * mp)
        total += temp
    for i in m16_cost_list:
        if i == "Y":
            total += 20
    request = raw_input(str("0 = $50 Trainee Instructor , 1 = $100 Fully Qualified Instructor:   "))
    if request == 0:
        total += 50
    elif request == 1:
        total += 100
    print "#Party -  Total Cost#"
    print "\n" * 3
    print ("Total: $ %s" % total)
    print total
    

def information_search():
    """
    Code for searching employee information.
    """


