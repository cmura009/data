"""
What is the city that had the highest total amount of gross revenue?

Python script to find the total amount of revenue for each city, then find the city 
with the maximum gross revenue using Map-Reduce framework (mapper, combiner, and reducer functions) 
with mrjob package

 Python script to find the total amount of sales revenue for each city
 using Map-Reduce framework (mapper, combiner, and reducer functions) with mrjob package
 4/14/17
"""
from mrjob.job import MRJob

class maxRevenue(MRJob):
# each input lines consists of city, productCategory, revenue, and paymentMode

    def mapper(self, _, line):
        # create a key-value pair with key: city and value: revenue
        line_cols = line.split(',')
        yield line_cols[0], float(line_cols[2])

    def combiner(self, city, counts):
        # consolidates all key-value pairs of mapper function (performed at mapper nodes)
        yield city, sum(counts)

    def reducer(self, city, counts):
        # consolidation of key-value pairs at reducer nodes
        yield city, '${:,.2f}'.format(sum(counts))

    def reducer(self, city, counts):
        # consilation of key-vaue pairs at reducer nodes
        maxRev = next(counts)
        for item in counts:
            max_temp = max(item, maxRev)
        yield city, maxRev


if __name__ == '__main__':
    maxRevenue.run()