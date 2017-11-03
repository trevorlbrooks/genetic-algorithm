# Notes

## From pdf 

* Start with random
* Should add start index to gene objects 
    - This would allow for array splicing to get gene.
* Add a validate to gene class
* Normalized data set mutation recommended to be around .001
* Track best so far chromosome
* Continuous should likely use floats to represent. 
    - Must set a precision and decimal placement
* Continuous may benefit from a higher mutation rate 0.05 possibly
* Due to crossover, mating returns two individuals
* Use Haupt's Method for crossing over continuous data
    - Set a boolean for each gene saying whether or not is normalized
* For continuous a mutation should be continuous within range. For bit strings it is generally a flipped bit, but may need to check this in case of invalid end gene.
* If you keep fittest, the selection algorithm should only select from these, not the ones previously discarded.

## From assignment sheet
* Write minimum, maximum, and average for each generation to a file.
* Split data into testing and training data.
* Only test against training data during fitness testing? 
* Allow for manual entry of data (minus result) at run time to test 
* Check against training as well as test data for end result checking?

## Fitness notes
* For normalized
    - Add 1/num_genes if match
    - Multiply result by -1 if wrong answer
    - Stop if reach -1 or 1. 
    - Keep top fitness in test as result 
* For continuous
    - Need to find some way to weight result
        * Golf score manhattan distance?
        * Would need to figure out result effect
