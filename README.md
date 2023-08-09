# Piotroski F-Score: A Trading Strategy

Just a repository to calculate the Piotroski F-score based on the financial statements of publicly traded, high Book-to-Market firms. To find the F-score, you need information from the balance sheet, the income statement, and the statement of cash-flow. Piotroski argues that these statements contain information about the future earnings of a firm which may not be priced in adequately by the market.

The Piotorski F-score is an integer score out of 9, which should distinguish potential winners from potential losers in the universe of high Book-to-Market firms. Piotroski identified 9 indicators which provide information about the profitability, the capital structure, and the efficiency of a firm. Each indicator gets assigned either a value of 1 (a positive signal) or 0 (a negative signal) depending on its value, constituting a score out of 9 in aggregate.

A trading strategy is derived and realized by going long on potential winners (with a high F-score) while shorting the potential losers (with a low F-score). 

Piotroski published his findings in:
- Piotroski, Joseph D. “Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers.” Journal of Accounting Research 38 (2000): 1–41. https://doi.org/10.2307/2672906.
