
# Project Ainu Kamuichika

## Purpose (English)
This project, named after Kamuichika—the Owl God of the Ainu, guardian of people and villages, and the spirit who first appears in the Ainu shin'yōshū—stands as a bridge between tradition and the ever-advancing era. 

Inspired by the words of Yukie Chiri, who wrote: “However, one day, two or three strong individuals among us will arise and walk alongside the ever-advancing era. That day will eventually come. This is our urgent wish. This is our prayer for day and night.”

Now, as Ainu language and culture walk hand in hand with Artificial Intelligence, this project seeks to honor the past and embrace the future. Through the wisdom of Kamuichika and the power of AI, we strive to nurture, protect, and renew the stories, chants, and voices of the Ainu people.

Our purpose is to explore how AI can be used for research and preservation of Ainu culture, and to create translations that are not only accurate, but poetic and elegant — so that the soul of the Ainu may continue to sing, and the prayers of day and night may echo in new generations.

This project provides an advanced translation agent for Ainu chants, focusing on Japanese, Traditional Chinese, and English. It automates the translation process, ensuring high-quality, poetic, and accurate translations for both main stories and footnotes of Ainu oral literature, always with a human-in-the-loop for the final touch.

## 宗旨（繁體中文）
這個項目名為 “Project Ainu Kamuichika”，以守護村落與人民的貓頭鷹神Kamuichika為名，亦是《阿伊努神謠集》首篇吟唱的神靈。它如同一座橋樑，連接傳統與不斷前進的時代。

靈感源自知里幸惠的序言：「但總有一天，如果能出現兩三位堅強的人，與不斷前進的時代並肩前行的日子，也終將到來吧。這確實是我們迫切的願望，我們日夜為此祈禱。」

如今，愛努語言與文化正與人工智慧攜手並行。本項目以 Kamuichika 的智慧與 AI 的力量，守護、滋養並再生愛努的故事、謠曲與聲音。

我們的宗旨是探索 AI 如何用於愛努文化的研究與保存，並創造既精確又詩意優雅的譯文 —— 讓愛努的靈魂得以繼續歌唱，讓日夜的祈禱在新世代中迴響。

本項目提供愛努謠曲的 AI 翻譯代理，聚焦日語、繁體中文與英語。它自動化翻譯流程，確保主故事與註腳皆能獲得高品質、詩意且精確的譯文，並始終由人類審定。


## Techniques & Approach



Core components:

- Agentic notebooks for reproducible workflows.
- Prompt templates to steer tone and generate footnotes.
- Parallel/direct vs. cross-translation with automated reflection and scoring.
- Human-in-the-loop QA and lightweight automated evaluation.

This balances computational rigor with literary care to preserve voice while making texts sing in new tongues.

## Key Files & Structure

```
ainu_kamuy_yukar/
├─ AgenticTranslation_workflow_adk_main_text.ipynb
│   — Notebook for main-text translation experiments and runs.
├─ AgenticTranslation_workflow_adk_footnotes.ipynb
│   — Notebook for generating and editing footnotes/annotations.
├─ AgenticTranslationOutput_adk_main_text/     — Generated main-text outputs (markdown/JSON).
├─ AgenticTranslationOutput_adk_footnotes/     — Generated footnotes and annotation artifacts.
├─ Chiri_Japanese_Translation/                 — Project-specific Japanese source texts and drafts.
├─ Chiri_footnotes/                            — Footnote drafts and notes for Chiri texts.
├─ templates/
│  ├─ updated_output_md_template               — Markdown template for standardized outputs.
│  └─ updated_footnotes_md_template             — Template for footnotes and annotation blocks.
├─ utils/
│  └─ md_to_html_json.py                        — Helper: convert markdown to HTML + JSON metadata.
├─ original_Ainu_text/                         — Scanned/transcribed original Ainu source texts.
├─ Manual_updated_Translation/
│  ├─ Chinese_Translation/                      — Human-edited Traditional Chinese translations.
│  └─ English_Translation/                      — Human-edited English translations.
└─ translation_agent_adk/
   ├─ agent.py                                 — Core agent orchestration and run logic.
   ├─ prompt.py                                — Prompt templates and prompt-building utilities.
   ├─ config.py                                — Configuration and runtime settings.
   ├─ schema.py                                — Data schemas for outputs and exchanges.
   └─ .env                                     — Environment variables (API keys, model selection).
```

Webpage / Interface
-------------------

There is a lightweight web/demo interface in `vibe_web_interface/` (if present) for quick inspection of outputs and demoing translations. The primary interaction method is via the notebooks; the web UI is optional and intended for review and demonstration rather than production use.

How to Use
----------

1. Open `v2_translation_agent.ipynb` in Jupyter or compatible environment and follow the notebook cells in order.
2. Adjust prompt templates in `templates/` if you want different translation/annotation behavior.
3. Inspect generated files in `AgenticTranslationOutput_*` and apply manual edits in `Manual_updated_Translation/`.

Licensing
---------

Check `LICENSE.txt` in this folder for license specifics relating to the translation artifacts. Source texts may have separate copyright terms — consult `original_Ainu_text/` and the included license file before redistributing.

References
----------

- Ainu language resources and corpora used as source material (see `original_Ainu_text/` for provenance notes).
- Translation workflow inspiration: human+LLM hybrid translation literature and agentic workflows using stepwise prompting.

Contact & Contribution
----------------------

If you'd like changes, submit issues or pull requests. For questions about methodology or licensing, contact the repository owner.

