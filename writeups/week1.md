# ChronosMatch — Week 1 Progress Report

## 1. Project Overview

ChronosMatch is a Python-based project that simulates a basic financial order matching engine. Its purpose is to match buy and sell orders according to their prices and available quantities.

## 2. Objectives

- Create a structured representation of trading orders.
- Implement basic buy and sell order matching.
- Support partial fills when order quantities differ.
- Test the matching logic using automated unit tests.
- Maintain project code using Git and GitHub.

## 3. Work Completed

### 3.1 Order Model

Created an `Order` dataclass containing:
- Order ID
- Order side (BUY or SELL)
- Price
- Quantity

### 3.2 Order Matching Engine

Implemented matching logic that checks whether the buy price is greater than or equal to the sell price.

When a match is possible, the engine executes a trade at the sell order's price and updates the remaining quantities.

### 3.3 Partial Order Fills

Extended the matching engine to process one buy order against multiple sell orders. The engine records individual trades and updates the quantities remaining after each match.

### 3.4 Automated Testing

Created unit tests using Python's `unittest` framework.

The following three tests passed:
1. Partial fill of a buy order.
2. No trade when the buy price is lower than the sell price.
3. Matching one buy order against multiple sell orders.

### 3.5 Version Control

Created and maintained a GitHub repository for ChronosMatch. Committed and pushed the implementation, tests, and Python `.gitignore` configuration.

## 4. Testing Results

Command used:

`python -m unittest -v`

Result: **3 tests passed successfully.**

The example matching scenario executed two trades: 4 units at 98.0 and 3 units at 99.0. The buy order began with 10 units and had 3 units remaining.

## 5. Current Limitations

The current implementation is a basic simulation. It does not yet include a complete price-prioritized order book, an asynchronous mock market feed, a memory-mapped ring buffer, or advanced latency measurements.

## 6. Planned Next Steps

- Improve order-book management and price prioritization.
- Add further validation and automated tests.
- Explore asynchronous processing and a simulated market feed.
- Investigate the planned ring-buffer and performance features.
- Document further development and testing results.

## 7. Conclusion

The initial ChronosMatch matching engine has been implemented and tested successfully. The project currently supports basic matching, partial fills, multiple sell orders, and automated tests. Further development is required to implement the advanced features in the project roadmap.