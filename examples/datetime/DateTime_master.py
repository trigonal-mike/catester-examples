import datetime

var_date = datetime.date.today()
var_time = datetime.datetime.now().time()
var_datetime = datetime.datetime.now()
var_duration = datetime.timedelta(days=5, hours=3)

#$VARIABLETEST datetime
#$TESTVAR var_date
#$TESTVAR var_time
#$TESTVAR var_datetime
#$TESTVAR var_duration