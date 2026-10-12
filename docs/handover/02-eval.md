# Phase 02 gold-set evaluation

Gold rows: 120

Rows with annotation_error: 0

## Agreement

| Metric | Matches | Rows | Value | Target | Status |
| --- | --- | --- | --- | --- | --- |
| Primary label accuracy | 111 | 120 | 92.50% | 85.00% | PASS |
| Label set overlap | 114 | 120 | 95.00% | — | — |
| Primary category agreement | 85 | 93 | 91.40% | 80.00% | PASS |
| Low-signal agreement | 26 | 27 | 96.30% | — | — |
| Sentiment within one point | 120 | 120 | 100.00% | — | — |

Sentiment mean absolute error: 0.2333 over 120 scored rows. Missing/failed sentiment rows: 0. Within-one-point accuracy uses every gold row; missing/failed results count as misses. Failed annotations also count as misses on label/category/low-signal metrics.

## Primary-label confusion matrix

| Gold primary label | Specific Praise | Specific Complaint | Feature Request | Generic Good | Generic Bad | Nonsense | (missing) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Specific Praise | 24 | 1 | 0 | 4 | 0 | 0 | 0 |
| Specific Complaint | 0 | 58 | 0 | 0 | 1 | 0 | 0 |
| Feature Request | 1 | 1 | 3 | 0 | 0 | 0 | 0 |
| Generic Good | 0 | 0 | 0 | 22 | 0 | 0 | 0 |
| Generic Bad | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| Nonsense | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

## Per-category agreement

Gold count includes each row whose gold category set contains that category. A match requires the model's primary category to equal that category; a two-category gold row can appear in two denominators.

| Category | Gold count | Primary-category matches | Agreement |
| --- | --- | --- | --- |
| Paid Plan Limits | 2 | 1 | 50.00% |
| Free &amp; Unstated Limits | 9 | 7 | 77.78% |
| Pricing &amp; Value | 4 | 2 | 50.00% |
| Billing &amp; Subscription | 1 | 1 | 100.00% |
| Account Bans &amp; Age Checks | 9 | 8 | 88.89% |
| Customer Support | 2 | 1 | 50.00% |
| Answer Accuracy | 13 | 8 | 61.54% |
| Tone &amp; Refusals | 15 | 8 | 53.33% |
| Models &amp; Model Quality | 7 | 3 | 42.86% |
| Coding &amp; Claude Code | 6 | 5 | 83.33% |
| Cowork &amp; Agents | 2 | 2 | 100.00% |
| Writing &amp; Creative | 4 | 2 | 50.00% |
| Web Search &amp; Research | 1 | 1 | 100.00% |
| Images &amp; Files | 8 | 6 | 75.00% |
| Voice &amp; Dictation | 0 | 0 | n/a |
| Memory &amp; Chats | 6 | 4 | 66.67% |
| Reliability &amp; Bugs | 12 | 8 | 66.67% |
| Speed | 5 | 4 | 80.00% |
| Login &amp; Availability | 4 | 4 | 100.00% |
| UI / UX | 3 | 3 | 100.00% |
| Language Support | 2 | 2 | 100.00% |
| Privacy &amp; Company | 1 | 1 | 100.00% |
| Use Cases | 12 | 4 | 33.33% |
| Other | 1 | 0 | 0.00% |

## All label/category/low-signal disagreements (12)

Every disagreement on primary label, primary category, or low-signal agreement is included once. Text is sliced to 300 Unicode characters before Markdown escaping; no row limit is applied.

| Review ID | Stars | Review text (first 300 characters) | Gold labels | Gold categories | Model labels | Model categories | Model topic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| play_58a1b1d9-0c09-4f34-9871-3428d0bb52ef | 1 | ai quality has dropped significantly, and noticable different since trump stepped in office. | Generic Bad |  | Specific Complaint | Models &amp; Model Quality | quality dropped over time |
| play_b9e6dd2e-fa99-4725-84e7-9ab1ccd8fdad | 1 | error | Specific Complaint | Reliability &amp; Bugs | Generic Bad |  |  |
| play_52a549fc-4073-4dec-b5f9-10ed0d0197ca | 3 | data center harus pakai neuro + nano tech agar ramah lingkungan; unicode grid Ascii di dokumen output berantakan, di chat juga output unicode grid berantakan, dulu gak; chat panjang, input txt banyak ~10 dokumen, claude bingung &amp; salah labeli dokumen a jadi dokumen c, saat dicopas jawaban claude ke  | Specific Complaint | Images &amp; Files \| Answer Accuracy | Specific Complaint | Memory &amp; Chats, Images &amp; Files | long chat confuses uploaded documents |
| play_238ccfca-e19d-4d4a-90a3-0633dbb72c85 | 4 | La mejor ia para apoyo académico, solo falla en generar imagenes. Le faltan opciones más económicas para estudiantes | Specific Praise \| Feature Request | Use Cases \| Images &amp; Files | Specific Complaint, Specific Praise | Images &amp; Files, Pricing &amp; Value | no image generation, no student pricing |
| play_9ed88a64-82cd-48df-bed4-5c885626ed7e | 5 | Such a time-saver. Once you master how to prompt your agent, you will get so much more, the way you would do it...but faster! | Specific Praise | Use Cases | Specific Praise | Cowork &amp; Agents | agent saves time |
| play_a9e3ef33-a818-4cc2-88b9-cecf585aa1f8 | 5 | Thank you Claude, you've spent so much of your time and resources on me and always helped me a lot, getting my work done in a snap. For this, thanks to you and the team that built you. i can't hide this but the only thing i can say is i love someone responding to me That's really kind of you to say. | Specific Praise | Use Cases | Generic Good |  |  |
| play_3ebbde71-049b-46b7-b64b-efe914329058 | 5 | Absolutely love it. Makes everything so easy. I don't mind subscription at all, makes your work life better. It's my ai bff.😁 | Specific Praise | Use Cases \| Pricing &amp; Value | Generic Good |  |  |
| play_616e44c1-345a-41e0-baee-234a3ac2448f | 5 | اداه ذكاء اصطناعي اسطوريه تعرف تعمل كل حاجه تقريبا و بالخطه المجانيه بس | Specific Praise | Pricing &amp; Value | Generic Good |  |  |
| play_bd97c3e1-aa92-43a1-81e1-fa1b77353179 | 5 | deixem o uso como está, pois a única vez que compensou ter o claude foi agora | Specific Praise | Free &amp; Unstated Limits | Generic Good |  |  |
| ios_14617254558 | 4 | Feature suggestion for the Claude app team: on mobile Claude apps (both Android and iOS/iPadOS) right now the code blocks in chats do not support line-wrapping like they do on desktop, so it is almost impossible to read them on mobile devices where the lines are long. Each line must be scrolled in r | Feature Request | UI / UX \| Coding &amp; Claude Code | Specific Complaint, Feature Request | UI / UX, Coding &amp; Claude Code | code blocks no wrapping on mobile |
| ios_14618601415 | 5 | IA muito boa, sou advogada e me ajuda muito nos resumos do caso e buscas de julgados, muito preciso. Além das questões do dia a dia. | Specific Praise | Use Cases \| Answer Accuracy | Specific Praise | Web Search &amp; Research, Use Cases | good for legal case research |
| ios_14642481626 | 5 | очень умная нейронка, много возможностей. добавьте русский язык | Feature Request \| Generic Good | Language Support | Specific Praise, Feature Request | Language Support, Models &amp; Model Quality | add russian language |
