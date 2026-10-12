# Review volume report

Run time UTC: 2026-10-12T06:25:18Z

Window: 2026-07-14T06:25:18Z through 2026-10-12T06:25:18Z, inclusive.

Total rows before cap: 26000

Total rows after cap: 26000

Cap: 200000; sampling seed: 42.

Counts before cap are unique, nonempty reviews retrieved from the configured locales. They are not the total universe of store reviews: feeds can stop before the window is covered. Country is populated only for iOS and records the first storefront that returned a review, not reviewer residence. Android country is empty; store_lang records the first Play language stream that returned each review.

## By platform

| Platform | Before cap | After cap |
| --- | --- | --- |
| android | 23692 | 23692 |
| ios | 2308 | 2308 |

## iOS by storefront

| Storefront | Before cap | After cap |
| --- | --- | --- |
| au | 97 | 97 |
| br | 188 | 188 |
| ca | 181 | 181 |
| de | 178 | 178 |
| es | 128 | 128 |
| fr | 224 | 224 |
| gb | 186 | 186 |
| in | 190 | 190 |
| jp | 238 | 238 |
| kr | 128 | 128 |
| mx | 104 | 104 |
| sg | 16 | 16 |
| us | 450 | 450 |

## Android by store_lang

| Store language | Before cap | After cap |
| --- | --- | --- |
| ar | 817 | 817 |
| bg | 22 | 22 |
| bn | 12 | 12 |
| ca | 10 | 10 |
| cs | 49 | 49 |
| da | 14 | 14 |
| de | 449 | 449 |
| el | 32 | 32 |
| en | 11679 | 11679 |
| es | 2379 | 2379 |
| fa | 307 | 307 |
| fi | 9 | 9 |
| fil | 1 | 1 |
| fr | 1943 | 1943 |
| hi | 13 | 13 |
| hr | 18 | 18 |
| hu | 35 | 35 |
| id | 755 | 755 |
| it | 337 | 337 |
| iw | 57 | 57 |
| ja | 194 | 194 |
| ko | 329 | 329 |
| mr | 2 | 2 |
| ms | 19 | 19 |
| nb | 14 | 14 |
| nl | 71 | 71 |
| pl | 149 | 149 |
| pt | 1464 | 1464 |
| ro | 57 | 57 |
| ru | 804 | 804 |
| sk | 23 | 23 |
| sr | 14 | 14 |
| sv | 26 | 26 |
| ta | 1 | 1 |
| th | 188 | 188 |
| tr | 450 | 450 |
| uk | 144 | 144 |
| ur | 1 | 1 |
| vi | 314 | 314 |
| zh-CN | 384 | 384 |
| zh-TW | 106 | 106 |

## By UTC week (Monday start)

| Week starting | Before cap | After cap |
| --- | --- | --- |
| 2026-07-13 | 1775 | 1775 |
| 2026-07-20 | 2022 | 2022 |
| 2026-07-27 | 1817 | 1817 |
| 2026-08-03 | 1847 | 1847 |
| 2026-08-10 | 1713 | 1713 |
| 2026-08-17 | 1731 | 1731 |
| 2026-08-24 | 1798 | 1798 |
| 2026-08-31 | 2136 | 2136 |
| 2026-09-07 | 2187 | 2187 |
| 2026-09-14 | 2110 | 2110 |
| 2026-09-21 | 2174 | 2174 |
| 2026-09-28 | 2367 | 2367 |
| 2026-10-05 | 2323 | 2323 |

## By star rating per platform

| Platform | Stars | Before cap | After cap |
| --- | --- | --- | --- |
| android | 1 | 5181 | 5181 |
| android | 2 | 912 | 912 |
| android | 3 | 1175 | 1175 |
| android | 4 | 2049 | 2049 |
| android | 5 | 14375 | 14375 |
| ios | 1 | 833 | 833 |
| ios | 2 | 131 | 131 |
| ios | 3 | 152 | 152 |
| ios | 4 | 132 | 132 |
| ios | 5 | 1060 | 1060 |

## Review text lengths and shares

Lengths count Unicode characters in the unmodified body. Words use whitespace splitting; this is not language-aware tokenization. P90 uses linear interpolation.

| Dataset | Platform | Rows | Median chars | P90 chars | Under 4 words | Non-ASCII |
| --- | --- | --- | --- | --- | --- | --- |
| Before cap | all | 26000 | 36.0 | 241.0 | 35.75% | 40.08% |
| Before cap | android | 23692 | 33.0 | 227.0 | 37.20% | 38.27% |
| Before cap | ios | 2308 | 86.0 | 387.3 | 20.84% | 58.71% |
| After cap | all | 26000 | 36.0 | 241.0 | 35.75% | 40.08% |
| After cap | android | 23692 | 33.0 | 227.0 | 37.20% | 38.27% |
| After cap | ios | 2308 | 86.0 | 387.3 | 20.84% | 58.71% |

## Date ranges

