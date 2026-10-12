# Taxonomy v1 (Claude run)

Written by Claude after reading a stratified sample of 260 reviews from the Oct 12, 2026 scrape
(26,000 reviews of the Claude app, Jul 14 to Oct 11, 2026). Machine-readable copy:
`analysis/taxonomy.json`. The prompt the model sees: `docs/annotation_prompt.md`. If these three
disagree, `taxonomy.json` wins for validation and this file gets fixed.

The six labels are the same as in the Perplexity and Indeed runs. The categories are new.

## Labels: what kind of review is it

One or two per review. The first is the primary label.

| Label | Use when | Categories |
|---|---|---|
| Specific Praise | Positive, and names a feature, a quality, or a use case | 1-2 |
| Specific Complaint | Negative, and names a concrete problem | 1-2 |
| Feature Request | Asks for something to be added, changed, or made free | 1-2 |
| Generic Good | Positive with nothing specific ("great app", "best AI") | none |
| Generic Bad | Negative with nothing specific ("worst app", "useless") | none |
| Nonsense | Unintelligible, off-topic, wrong app, abuse with no product content | none |

Rules:

- **Specific outranks generic.** "Good app but the limit is too low" is `Specific Complaint, Generic Good`.
- **Two specific labels:** order by which takes more of the text. Tie goes to the complaint.
- **Never pair** Generic Good with Specific Praise, Generic Bad with Specific Complaint, or Generic
  Good with Generic Bad. Nonsense always stands alone.
- **Naming a use case or quality counts as specific.** "Great for coding" is Specific Praise.
- **A comparison alone is not specific.** "ChatGPT is better" is Generic Bad with a competitor tag.

## Categories: what part of the product

Up to two, most important first. Empty for Generic Good, Generic Bad, and Nonsense.

| Category | Covers |
|---|---|
| Paid Plan Limits | Usage limits when the reviewer says they pay (Pro, Max, a subscription, 5x or 20x): running out, five-hour or weekly limits, limits that shrank, extra usage credits |
| Free & Unstated Limits | Usage limits when the reviewer is on the free plan or does not say which plan: messages run out, long waits to reset, upgrade prompts |
| Pricing & Value | Too expensive, good value, regional or student pricing, payment methods, asking for a cheaper tier |
| Billing & Subscription | Charges, refunds, cancelling, a paid upgrade that did not apply, a subscription lost or still charged |
| Account Bans & Age Checks | Accounts banned, suspended, or put on hold; under-18 detection; identity or age verification; appeals |
| Customer Support | Support not answering or not resolving; no human to reach |
| Answer Accuracy | Wrong, invented, or contradictory answers; ignoring or misreading instructions; praise for being correct, honest, or reliable |
| Tone & Refusals | Refusals, safeguards and content filters, moralizing, bias, arguing or pushing back, getting defensive, verbosity; praise for a direct, honest, or human tone |
| Models & Model Quality | A named model or model choice (Opus, Sonnet, Haiku, Fable), a model that got dumber or duller, asking for a model, praise for a model's intelligence or reasoning |
| Coding & Claude Code | Programming help, Claude Code, Remote Control, building apps or scripts |
| Cowork & Agents | Cowork, scheduled tasks, agent work, MCP and connectors, integrations with other tools |
| Writing & Creative | Writing, editing, letters, scripts, creative writing, roleplay, storytelling |
| Web Search & Research | Web search, sources and links, freshness of information, research and analysis depth |
| Images & Files | No image generation or editing, reading images, file uploads and downloads, artifacts, generated documents |
| Voice & Dictation | Voice mode, voices, dictation and transcription, read-aloud |
| Memory & Chats | Memory across chats, lost context in long chats, chat length limits, chat search and organisation, Projects and project knowledge |
| Reliability & Bugs | Crashes, errors, overloaded or at-capacity messages, cut-off responses, features that stopped working after an update |
| Speed | Fast or slow |
| Login & Availability | Sign-in and sign-up problems, phone-number requirement, the app not being available in a country |
| UI / UX | Layout, navigation, sidebar, tablet and foldable layout, widgets, notifications, themes, ease of use |
| Language Support | Interface or answers not available in the reviewer's language, replies in the wrong language, quality in a non-English language |
| Privacy & Company | Data and privacy worries, training data, data centers, AI risk, watermarking, objections to Anthropic as a company |
| Use Cases | What they use it for when no feature is named: study, homework, work, daily tasks, advice, personal support |
| Other | Specific, but fits nothing above |

Tie-breakers the sample forced:

- **Paid vs free limits.** The split rests on what the reviewer says. Says they pay: Paid Plan
  Limits. Free, or plan not stated: Free & Unstated Limits. The second bucket therefore holds some
  paying users who didn't say so; the site says this wherever the two are compared.
- **Bans vs billing.** A banned or held account is Account Bans & Age Checks first, even when the
  complaint is about money; Billing & Subscription goes second.
- **Accuracy vs tone.** Wrong or off-target is Answer Accuracy. Refusing, lecturing, or arguing is
  Tone & Refusals.
- **Models.** Only when a model is named or the model itself is said to have changed.
- **Capacity.** "Overloaded" and "high traffic" messages are Reliability & Bugs, not limits.
- **Image generation.** Claude doesn't generate images, so nearly every mention is a Feature Request
  under Images & Files.

## Other fields from the model

| Field | Rule |
|---|---|
| `sentiment_rating` | 1-5 from the text alone, ignoring the stars. Nonsense gets 3. |
| `language` | ISO 639-1 code of the text as written. Emoji-only or undeterminable is `und`. |
| `english_translation` | Faithful translation when the language isn't English. Empty otherwise. |
| `topic` | 2-6 lowercase English words naming the specific thing. Empty for generic and nonsense. |
| `competitors` | Products named in the text, from the fixed list. Claude's own models and Anthropic's own products don't count. |
| `regression_claim` | True when the reviewer says the product got worse than it used to be. |

## Computed in code, never by the model

| Column | Rule |
|---|---|
| `rating_mismatch` | abs(stars - sentiment) >= 2 |
| `is_low_signal` | No categories. Counted in volume and ratings, excluded from topic work. |
| `is_duplicate_text` | Normalized text appears 3 or more times in the corpus. |
| `is_truncated` | Android text is 500 characters or longer (Play cuts reviews there). |
| `needs_translation` | `language` is not `en` and not `und`. |

## A conflict to keep in view

The labeling model is Claude Haiku, and the product being reviewed is Claude. The gold-set check
(`docs/handover/02-eval.md`) is the control: 120 reviews labeled by hand before the model saw them.
The site states this in its footer.

## What the sample showed

Read before anything was labeled, so these were expectations to test, not findings:

- Usage limits dominate the complaints, from paying and free users alike.
- Account bans tied to under-18 detection and identity checks are a distinct, angry cluster.
- Refusals, pushback, and "the new model is duller" recur, mostly from long-time users.
- Praise clusters on coding, writing, honesty, and reasoning quality.
- Image generation is the most common named request.
