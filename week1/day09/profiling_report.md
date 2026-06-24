# Profiling Report

## Objective

Analyze and optimize a recursive Fibonacci implementation.

---

## Before Optimization

Method:
- Recursive Fibonacci
- No caching

Observations:
- Repeated calculations
- Exponential time complexity
- Slow execution for larger inputs

---

## Optimization Applied

Technique:
- functools.lru_cache

Benefits:
- Eliminates repeated computations
- Stores previously computed values
- Significant performance improvement

---

## Results

Benchmark completed using n=35.

Observed:
- Optimized version significantly faster
- Same output correctness maintained

---

## Conclusion

Caching dramatically improves recursive algorithm performance by avoiding redundant computations.