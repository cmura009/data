"""
 Python script to find the number of sales transactions for each product category
 using Map-Reduce framework (mapper, combiner, and reducer functions) with mrjob package
 4/14/17
"""
from mrjob.job import MRJob

class CategoryCount(MRJob):
# each input lines consists of city, productCategory, price, and paymentMode

    def mapper(self, _, line):
        # create a key-value pair with key: product category and value: 1
        line_cols = line.split(',')
        yield line_cols[1], 1

    def combiner(self, category, counts):
        # consolidates all key-value pairs of mapper function (performed at mapper nodes)
        yield category, sum(counts)

    def reducer(self, category, counts):
        # final consolidation of key-value pairs at reducer nodes
        yield category, sum(counts)


if __name__ == '__main__':
    CategoryCount.run()