| Dataset | Platform | Earliest date | Latest date |
| --- | --- | --- | --- |
| Before cap | android | 2026-07-14 | 2026-10-11 |
| Before cap | ios | 2026-07-14 | 2026-10-11 |
| After cap | android | 2026-07-14 | 2026-10-11 |
| After cap | ios | 2026-07-14 | 2026-10-11 |

Hours between run time and newest review (before cap): android: 24.01 hours; ios: 28.52 hours.

## Google Play language contributions (before cap)

| Language | Pages served | Rows fetched | In-window rows | Unique added | Overlapping IDs by first language | Same IDs as | Stop reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| en | 60 | 12000 | 11679 | 11679 | — | — | window_edge |
| es | 13 | 2600 | 2379 | 2379 | — | — | window_edge |
| pt | 9 | 1800 | 1464 | 1464 | — | — | window_edge |
| fr | 11 | 2200 | 1943 | 1943 | — | — | window_edge |
| ar | 6 | 1200 | 817 | 817 | — | — | window_edge |
| id | 5 | 1000 | 755 | 755 | — | — | window_edge |
| ru | 6 | 1200 | 804 | 804 | — | — | window_edge |
| de | 4 | 800 | 449 | 449 | — | — | window_edge |
| ko | 3 | 600 | 329 | 329 | — | — | window_edge |
| it | 3 | 600 | 337 | 337 | — | — | window_edge |
| th | 2 | 400 | 188 | 188 | — | — | window_edge |
| vi | 3 | 600 | 314 | 314 | — | — | window_edge |
| tr | 4 | 800 | 450 | 450 | — | — | window_edge |
| ja | 2 | 400 | 194 | 194 | — | — | window_edge |
| hi | 1 | 47 | 13 | 13 | — | — | no_continuation |
| nl | 2 | 381 | 71 | 71 | — | — | window_edge |
| pl | 2 | 400 | 149 | 149 | — | — | window_edge |
| sv | 1 | 141 | 26 | 26 | — | — | no_continuation |
| da | 1 | 53 | 14 | 14 | — | — | no_continuation |
| nb | 1 | 63 | 14 | 14 | — | — | no_continuation |
| fi | 1 | 53 | 9 | 9 | — | — | no_continuation |
| cs | 2 | 225 | 49 | 49 | — | — | window_edge |
| el | 1 | 192 | 32 | 32 | — | — | no_continuation |
| hu | 1 | 185 | 35 | 35 | — | — | no_continuation |
| ro | 2 | 309 | 57 | 57 | — | — | window_edge |
| uk | 2 | 400 | 144 | 144 | — | — | window_edge |
| bg | 1 | 103 | 22 | 22 | — | — | no_continuation |
| hr | 1 | 56 | 18 | 18 | — | — | no_continuation |
| sk | 1 | 78 | 23 | 23 | — | — | no_continuation |
| sr | 1 | 67 | 14 | 14 | — | — | no_continuation |
| iw | 2 | 400 | 57 | 57 | — | — | window_edge |
| fa | 3 | 600 | 307 | 307 | — | — | window_edge |
| ur | 1 | 3 | 1 | 1 | — | — | no_continuation |
| bn | 1 | 35 | 12 | 12 | — | — | no_continuation |
| ta | 1 | 5 | 1 | 1 | — | — | no_continuation |
| mr | 1 | 4 | 2 | 2 | — | — | no_continuation |
| ms | 1 | 86 | 19 | 19 | — | — | no_continuation |
| fil | 1 | 3 | 1 | 1 | — | — | no_continuation |
| zh-TW | 2 | 400 | 106 | 106 | — | — | window_edge |
| zh-CN | 3 | 600 | 384 | 384 | — | — | window_edge |
| ca | 1 | 39 | 10 | 10 | — | — | no_continuation |

## App Store pages served per storefront (before cap)

| Storefront | Pages served | Rows fetched | In-window rows | Unique added | Stop reason | Rejected page |
| --- | --- | --- | --- | --- | --- | --- |
| us | 10 | 450 | 450 | 450 | page_limit_http_400 | 11 |
| gb | 5 | 250 | 186 | 186 | window_edge | — |
| in | 5 | 250 | 190 | 190 | window_edge | — |
| ca | 5 | 250 | 181 | 181 | window_edge | — |
| au | 3 | 150 | 97 | 97 | window_edge | — |
| de | 6 | 250 | 178 | 178 | window_edge | — |
| fr | 6 | 300 | 224 | 224 | window_edge | — |
| es | 4 | 200 | 128 | 128 | window_edge | — |
| br | 5 | 250 | 188 | 188 | window_edge | — |
| mx | 4 | 200 | 104 | 104 | window_edge | — |
| jp | 6 | 300 | 238 | 238 | window_edge | — |
| kr | 4 | 200 | 128 | 128 | window_edge | — |
| id | 2 | 50 | 0 | 0 | window_edge | — |
| sg | 2 | 81 | 16 | 16 | window_edge | — |
| ae | 2 | 50 | 0 | 0 | window_edge | — |

## Locales with no in-window reviews

appstore: id, appstore: ae
