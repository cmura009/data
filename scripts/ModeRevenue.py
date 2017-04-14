"""
 Python script to find the total amount of sales revenue for each payment mode
 using Map-Reduce framework (mapper, combiner, and reducer functions) with mrjob package
 4/14/17
"""
from mrjob.job import MRJob

class ModeRevenue(MRJob):
# each input lines consists of city, productCategory, price, and paymentMode

    # Initialize the count value
    count = 0

    def mapper(self, _, line):
        # create a key-value pair with key: paymentMode and value: price
        line_cols = line.split(',')
        yield line_cols[3], float(line_cols[2])

    def combiner(self, mode, counts):
        # consolidates all key-value pairs of mapper function (performed at mapper nodes)
        yield mode, sum(counts)

    def reducer(self, mode, counts):
        # final consolidation of key-value pairs at reducer nodes
        self.count += 1
        
        if self.count <= 5:
          yield mode, '${:,.2f}'.format(sum(counts))


if __name__ == '__main__':
    ModeRevenue.run()
