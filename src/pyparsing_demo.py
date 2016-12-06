import pyparsing as pp

wc_var = pp.Regex('WC')
operator = pp.Regex('=').setName("operator")
wc_values = pp.Regex('"[^"]+"')
ts_var = pp.Regex('TS')
ts_values = pp.Regex('[(][^()]+[)]')
wc_group = pp.Group(wc_var + operator + wc_values)
wc_condition = pp.operatorPrecedence(wc_group, [
    ("AND", 2, pp.opAssoc.LEFT,),
    ("OR", 2, pp.opAssoc.LEFT,),
])
ts_group = pp.Group(ts_var + operator + ts_values)
ts_condition = pp.operatorPrecedence(ts_group, [
    ("AND", 2, pp.opAssoc.LEFT,),
    ("OR", 2, pp.opAssoc.LEFT,),
])

query_pattern = '(' + wc_condition + ')' + 'AND' + '(' + ts_condition + ')'

query = '(WC = "Engineering, Aerospace" OR WC = "Engineering, Electrical & Electronic" OR WC = "Robotics" OR WC = "Telecommunications" OR WC = "Transportation" OR WC = "Transportation Science & Technology" OR WC = "Urban Studies") AND (TS = (magnet* NEAR/1 levit*) OR TS = (freight NEAR/1 transport) OR TS = (high-spe* NEAR/1 line*) OR TS = (rail NEAR/1 transport*) OR TS = (railroad NEAR/1 track*) OR TS = (railroad NEAR/1 engin*) OR TS = (Vehicle-to-Vehicl*) OR TS = (high-spe* NEAR/1 transport*) OR TS = (Tube NEAR/1 Transport) OR TS = (high-spe* NEAR/1 vehicl*) OR TS = (Hyperloop) OR TS = (digit* NEAR/1 age NEAR/1 transport*) OR TS = (high-spe* NEAR/1 magnet* NEAR/1 levit* NEAR/1 transport) OR TS = (Railroad NEAR/1 Vehicl*) OR TS = (maglev) OR TS = (vehicl* NEAR/1 rout* NEAR/1 problem) OR TS = (passeng* NEAR/1 vehicl*) OR TS = (commerci* NEAR/1 vehicl*) OR TS = (vehicl* NEAR/1 rout*) OR TS = (vehicl* NEAR/1 size) OR TS = (public NEAR/1 transport) OR TS = (vehicl* NEAR/1 fleet) OR TS = (autonom* NEAR/1 vehicl*) OR TS = (road NEAR/1 condit*) OR TS = (unman* NEAR/1 aerial NEAR/1 vehicl*) OR TS = (electr* NEAR/1 vehicl*) OR TS = (hybrid NEAR/1 electr* NEAR/1 vehicl*) OR TS = (fuel NEAR/1 consumpt*) OR TS = (plug-in NEAR/1 hybrid NEAR/1 electr* NEAR/1 vehicl*) OR TS = (hybrid NEAR/1 vehicl*) OR TS = (dc-dc NEAR/1 convert*) OR TS = (plug-in NEAR/1 electr* NEAR/1 vehicl*) OR TS = (dc/dc convert*) OR TS = (traffic NEAR/1 flow) OR TS = (motor NEAR/1 vehicl*) OR TS = (probe NEAR/1 vehicl*) OR TS = (vehicular NEAR/1 network) OR TS = (intellig* NEAR/1 transport* NEAR/1 system) OR TS = (traffic NEAR/1 safet*) OR TS = (road NEAR/1 safet*) OR TS = (vehicle-to-vehicl* NEAR/1 commun*) OR TS = (move NEAR/1 vehicl*) OR TS = (individu* NEAR/1 vehicl*) OR TS = (multipl* NEAR/1 vehicl*) OR TS = (transmiss* NEAR/1 rang*) OR TS = (magnet* NEAR/1 levit* NEAR/1 transport))'

print(query_pattern.parseString(query))