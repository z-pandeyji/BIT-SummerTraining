# Ablation Experiment

## Objective

Study the effect of chunk size on retrieval performance.

## Default Configuration

- Chunk Size: 120 words
- Overlap: 20 words

## Experiment

The chunk size was reduced to 80 words while keeping the overlap proportional.

## Observation

Smaller chunks produced more precise retrieval but increased the total number of chunks. Larger chunks provided more context but sometimes included unnecessary information.

## Conclusion

A chunk size of 120 words with 20-word overlap provided the best balance between retrieval accuracy and contextual completeness for this document collection.