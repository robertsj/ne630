#!/usr/bin/env python3
"""Initialize the HW03 NE 630 solution table from typeset submissions."""

from __future__ import annotations

import match_hw04_latex as core


core.HOMEWORK_ID = "hw03"
core.HW_DIR = core.ROOT / "hw03"
core.TABLE_DIR = core.HW_DIR / "tables"
core.ARTIFACT_DIR = core.HW_DIR / "table_artifacts"
core.PDF_TEXT_DIR = core.ARTIFACT_DIR / "pdf_text"
core.STATEMENT_PATH = str(core.NE630_ROOT / "homework/markdown/HW03.md")
core.SOLUTION_PATH = str(core.NE630_ROOT / "homework/solutions/hw03.tex")

core.SPECS = (
    core.AnswerSpec(
        "p01",
        "a",
        "initial_enrichment",
        "Problem 1(a) uranium enrichment at earth formation",
        22.39,
        "percent",
        "22.39 percent",
        1.0,
        r"e(0) \approx \boxed{0.2239 = 22.39\%}",
        (
            r"Final\s+(?:answer|Result)\s*\(a\)",
            r"(?:initial|earth)[^\n]{0,80}enrichment",
            r"e\(0\)\s*(?:=|≈)",
        ),
        ("enrichment", "%", "22"),
        10.0,
        40.0,
    ),
    core.AnswerSpec(
        "p01",
        "b",
        "time_ago_4_percent",
        "Problem 1(b) time ago when enrichment was 4 percent",
        2.14e9,
        "yr",
        "2.14e9 yr ago",
        0.15e9,
        r"\boxed{2.14\cdot 10^{9}~\mathrm{y}}",
        (
            r"Final\s+(?:answer|Result)\s*\(b\)",
            r"how\s+long\s+ago",
            r"(?:ago|before present)[^\n]{0,80}(?:10|billion|Gyr)",
        ),
        ("ago", "yr", "10"),
        1.0e9,
        3.2e9,
    ),
    core.AnswerSpec(
        "p02",
        "",
        "irradiation_time",
        "Problem 2 irradiation time for 25 Ci",
        12.54,
        "d",
        "12.54 d",
        0.5,
        r"t \approx \boxed{1.083\cdot 10^{6}~\mathrm{s} \approx 12.54~\mathrm{d}}",
        (
            r"Final\s+(?:answer|Result)",
            r"(?:irradiated|irradiation|time)[^\n]{0,120}(?:d|day)",
            r"t\s*(?:=|≈)[^\n]{0,80}(?:d|day)",
        ),
        ("time", "d", "day"),
        5.0,
        20.0,
    ),
)

core.TEXT_SPECS = (
    core.TextSpec(
        "p03",
        "a",
        "na_nb_time",
        "Problem 3(a) N_A(t) and N_B(t)",
        "algebraic",
        (
            r"N_A(t)=\frac{A_0}{\lambda_A}(1-e^{-\lambda_A t}); "
            r"N_B(t)=\frac{A_0}{\lambda_B}(1-e^{-\lambda_B t})-"
            r"\frac{A_0}{\lambda_B-\lambda_A}(e^{-\lambda_A t}-e^{-\lambda_B t})"
        ),
        r"\Aboxed{N_A(t)=...}; \Aboxed{N_B(t)=...}",
    ),
    core.TextSpec(
        "p03",
        "b",
        "steady_state_limits",
        "Problem 3(b) long-time N_A and N_B",
        "algebraic",
        r"N_A(\infty)=A_0/\lambda_A,\quad N_B(\infty)=A_0/\lambda_B",
        r"\boxed{N_A(\infty)=A_0/\lambda_A,\ N_B(\infty)=A_0/\lambda_B}",
    ),
)


if __name__ == "__main__":
    core.main()
