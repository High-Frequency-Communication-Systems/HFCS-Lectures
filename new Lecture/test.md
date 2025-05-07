---
header-includes:
- |
  ```{=latex}
  \directlua{luaotfload.add_fallback(
               "myfallback",
               {"NotoColorEmoji:mode=harf;"}
             )}
  \setmainfont[RawFeature={fallback=myfallback}]{LatinModernRoman}
  \setmonofont[RawFeature={fallback=myfallback}]{LatinModernMono}
  ```
---

It 😺 lorem 👅 \LaTeX.

```julia
🟡 = 2
```
