# A/B Test Results

## Objective

Evaluate whether the experimental variant produced a meaningful improvement in order revenue or return rate compared with the control group.

## Experiment Summary

| Metric | Control | Variant |
|---|---:|---:|
| Orders | 7,620 | 7,380 |
| Mean Revenue per Order | 5,107.17 | 5,032.33 |
| Total Revenue | 38,916,621.54 | 37,138,572.31 |
| Return Rate | 9.53% | 9.13% |

## Observed Effect

- Mean revenue difference: **-1.47%**
- Return-rate difference: **-0.39 percentage points**

The variant shows a slightly lower average order revenue and a slightly lower return rate.

## Hypotheses

### Revenue

**Null hypothesis (H0):**
There is no statistically significant difference in mean order revenue between the control and variant groups.

**Alternative hypothesis (H1):**
There is a statistically significant difference in mean order revenue between the groups.

### Return Rate

**Null hypothesis (H0):**
Return behaviour is independent of experiment group.

**Alternative hypothesis (H1):**
Return behaviour differs between the control and variant groups.

## Statistical Tests

Revenue was evaluated using an independent two-sample t-test.

- Revenue p-value: **0.44078**

Return-rate differences were evaluated using a chi-square test.

- Return-rate p-value: **0.42206**

Significance threshold:

**alpha = 0.05**

## Interpretation

Both p-values are greater than 0.05.

Therefore, we **fail to reject the null hypothesis** for both revenue and return rate.

Although the variant had approximately 1.47% lower mean revenue and a 0.39 percentage-point lower return rate, the observed differences are not statistically significant.

The results do not provide sufficient evidence to conclude that the variant materially improves or worsens business performance.

## Business Recommendation

Do not roll out the variant solely on the basis of this experiment.

Recommended next steps:

1. Run the experiment for a longer period or increase sample size if a smaller detectable effect is commercially important.
2. Review results by customer segment, product category, channel and device.
3. Define the minimum business-relevant effect size before the next experiment.
4. Evaluate secondary metrics such as conversion rate, repeat purchase behaviour and contribution margin.
5. Check experiment assignment and data-quality assumptions before making a production decision.

## Analyst Takeaway

A numerically different result is not automatically a statistically meaningful result.

The business decision should consider statistical significance, effect size, sample size and commercial relevance together.
