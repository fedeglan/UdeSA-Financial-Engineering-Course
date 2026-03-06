# UdeSA – Financial Engineering I (F414) - Workshop

This course introduces students to the **design, implementation, and evaluation of quantitative trading strategies** grounded in academic research and implemented with modern data and software tools.

The course combines:

- Academic finance literature
- Systematic trading strategies
- Quantitative modeling
- Realistic backtesting
- Portfolio construction
- Production-level strategy design

The goal is to bridge the gap between **financial research** and **real-world quantitative investment systems**.

---

# Course Philosophy

Most successful quantitative investment strategies can be grouped into a small number of **core strategy families** used widely by hedge funds and asset managers.

In this course we study these strategies by:

1. Understanding the **economic intuition** behind them
2. Translating the intuition into a **quantitative signal**
3. Constructing a **systematic portfolio**
4. Implementing a **realistic backtest**
5. Replicating key results from the **academic literature**
6. Discussing **limitations and robustness**

Each lecture follows a common framework:

### 1. Conceptual structure

- Economic hypothesis  
- Why the anomaly exists  
- Whether it is likely to persist  

### 2. Signal construction

- How the phenomenon is quantified
- How we empirically test the hypothesis

### 3. Portfolio construction

- What we buy and sell given the signal

### 4. Backtesting

- Strategy pipeline
- Dataset
- Realistic transaction costs
- Performance evaluation

### 5. Paper replication

Replicate key empirical results from the reference paper.

### 6. Discussion and limitations

- Robustness
- Implementation constraints
- Real-world risks

---

# Course Structure

The course covers **eight major strategy families** used in systematic investing, followed by a lecture on **portfolio optimization and alpha combination**.

---

# Lectures

## Lecture 01 – Trend Following Strategies

Theme:
**Time-Series Momentum**

Reference paper:

Moskowitz, Ooi, Pedersen  
*Time Series Momentum (2012)*

Topics:

- Trend following intuition
- Time-series momentum signal
- Multi-asset strategies
- Volatility scaling
- CTA-style trading systems

---

## Lecture 02 – Factor Investing: Momentum

Theme:
**Cross-Sectional Momentum**

Reference paper:

Jegadeesh & Titman  
*Returns to Buying Winners and Selling Losers (1993)*

Topics:

- Momentum anomaly
- Ranking strategies
- Long-short portfolios
- Momentum crashes
- Volatility-managed momentum

---

## Lecture 03 – Factor Investing: Value

Theme:
**Value Investing**

Reference paper:

Fama & French  
*The Cross-Section of Expected Stock Returns (1992)*

Topics:

- Value anomaly
- Book-to-market signals
- Portfolio sorting
- Multi-factor models
- Value vs momentum

---

## Lecture 04 – Factor Investing: Quality

Theme:
**Profitability and Quality**

Reference paper:

Novy-Marx  
*The Other Side of Value: The Gross Profitability Premium (2013)*

Topics:

- Profitability signals
- Quality factor construction
- Accounting-based signals
- Quality-minus-junk portfolios

---

## Lecture 05 – Factor Investing: Low Volatility

Theme:
**Low Risk Anomaly**

Reference paper:

Frazzini & Pedersen  
*Betting Against Beta (2014)*

Topics:

- Low-volatility anomaly
- Beta estimation
- Levered low-beta portfolios
- Risk parity intuition

---

## Lecture 06 – Carry Trade

Theme:
**Currency Carry**

Reference paper:

Lustig, Roussanov, Verdelhan  
*Common Risk Factors in Currency Markets*

Topics:

- Interest rate differentials
- FX carry strategies
- Currency portfolios
- Global risk factors

---

## Lecture 07 – Volatility Risk Premium

Theme:
**Selling Insurance in Financial Markets**

Reference paper:

Bollerslev, Tauchen, Zhou  
*Expected Stock Returns and Variance Risk Premia (2009)*

Topics:

- Implied vs realized volatility
- Variance risk premium
- VIX-based signals
- Volatility timing

---

## Lecture 08 – Statistical Arbitrage

Theme:
**Mean Reversion and Relative Value**

Reference paper:

Gatev, Goetzmann, Rouwenhorst  
*Pairs Trading (2006)*

Topics:

- Pairs trading
- Cointegration intuition
- Spread trading
- Market-neutral portfolios

---

## Lecture 09 – Portfolio Optimization

Theme:
**Combining Alpha Signals**

Topics:

- The Fundamental Law of Active Management
- Information coefficient (IC)
- Breadth and signal independence
- Alpha diversification
- Portfolio construction methods

Methods covered:

- Equal-weight portfolios
- Risk parity
- Mean-variance optimization
- Volatility targeting

Goal:

Understand how **multiple weak signals can be combined to produce a strong portfolio**.

---

# Final Project

Students will work in groups (up to **4 students**) to design a **production-level quantitative trading strategy** based on one of the strategy families studied in the course.

Project requirements include:

- Literature review
- Strategy design
- Realistic backtesting
- Robustness analysis
- Production-grade implementation

Students must build a framework capable of:

- Running backtests
- Monitoring performance
- Logging trades
- Connecting to a broker API
- Executing trades automatically

More details are available in */Final Project*.

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


Each lecture contains:

- notebooks
- datasets
- paper references
- replication code

---

# Tools Used in the Course

Students are encouraged to use modern development tools including:

- Python
- Jupyter notebooks
- Git
- AI-assisted development tools (E.g: ChatGPT, Claude, Cursor, Codex, ClaudeCode, OpenClaw, etc.)

---

# Learning Outcomes

By the end of the course students will be able to:

- Translate financial research into systematic strategies
- Implement robust backtesting pipelines
- Evaluate strategy performance realistically
- Understand the core sources of quantitative alpha
- Combine signals into a diversified portfolio
- Build deployable trading systems

---

# Instructor

Prof. Federico Glancszpigel
Universidad de San Andrés