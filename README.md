# Financial Engineering I (F414) — Workshop

**Universidad de San Andrés**

Instructor: Prof. Federico Glancszpigel
Year: 2026

---

# About This Repository

This repository contains the materials for the **practical sessions** of the course **Financial Engineering I (F414)**.

These sessions run **in parallel to the theoretical lectures** of the course.  
While the theoretical lectures focus on financial models and theory, the workshop track focuses on **implementation and real-world applications**.

The goal of the practical sessions is to teach students how to:

- translate financial research into trading strategies
- implement quantitative signals
- construct systematic portfolios
- build realistic backtesting systems
- design production-level trading frameworks

These sessions function as a **quantitative research lab**, where students transform financial ideas into **working investment strategies**.

---

# Practical Track Philosophy

A large fraction of systematic investment strategies used by hedge funds can be traced back to a **small number of core strategy families**.

The practical track studies these strategies through the academic papers that introduced them and focuses on **implementing them in code**.

Students repeatedly follow the same pipeline used by quantitative researchers.

---

# Strategy Development Pipeline

Each practical lecture follows a structured workflow used in quantitative finance.

## 1. Conceptual Framework

- What anomaly or phenomenon is observed?
- What economic hypothesis explains it?
- Why might the anomaly persist?

## 2. Quantitative Signal Construction

- How do we measure the anomaly?
- How do we test statistically that it exists?

Examples of signals:

- momentum = past returns
- value = book-to-market
- carry = interest rate differential
- quality = profitability metrics

## 3. Portfolio Construction

Given a signal:

- what do we buy?
- what do we sell?

Typical structures include:

- long-short portfolios
- market-neutral portfolios
- factor portfolios

## 4. Backtesting

Each strategy is evaluated using a realistic backtest including:

- transaction costs
- turnover
- realistic rebalancing
- out-of-sample evaluation

## 5. Paper Replication

Students replicate the key empirical results from the academic paper discussed in class.

## 6. Discussion and Limitations

We analyze:

- implementation challenges
- robustness
- model risk
- real-world constraints

---

# Strategy Families Covered

The practical track covers **eight major strategy families** widely used in systematic investing.

- Trend Following (Time-Series Momentum)
- Momentum (Cross-Sectional Momentum)
- Value
- Quality / Profitability
- Low Volatility
- Carry Trade
- Volatility Risk Premium
- Statistical Arbitrage

These strategies represent the **core building blocks of quantitative investing**.

---

# Lectures

## Lecture 01 — Trend Following Strategies

Theme: **Time-Series Momentum**

Reference paper:

Moskowitz, Ooi, Pedersen  
*Time Series Momentum (2012)*

Topics:

- trend following strategies
- time-series momentum
- multi-asset strategies
- volatility scaling
- CTA-style trading systems

Folder: `Lecture 01 - Trend Following Strategies`

---

## Lecture 02 — Factor Investing: Momentum

Theme: **Cross-Sectional Momentum**

Reference paper:

Jegadeesh & Titman  
*Returns to Buying Winners and Selling Losers (1993)*

Topics:

- momentum anomaly
- ranking portfolios
- long-short factor portfolios
- momentum crashes
- volatility-managed momentum

Folder: `Lecture 02 - (Factor Investing) Momentum`

---

## Lecture 03 — Factor Investing: Value

Theme: **Value Investing**

Reference paper:

Fama & French  
*The Cross-Section of Expected Stock Returns (1992)*

Topics:

- value anomaly
- book-to-market signals
- factor portfolios
- value vs growth

Folder: `Lecture 03 - (Factor Investing) Value`

---

## Lecture 04 — Factor Investing: Quality

Theme: **Profitability and Quality**

Reference paper:

Novy-Marx  
*The Other Side of Value: The Gross Profitability Premium (2013)*

Topics:

- profitability signals
- accounting-based factors
- quality portfolios
- Quality Minus Junk

