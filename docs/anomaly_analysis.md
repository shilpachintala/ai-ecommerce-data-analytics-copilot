# Revenue & Operational Anomaly Analysis

## Objective

Identify unusual daily business-performance patterns that may require further investigation.

The analysis evaluates multiple operational metrics together rather than relying on a single fixed revenue threshold.

## Dataset

- Total days analysed: **610**
- Anomaly days identified: **19**
- Anomaly rate: **3.11%**

## Method

An Isolation Forest model was applied to daily KPI features including:

- Revenue
- Order volume
- Return rate

Rolling revenue metrics were also generated to provide short- and medium-term trend context.

The model flags observations that behave differently from the overall distribution of daily operational performance.

## Key Observations

Several high-revenue days were identified as unusual, including:

| Date | Revenue | Orders | Return Rate |
|---|---:|---:|---:|
| 2026-07-16 | 288,994.23 | 34 | 2.94% |
| 2025-05-13 | 262,548.88 | 40 | 2.50% |
| 2025-08-29 | 253,341.51 | 29 | 6.90% |
| 2026-07-04 | 253,006.90 | 32 | 9.38% |
| 2025-04-17 | 218,857.38 | 36 | 16.67% |

Some lower-revenue days were also flagged because anomaly detection considers combinations of metrics rather than revenue alone.

## Business Interpretation

An anomaly does not automatically indicate an error or negative business event.

Potential explanations include:

- Promotional campaigns
- Seasonal demand spikes
- Large-value purchases
- Product-mix changes
- Operational disruptions
- Elevated return behaviour
- Data-quality issues
- Changes in customer or channel behaviour

Each flagged day should therefore be investigated with additional dimensions such as product category, customer segment, channel, discount level and geography.

## Recommended Follow-Up

1. Compare anomalous days with promotional and campaign calendars.
2. Drill down by product category, channel and customer segment.
3. Review return-rate spikes independently from revenue anomalies.
4. Validate unusual observations against source-data quality checks.
5. Surface anomaly indicators in Power BI for operational monitoring.
6. Investigate repeated anomaly patterns rather than treating each flag independently.

## Analyst Takeaway

Machine-learning anomaly detection should be used as an investigation tool rather than an automatic decision mechanism.

The model helps prioritize unusual observations, while business context and additional analysis determine whether an anomaly represents an opportunity, operational issue or normal variation.
