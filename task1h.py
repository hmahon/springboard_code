# got a 100% here


from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("local").setAppName("task1")
sc = SparkContext(conf=conf)

def parseLines(line):
    fields = line.split(",")
    rk = int(fields[0])
    player_name = fields[1]
    pos = fields[2]
    team = fields[3]
    conf = fields[4]
    gp = int(fields[5])
    ppg = float(fields[7])
    ast = int(fields[8])
    return (rk, player_name, pos, team, conf, gp, ppg, ast)
    

lines = sc.textFile("file:///SparkCourse/nba1.csv")
nba1 = lines.map(parseLines)

under25 = nba1.filter(lambda x: x[6] < 25)
under25_sorted = under25.map(lambda x: (x[1], x[0], x[6], x[2], x[3])).sortByKey(ascending=False)


#under25_sorted.saveAsTextFile("file:///SparkCourse/task1.csv")

under25_sorted.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("file:///SparkCourse/task1.csv")  ###need to remember this!!!
#under25_sorted.map(lambda x: "\t".join(map(str, x))).coalesce(1).saveAsTextFile("file:///SparkCourse/task1")    # for tab delimited