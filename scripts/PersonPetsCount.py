"""
 Python script to find the pet count for each pet owner
 using Map-Reduce framework (mapper, combiner, and reducer functions) with mrjob package
 4/14/17
"""
from mrjob.job import MRJob

class PersonPetsCount(MRJob):
# each input lines consists of petOwner, and petName

    def mapper(self, _, line):
        # create a key-value pair with key: petOwner and value: 1
        line_cols = line.split(',')
        yield line_cols[0], 1

    def combiner(self, category, counts):
        # consolidates all key-value pairs of mapper function (performed at mapper nodes)
        yield category, sum(counts)

    def reducer(self, category, counts):
        # final consolidation of key-value pairs at reducer nodes
        yield category, sum(counts)


if __name__ == '__main__':
    PersonPetsCount.run()
