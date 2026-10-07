class StockSpanner:
    def __init__(self):
        # Stack stores tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # While the stack is not empty and the current price is >= the top of the stack
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the popped element to our current span
            span += self.stack.pop()[1]
            
        self.stack.append((price, span))
        return span