Folder: `Lecture 04 - (Factor Investing) Quality`

---

## Lecture 05 — Factor Investing: Low Volatility

Theme: **Low Risk Anomaly**

Reference paper:

Frazzini & Pedersen  
*Betting Against Beta (2014)*

Topics:

- low volatility anomaly
- leverage constraints
- beta estimation
- defensive equity portfolios

Folder: `Lecture 05 - (Factor Investing) Low Vol`

---

## Lecture 06 — Carry Trade

Theme: **Currency Carry**

Reference paper:

Lustig, Roussanov, Verdelhan  
*Common Risk Factors in Currency Markets*

Topics:

- interest rate differentials
- FX carry strategies
- currency portfolios
- global risk exposure

Folder: `Lecture 06 - Carry Trade`

---

## Lecture 07 — Volatility Risk Premium

Theme: **Volatility Risk Premium**

Reference paper:

Bollerslev, Tauchen, Zhou  
*Expected Stock Returns and Variance Risk Premia (2009)*

Topics:

- implied vs realized volatility
- variance risk premium
- VIX-based strategies
- volatility timing

Folder: `Lecture 07 - Volatility Risk Premium`

---

## Lecture 08 — Statistical Arbitrage

Theme: **Mean Reversion and Relative Value**

Reference paper:

Gatev, Goetzmann, Rouwenhorst  
*Pairs Trading (2006)*

Topics:

- pairs trading
- spread construction
- mean reversion
- market-neutral portfolios

Folder: `Lecture 08 - Statistical Arbitrage`

---

## Lecture 09 — Portfolio Optimization

Theme: **Combining Alpha Signals**

Reference paper:

Clarke, Silva, Thorley  
*Portfolio Constraints and the Fundamental Law of Active Management (2001)*

Topics:

- Fundamental Law of Active Management
- information coefficient
- signal diversification
- alpha portfolio construction

Methods discussed:

- equal weight portfolios
- risk parity
- mean-variance optimization
- volatility targeting

Goal: Understand how **multiple weak signals can be combined to produce a strong portfolio**.

Folder: `Lecture 09 - Portfolio Optimization`

---

# Final Project

Students will design and implement a **production-level quantitative trading strategy**.

## Groups

Maximum **4 students per group**.

## Strategy Choice

Each group must choose **one strategy family** studied in the course.

## Literature Requirements

The project must be based on:

- the paper discussed in class
- the complementary paper assigned as homework
- two additional academic papers chosen by the group

## System Requirements

Students must build a **fully functional trading framework**.

The system must allow users to:

- run backtests
- monitor performance
- log trades
- track portfolio performance
- connect to a broker API
- execute trades automatically

The system must include either:

- a CLI interface, or
- a graphical user interface.

---

# Repository Structure

    ├── Final Project
    ├── Lecture 01 - Trend Following Strategies
    ├── Lecture 02 - (Factor Investing) Momentum
    ├── Lecture 03 - (Factor Investing) Value
    ├── Lecture 04 - (Factor Investing) Quality
    ├── Lecture 05 - (Factor Investing) Low Vol
    ├── Lecture 06 - Carry Trade
    ├── Lecture 07 - Volatility Risk Premium
    ├── Lecture 08 - Statistical Arbitrage
    ├── Lecture 09 - Portfolio Optimization


Each lecture folder contains:

- academic papers
- lecture notes
- replication notebooks
- datasets
- code examples

---

# Tools Used

The practical track uses modern quantitative research tools.

Main stack:

- Python  
- pandas  
- numpy  
- matplotlib  
- Jupyter notebooks  
- Git / GitHub

---

# Learning Outcomes

By the end of the practical track students will be able to:

- translate financial research into systematic strategies
- implement realistic backtests
- evaluate strategy performance critically
- design diversified alpha portfolios
- build deployable trading systems
- understand the main drivers of quantitative investment returns