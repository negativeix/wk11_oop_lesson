import csv, os

__location__ = os.path.realpath(
os.path.join(os.getcwd(), os.path.dirname(__file__)))

class TableDB:
    def __init__(self):
        self.table_database = []
        self.table = []

    def insert(self, table):
        with open(os.path.join(__location__, table)) as f:
            reader = csv.DictReader(f)
            self.table_database = list(reader)

    def search(self, table_name):
        pass
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.cur = TableDB()
        self.cur.insert(table)
        self.table_database = self.cur.table_database
        self.table = []

    def filter(self, condition):
        for item in self.table_database:
            if condition(item):
                self.table.append(item)
        return self.table

    def aggregate(self, aggregation_function, aggregation_key):
        aggregated_list = [float(i[aggregation_key]) for i in self.table]
        print (aggregation_function(aggregated_list))

    def __str__(self):
        return ('Table: '+str(self.table)+'\n'
                +'Table Name: '+str(self.table_name))


x = Table('Italy','Cities.csv')
s = x.table_name
x.filter(lambda x: x['country'] == s)
x.aggregate((lambda x:sum(x)/len(x)),'temperature')
print(x)








# print(y)

# Let's write code to
# - print the average temperature for all the cities in Italy
#aggregate ('temperature',(lambda x:sum(x)/len(x)), filter( lambda x: x['country'] == 'Italy', cities))
# - print the average temperature for all the cities in Sweden
#aggregate ('temperature',(lambda x:sum(x)/len(x)), filter(lambda x: x['country'] == 'Sweden', cities))
# - print the min temperature for all the cities in Italy
#aggregate ('temperature',(lambda x:min(x)), filter(lambda x: x['country'] == 'Italy', cities))
# - print the max temperature for all the cities in Sweden
#aggregate ('temperature',(lambda x:max(x)), filter(lambda x: x['country'] == 'Sweden', cities))