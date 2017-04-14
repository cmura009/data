"""
 Python script to find the total amount of sales revenue for each city
 using Map-Reduce framework (mapper, combiner, and reducer functions) with mrjob package
 4/14/17
"""
from mrjob.job import MRJob

class CityRevenue(MRJob):
# each input lines consists of city, productCategory, price, and paymentMode

    def mapper(self, _, line):
        # create a key-value pair with key: city and value: price
        line_cols = line.split(',')
        yield line_cols[0], float(line_cols[2])

    def combiner(self, city, counts):
        # consolidates all key-value pairs of mapper function (performed at mapper nodes)
        yield city, sum(counts)

    def reducer(self, city, counts):
        # final consolidation of key-value pairs at reducer nodes
        yield city, '${:,.2f}'.format(sum(counts))


if __name__ == '__main__':
    CityRevenue.run()
